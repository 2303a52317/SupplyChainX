import os, json, sqlite3
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash
try:
    from web3 import Web3
except ImportError:
    Web3 = None  # Optional for local demo mode
import qrcode

app = Flask(__name__)
app.secret_key = "supplychainx-demo-key"
DB = "supplychainx.db"
RPC_URL = os.getenv("RPC_URL", "http://127.0.0.1:7545")
CONTRACT_ADDRESS = os.getenv("CONTRACT_ADDRESS", "")
w3 = Web3(Web3.HTTPProvider(RPC_URL)) if Web3 else None

def db():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with db() as con:
        con.execute("""CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL,
            manufacturer TEXT NOT NULL, description TEXT, current_stage TEXT,
            created_at TEXT, tx_hash TEXT)""")
        con.execute("""CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT, product_id INTEGER,
            stage TEXT, actor TEXT, note TEXT, created_at TEXT, tx_hash TEXT)""")

def contract():
    if Web3 is None or w3 is None or not CONTRACT_ADDRESS or not os.path.exists("contract_abi.json"):
        return None
    with open("contract_abi.json") as f:
        abi = json.load(f)
    return w3.eth.contract(address=Web3.to_checksum_address(CONTRACT_ADDRESS), abi=abi)

def chain_register(pid, name, manufacturer):
    c = contract()
    if not c or not w3 or not w3.is_connected():
        return "LOCAL-DEMO (Ganache/contract not connected)"
    acct = w3.eth.accounts[0]
    tx = c.functions.registerProduct(int(pid), name, manufacturer).transact({"from": acct})
    receipt = w3.eth.wait_for_transaction_receipt(tx)
    return receipt.transactionHash.hex()

def chain_update(pid, stage, actor, note):
    c = contract()
    if not c or not w3 or not w3.is_connected():
        return "LOCAL-DEMO (Ganache/contract not connected)"
    acct = w3.eth.accounts[0]
    tx = c.functions.updateStage(int(pid), stage, actor, note).transact({"from": acct})
    receipt = w3.eth.wait_for_transaction_receipt(tx)
    return receipt.transactionHash.hex()

@app.route("/")
def index():
    with db() as con:
        products = con.execute("SELECT * FROM products ORDER BY id DESC").fetchall()
    return render_template("index.html", products=products, connected=bool(w3 and w3.is_connected()))

@app.route("/add", methods=["POST"])
def add_product():
    name = request.form.get("name", "").strip()
    manufacturer = request.form.get("manufacturer", "").strip()
    description = request.form.get("description", "").strip()
    if not name or not manufacturer:
        flash("Product name and manufacturer are required.")
        return redirect(url_for("index"))
    with db() as con:
        cur = con.execute("INSERT INTO products(name,manufacturer,description,current_stage,created_at) VALUES(?,?,?,?,?)",
                          (name, manufacturer, description, "Manufactured", datetime.now().isoformat(timespec="seconds")))
        pid = cur.lastrowid
    try:
        tx = chain_register(pid, name, manufacturer)
    except Exception as e:
        tx = "BLOCKCHAIN-ERROR: " + str(e)[:160]
    with db() as con:
        con.execute("UPDATE products SET tx_hash=? WHERE id=?", (tx, pid))
        con.execute("INSERT INTO events(product_id,stage,actor,note,created_at,tx_hash) VALUES(?,?,?,?,?,?)",
                    (pid, "Manufactured", manufacturer, "Product registered", datetime.now().isoformat(timespec="seconds"), tx))
    os.makedirs("static/qr", exist_ok=True)
    img = qrcode.make(request.host_url.rstrip("/") + url_for("track", pid=pid))
    img.save(f"static/qr/product_{pid}.png")
    flash(f"Product #{pid} registered.")
    return redirect(url_for("track", pid=pid))

@app.route("/update/<int:pid>", methods=["POST"])
def update_product(pid):
    stage = request.form.get("stage", "").strip()
    actor = request.form.get("actor", "").strip()
    note = request.form.get("note", "").strip()
    allowed = {"Dispatched", "In Transit", "Received by Retailer", "Available for Sale"}
    if stage not in allowed or not actor:
        flash("Choose a valid stage and enter the participant name.")
        return redirect(url_for("track", pid=pid))
    with db() as con:
        exists = con.execute("SELECT id FROM products WHERE id=?", (pid,)).fetchone()
    if not exists:
        flash("Product not found.")
        return redirect(url_for("index"))
    try:
        tx = chain_update(pid, stage, actor, note)
    except Exception as e:
        tx = "BLOCKCHAIN-ERROR: " + str(e)[:160]
    with db() as con:
        con.execute("UPDATE products SET current_stage=?, tx_hash=? WHERE id=?", (stage, tx, pid))
        con.execute("INSERT INTO events(product_id,stage,actor,note,created_at,tx_hash) VALUES(?,?,?,?,?,?)",
                    (pid, stage, actor, note, datetime.now().isoformat(timespec="seconds"), tx))
    flash("Supply-chain stage updated.")
    return redirect(url_for("track", pid=pid))

@app.route("/track/<int:pid>")
def track(pid):
    with db() as con:
        product = con.execute("SELECT * FROM products WHERE id=?", (pid,)).fetchone()
        events = con.execute("SELECT * FROM events WHERE product_id=? ORDER BY id", (pid,)).fetchall()
    if not product:
        flash("Product not found.")
        return redirect(url_for("index"))
    return render_template("track.html", product=product, events=events)

init_db()

if __name__ == "__main__":
    app.run(debug=True)
