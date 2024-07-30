#!/usr/bin/node

// Import the 'request' module for making HTTP requests
const request = require('request');

// Function to get data from a URL and return a Promise
function getDataFrom(url) {
  return new Promise(function (resolve, reject) {
    // Make a request to the URL
    request(url, function (err, _res, body) {
      if (err) {
        // Reject the promise if there is an error
        reject(err);
      } else {
        // Resolve the promise with the response body
        resolve(body);
      }
    });
  });
}

// Error handler function to log errors
function errHandler(err) {
  console.log(err);
}

// Function to print movie characters given a movie ID
function printMovieCharacters(movieId) {
  // Construct the movie URL using the movie ID
  const movieUri = `https://swapi-api.hbtn.io/api/films/${movieId}`;

  // Get data from the movie URL
  getDataFrom(movieUri)
    // Parse the response body as JSON
	.then(JSON.parse, errHandler)
    .then(function (res) {
      // Extract the characters array from the response
      const characters = res.characters;
      const promises = [];

      // Loop through each character URL and get data
      for (let i = 0; i < characters.length; ++i) {
        promises.push(getDataFrom(characters[i]));
      }

      // Wait for all character data requests to complete
      Promise.all(promises)
        .then((results) => {
          // Loop through each result and print
		// the character's name
          for (let i = 0; i < results.length; ++i) {
            console.log(JSON.parse(results[i]).name);
          }
        })
        .catch((err) => {
          // Log any errors that occur during the character data requests
          console.log(err);
        });
    });
}

// Call the function to print movie characters using the
// movie ID passed as a command-line argument
printMovieCharacters(process.argv[2]);
