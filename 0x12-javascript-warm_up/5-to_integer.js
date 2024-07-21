#!/usr/bin/node
const farg = process.argv[2];
const fint = parseInt(farg);
console.log(isNaN(fint) ? 'Not a number' : `My number: ${fint}`);
