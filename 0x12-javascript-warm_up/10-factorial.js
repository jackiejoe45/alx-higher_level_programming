#!/usr/bin/node

function factorial(n)
{
    if (n == 0)
    {
        return 1;
    }
    else if (n == NaN) {
        return 1;        
    }
    else
    {
        return n * factorial(n - 1);
    }
}

const { argv } = require('node:process');

console.log(factorial(parseInt(argv.index(0))));
