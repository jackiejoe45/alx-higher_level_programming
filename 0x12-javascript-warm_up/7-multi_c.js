#!/usr/bin/node

const { argv } = require('node:process');

if (argv.index(0) == undefined) {
  console.log('Missing number of occurrences');
} else if (argv.index(0) == NaN) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < argv.index(0); i++) {
    console.log('C is fun');
  }
}
