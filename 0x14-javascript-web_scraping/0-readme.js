#!/usr/bin/node
const path = process.argv[2];
const fs = require('fs');
const text = fs.readFileSync(path, 'utf-8');
console.log(text);
