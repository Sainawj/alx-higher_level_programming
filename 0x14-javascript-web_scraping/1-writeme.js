#!/usr/bin/node

// Import the 'fs' module for file system operations
const fs = require('fs');

// Write to the file specified by the first command-line argument
// with the content specified by the second command-line argument
fs.writeFile(process.argv[2], process.argv[3], 'utf8', function (err) {
  // Check for an error during the file write operation
  if (err) {
    // Log the error message to the console if an error occurs
    console.log(err);
  }
});
