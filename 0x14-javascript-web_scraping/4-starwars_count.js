#!/usr/bin/node

// Import the 'request' module for making HTTP requests
const request = require('request');

// The Star Wars API URL is passed as a command-line argument
const starWarsUri = process.argv[2];
let times = 0;

// Make a request to the Star Wars API
request(starWarsUri, function (_err, _res, body) {
  // Parse the response body as JSON and get the results array
  body = JSON.parse(body).results;

  // Loop through each film in the results array
  for (let i = 0; i < body.length; ++i) {
    const characters = body[i].characters;

    // Loop through each character URL in the film
    for (let j = 0; j < characters.length; ++j) {
      const character = characters[j];
      const characterId = character.split('/')[5];

      // Increment the count if the character ID is '18'
      if (characterId === '18') {
        times += 1;
      }
    }
  }

  // Print the total count of characters with ID '18'
  console.log(times);
});
