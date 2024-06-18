#!/usr/bin/node

const input = process.argv[2];
const num = Math.floor(Number(input));

if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${num}`);
}
