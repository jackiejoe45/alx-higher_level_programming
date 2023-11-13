#!/usr/bin/node
/*
Write a script that searches the second biggest integer in the list of arguments.

You can assume all arguments can be converted to integer
If no argument passed, print 0
If the number of arguments is 1, print 0
You must use console.log(...) to print all output
You are not allowed to use var
 */

const { argv } = require('node:process');

if (argv.index(0) == undefined) {
  console.log('0');
} else if (argv.index(1) == undefined) {
  console.log('0');
} else {
  let biggest = 0;
  let second_biggest = 0;
  for (let i = 0; i < argv.length; i++) {
    if (argv[i] > biggest) {
      second_biggest = biggest;
      biggest = argv[i];
    } else if (argv[i] > second_biggest) {
      second_biggest = argv[i];
    }
  }
  console.log(second_biggest);
}
