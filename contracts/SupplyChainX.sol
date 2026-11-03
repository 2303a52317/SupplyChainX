// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract SupplyChainX {
    address public owner;
    struct Product {
        uint256 id;
        string name;
        string manufacturer;
        bool exists;
    }
    struct Update {
        string stage;
        string actor;
        string note;
        uint256 timestamp;
    }
    mapping(uint256 => Product) public products;
    mapping(uint256 => Update[]) private history;

    event ProductRegistered(uint256 indexed productId, string name, string manufacturer);
    event StageUpdated(uint256 indexed productId, string stage, string actor);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only contract owner");
        _;
    }

    constructor() { owner = msg.sender; }

    function registerProduct(uint256 id, string memory name, string memory manufacturer) public onlyOwner {
        require(!products[id].exists, "Product already exists");
        products[id] = Product(id, name, manufacturer, true);
        history[id].push(Update("Manufactured", manufacturer, "Product registered", block.timestamp));
        emit ProductRegistered(id, name, manufacturer);
    }

    function updateStage(uint256 id, string memory stage, string memory actor, string memory note) public onlyOwner {
        require(products[id].exists, "Product does not exist");
        history[id].push(Update(stage, actor, note, block.timestamp));
        emit StageUpdated(id, stage, actor);
    }

    function getHistory(uint256 id) public view returns (Update[] memory) {
        require(products[id].exists, "Product does not exist");
        return history[id];
    }
}
