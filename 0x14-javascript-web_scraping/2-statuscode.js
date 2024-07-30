#!/usr/bin/node

// Import the 'request' module for making HTTP requests
const request = require('request');

// Make a request to the URL specified by the first command-line argument
request(process.argv[2], function (_err, res) {
  // Print the response status code if a response was received
  console.log('code:', res.statusCode);
});
