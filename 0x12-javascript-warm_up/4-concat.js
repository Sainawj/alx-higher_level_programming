#!/usr/bin/node

if (process.argv.length < 4) {
  console.log('Usage: ./script_name.js <subject> <verb>');
} else {
  const subject = process.argv[2];
  const verb = process.argv[3];
  console.log(`${subject} is ${verb}`);
}
