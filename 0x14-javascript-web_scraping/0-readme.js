#!/usr/bin/node

// Import the 'fs' module, which provides an API for interacting with the file system.
const fs = require('fs');

// Read the file specified as the first command-line argument (process.argv[2])
// using 'utf8' encoding.
fs.readFile(process.argv[2], 'utf8', function (err, data) {
  // Check for an error during the file read operation.
  if (err) {
    // If there is an error, log the error message to the console.
    console.log(err);
  } else {
    // If no error, write the content of the file to the standard output.
    process.stdout.write(data);
  }
});
