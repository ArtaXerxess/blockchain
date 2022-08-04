pragma solidity ^0.5.0;
contract harshu
{
    enum Colors{red,blue,green,yellow}
    Colors s;
    function setRed() public{
        s = Colors.red;
    }
    function setBlue() public{
        s = Colors.blue;
    }
    function setGreen() public{
        s = Colors.green;
    }function setYellow() public{
        s = Colors.yellow;
    }
    function returnColors() external view returns(string memory)
    {
        Colors x = s;
        if(x==Colors.red) return "red";
        if(x==Colors.blue) return "blue";
        if(x==Colors.green) return "green";
        if(x==Colors.yellow) return "yellow";
        return "";
    }
}
