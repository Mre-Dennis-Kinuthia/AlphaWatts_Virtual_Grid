// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.17;

contract SimpleContract {
  // Declare a state variable to store a value
  uint public value;

  // Constructor function to initialize the contract
  constructor() public {
    value = 0;
  }

  // Function to update the value of the state variable
  function setValue(uint _newValue) public {
    value = _newValue;
  }

  // Function to retrieve the current value of the state variable
  function getValue() public view returns (uint) {
    return value;
  }
}
