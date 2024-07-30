#!/usr/bin/node

// Import the 'request' module for making HTTP requests
const request = require('request');

// Import the 'fs' module for file system operations
const fs = require('fs');

// Make a request to the URL specified by the first command-line argument
request(process.argv[2], function (_err, _res, body) {
  // Write the response body to the file specified by the second command-line argument
  fs.writeFile(process.argv[3], body, 'utf8', function (err) {
    // Check for an error during the file write operation
    if (err) {
      // Log the error message to the console if an error occurs
      console.log(err);
    }
  });
});
