#!/usr/bin/node
const { argv } = require('node:process');

if (length(argv) == 0 )
{
    console.log("No argument");
}
else if (length(argv) == 1)
{
    console.log("Argument found");
}
else
{
    console.log("Arguments found");
}

