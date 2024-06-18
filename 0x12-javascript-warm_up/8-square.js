#!/usr/bin/node

const input = process.argv[2];
const size = Math.floor(Number(input));

if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let r = 0; r < size; r++) {
    let row = 'X'.repeat(size);
    console.log(row);
  }
}
