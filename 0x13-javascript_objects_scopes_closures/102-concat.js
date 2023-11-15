#!/usr/bin/node

const fs = require('fs');
const args = process.argv.slice(2);
const file1 = args[0];
const file2 = args[1];

fs.readFile(file1, 'utf8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    fs.appendFile(file2, data, function (err) {
      if (err) {
        console.log(err);
      }
    });
  }
});
