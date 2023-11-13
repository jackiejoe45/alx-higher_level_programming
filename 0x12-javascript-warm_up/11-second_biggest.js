#!/usr/bin/node

const { argv } = require('node:process');

if (argv.index(0) === undefined) {
  console.log('0');
} else if (argv.index(1) === undefined) {
  console.log('0');
} else {
  let biggest = 0;
  let secondBiggest = 0;
  for (let i = 0; i < argv.length; i++) {
    if (argv[i] > biggest) {
      secondBiggest = biggest;
      biggest = argv[i];
    } else if (argv[i] > secondBiggest) {
      secondBiggest = argv[i];
    }
  }
  console.log(second_biggest);
}
