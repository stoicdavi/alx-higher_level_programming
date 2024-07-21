#!/usr/bin/node
const argvlen = process.argv.length - 2;

if (argvlen <= 0) {
  console.log('No argument');
} else if (argvlen === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
