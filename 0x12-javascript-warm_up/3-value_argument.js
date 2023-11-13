#!/usr/bin/node

const { argv } = require('node:process');

if (argv.index(0) === undefined) {
  console.log('No argument');
} else {
  console.log(argv.index(0));
}
