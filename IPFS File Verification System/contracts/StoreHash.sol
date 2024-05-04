// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.9.0;

contract StoreHash {
    string ipfsHash;

    function sendHash(string memory x) public {
        ipfsHash = x;
    }

    function getHash() public view returns (string memory) {
        return ipfsHash;
    }
}
