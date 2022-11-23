//SPDX-License-Identifier : MIT
pragma solidity >=0.5.0 <0.9.0;

contract Banking{
    mapping(address => uint256) user_account;
    mapping(address => bool) user_exists;

    function create_account()public payable returns(string memory){
        require(user_exists[msg.sender]==false, "User already exists");
        if(msg.value==0){
            user_exists[msg.sender] = true;
            user_account[msg.sender] = 0;
            return "User created";
        }
        require(user_exists[msg.sender]==false, "User already exists");
        user_exists[msg.sender] = true;
        user_account[msg.sender] = msg.value;
        return "User Created";
    }
    function deposit()public payable returns(string memory){
        require(user_exists[msg.sender]==true, "User does not exist");
        require(msg.value>0,"The value to deposit is zero");
        user_account[msg.sender]+=msg.value;
        return "Deposited";
    }
    function Withdraw(uint256 amount) public payable returns(string memory){
        require(user_exists[msg.sender]==true, "User doesn't exist");
        require(user_account[msg.sender]>=amount, "The account doesnot contain enough money");
        user_account[msg.sender]-=amount;
        return"Amount Withdrawn";
    }
    function show_amount() public view returns(uint256){
        require(user_exists[msg.sender]==true, "User doesn't exist");
        return user_account[msg.sender];
    }
}   