# 🚚 SupplyChainX
### Blockchain-Based Supply Chain Management System

<p align="center">
  <b>Bringing Transparency, Traceability, and Trust to Supply Chain Management</b>
</p>

---

## 📌 About the Project

**SupplyChainX** is a web-based supply chain management system designed to improve product traceability and transparency throughout the supply chain.

The system allows users to register products, update their supply chain stages, and track product information using unique product IDs and QR codes.

The project demonstrates how blockchain technology and smart contracts can support secure and transparent supply chain operations.

## 🌐 Live Demo

🔗 **Live Application:https://supplychainx-d2gd.onrender.com

📂 **GitHub Repository:https://github.com/2303a52317/SupplyChainX

---

## ✨ Key Features

- **Product Registration:** Register products with details such as product name and manufacturer.
- **Stage Updates:** Update the current stage of a product as it moves through the supply chain.
- **QR Code Generation:** Generate a QR code for each registered product.
- **Product Tracking:** Track products using their unique product ID.
- **Tracking History:** View previously recorded product updates and movement history.
- **Web Dashboard:** Manage and view registered products through a simple interface.
- **Smart Contract Source:** Includes Solidity smart contract code demonstrating blockchain-based product registration and tracking.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Flask | Web application framework |
| SQLite | Local database |
| HTML | Web page structure |
| CSS | User interface styling |
| Solidity | Smart contract development |
| QR Code | Product identification and tracking |
| Git & GitHub | Version control and source code hosting |
| Render | Application deployment |

## 📸 Screenshots

https://github.com/2303a52317/SupplyChainX/blob/main/Screenshot%202026-11-03%20064155.png
https://github.com/2303a52317/SupplyChainX/blob/main/Screenshot%202026-11-03%20064206.png

## ⚙️ Installation and Setup

Follow these steps to run SupplyChainX on your local machine.

### Prerequisites

- Python 3.10 or above
- Git
- A web browser

### Step 1: Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
```

### Step 2: Open the Project Folder

```bash
cd SupplyChainX
```

### Step 3: Create a Virtual Environment

```bash
python -m venv venv
```

### Step 4: Activate the Virtual Environment

**Windows:**
```bash
venv\Scripts\activate
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

### Step 5: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 6: Run the Application

```bash
python app.py
```

### Step 7: Open in Browser

Visit:

```text
http://127.0.0.1:5000
```

The SupplyChainX application should now be running locally.

---

## 📂 Project Structure

```text
SupplyChainX/
│
├── app.py
├── requirements.txt
├── requirements-blockchain.txt
├── README.md
├── .gitignore
│
├── contracts/
│   └── SupplyChainX.sol
│
├── templates/
│   ├── index.html
│   └── track.html
│
├── static/
│   └── style.css
│
└── screenshots/
    ├── dashboard.png
    ├── add-product.png
    ├── tracking.png
    └── qr-code.png
```

## 🔄 How It Works

1. **Product Registration:** A user registers a new product by entering its details.
2. **Product Identification:** The system assigns a unique product ID and generates a QR code.
3. **Stage Updates:** Authorized users can update the product's current supply chain stage.
4. **Product Tracking:** Users can access product information through its tracking page.
5. **History Monitoring:** Previous updates are displayed to provide a record of the product's journey.

## 🔐 Smart Contract

The project includes a Solidity smart contract named `SupplyChainX.sol`.

The contract contains functions for:

- `registerProduct()` – Registers a product.
- `updateStage()` – Updates a product's supply chain stage.
- `getHistory()` – Retrieves the product's update history.

**Implementation note:** The currently deployed demonstration application uses Flask and SQLite. The Solidity contract source is included in the repository, but live blockchain transactions and smart contract deployment are not currently configured.

## 🎯 Project Objectives

- Improve supply chain transparency.
- Make product tracking easier.
- Maintain product movement history.
- Reduce information gaps between supply chain participants.
- Demonstrate the potential use of blockchain and QR codes in supply chain management.

## 🚀 Future Enhancements

- Integrate the deployed Solidity smart contract with the web application.
- Add role-based authentication for manufacturers, distributors, and retailers.
- Integrate IoT devices for real-time product monitoring.
- Develop a mobile application for product tracking.
- Add analytics and reporting features.

## 👥 Team Members

This project was developed as a collaborative team project.

| No. | Team Member | Role |
|---|---|---|
| 1 | Madhavi | Backend Development |
| 2 | Abhiram | Product Registration |
| 3 | Shiva | Smart Contract Development |
| 4 | Varshitha | QR Code and Frontend |
| 5 | Sai Krishna | Integration and Documentation |

*Replace the placeholders with your team members' names.*

## 👨‍🏫 Academic Project

**Project Name:** SupplyChainX – Blockchain-Based Supply Chain Management System

**Project Type:** Academic / Team Project

**Domain:** Blockchain Technology and Web Development

---

<p align="center">
  <b>SupplyChainX – Making Supply Chains More Transparent and Traceable.</b>
</p>
