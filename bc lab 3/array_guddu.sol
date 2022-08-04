pragma solidity ^0.5.0;
/*
    --operations--
    1. push
    2. pop
    3. delete
    4. display
*/
contract harshu {
    uint[] public arr;
    function get(uint i) public view returns (uint) {
        return arr[i];
    }
    function display() public view returns (uint[] memory) {
        return arr;
    }
    function push(uint i) public {
        arr.push(i);
    }
    function pop() public {
        arr.pop();
    }
    function getLength() public view returns (uint) {
        return arr.length;
    }
    function remove(uint index) public {
        delete arr[index];
    }
}