#!/usr/bin/node
const size = process.argv[2];
const intSize = parseInt(size);
if (isNaN(intSize)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < intSize; i++) {
    let line = '';
    for (let j = 0; j < intSize; j++) {
      line += 'X';
    }
    console.log(line);
  }
}
