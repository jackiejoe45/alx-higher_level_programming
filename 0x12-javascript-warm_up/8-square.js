#!/usr/bin/node

const { argv } = require('node:process');

if (typeof argv.index(0) != Number) {
    console.log("Missing size");
}
else {
    for (let i = 0; i < argv.index(0); i++) {
        for (let j = 0; j < argv.index(0); j++) {
            console.log("x");
        }
        console.log("\n");
    }
}
