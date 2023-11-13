#!/usr/bin/node

const { argv } = require('node:process');

if (argv.index(0) == undefined)
{
    console.log("undefined is undefined");
}
else if (argv.index(1) == undefined)
{
    console.log(argv.index(0) + " is undefined");
}
else
{
    console.log(argv.index(0) + " is " + argv.index(1));
}

