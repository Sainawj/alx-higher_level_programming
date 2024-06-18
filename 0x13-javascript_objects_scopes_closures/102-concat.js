#!/usr/bin/node

const fs = require('fs');
const util = require('util');
const readFile = util.promisify(fs.readFile);
const writeFile = util.promisify(fs.writeFile);

async function concatenateFiles(file1, file2, outputFile) {
  try {
    const content1 = await readFile(file1, 'utf8');
    const content2 = await readFile(file2, 'utf8');
    await writeFile(outputFile, content1 + content2);
    console.log(`Successfully concatenated ${file1} and ${file2} into ${outputFile}`);
  } catch (err) {
    console.error(`Error concatenating files: ${err.message}`);
  }
}

const [, , file1, file2, outputFile] = process.argv;

if (file1 && file2 && outputFile) {
  concatenateFiles(file1, file2, outputFile);
} else {
  console.error('Usage: node script.js <file1> <file2> <outputFile>');
}
