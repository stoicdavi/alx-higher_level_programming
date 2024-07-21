#!/usr/bin/node
const x = process.argv[2];
const intx = parseInt(x);
if (isNaN(intx)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < intx; i++) {
    console.log('C is fun');
  }
}
