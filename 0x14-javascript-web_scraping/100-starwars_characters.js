#!/usr/bin/node

// Import the 'request' module for making HTTP requests
const request = require('request');

// Construct the Star Wars API URL with the film ID from the command-line argument
const starWarsUri = 'https://swapi-api.hbtn.io/api/films/'.concat(process.argv[2]);

// Make a request to the constructed Star Wars API URL
request(starWarsUri, function (_err, _res, body) {
  // Parse the response body as JSON and extract the characters array
  const characters = JSON.parse(body).characters;

  // Loop through each character URL in the characters array
  for (let i = 0; i < characters.length; ++i) {
    // Make a request to the character URL
    request(characters[i], function (_cErr, _cRes, cBody) {
      // Parse the character response body as JSON and print the character's name
      console.log(JSON.parse(cBody).name);
    });
  }
});
