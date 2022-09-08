pragma solidity ^0.8.13;
contract Base {
uint xy=10;
function privateFunc() private pure returns (string memory) {
return "private function called";
}
function testPrivateFunc() public pure returns (string memory) {
return privateFunc();
}
function internalFunc() internal pure returns (string memory) {
return "internal function called";
}
function testInternalFunc() public pure virtual returns (string memory) {
return internalFunc();
}
function publicFunc() public view returns (uint) {
return xy;
}
function externalFunc() external pure returns (string memory) {
return "external function called";
}
string private privateVar = "my private variable";
string internal internalVar = "my internal variable";
string public publicVar = "my public variable";
}
contract Child is Base {
function testInternalFunc() public pure override returns (string memory) {
return internalFunc();
}
}
contract Base1 {
Base x= new Base();
function testExternalFunc() public view returns (string memory) {
return x.externalFunc();
}
}
