#!/usr/bin/node

// Import the 'request' module for making HTTP requests
const request = require('request');

// Construct the Star Wars API URI with the film ID from the command-line argument
const starWarsUri = 'https://swapi-api.hbtn.io/api/films/'.concat(process.argv[2]);

// Make a request to the constructed URI
request(starWarsUri, function (_err, _res, body) {
  // Parse the response body as JSON
  body = JSON.parse(body);
  // Print the title of the Star Wars film
  console.log(body.title);
});
