#!/usr/bin/node

require('./101-data.js')
  .dict
  .map((value, index) => [value, index])
  .reduce((acc, value) => {
    const [key, index] = value;
    if (acc[key]) {
      acc[key].push(index);
    } else {
      acc[key] = [index];
    }
    return acc;
  }, {})
  .forEach((value, key) => console.log(`${key}: ${value}`));
