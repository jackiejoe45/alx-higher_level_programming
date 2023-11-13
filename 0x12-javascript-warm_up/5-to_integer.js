#!/usr/bin/node

const { argv } = require('node:process');

if (argv.index(0) === undefined) {
  console.log('Not a number');
} else if (isNaN(argv.index(0))) {
  console.log('Not a number');
} else {
  console.log('My number: ' + argv.index(0));
}
