#!/usr/bin/node

// Import the 'request' module for making HTTP requests
const request = require('request');

// Make a request to the URL specified by the first command-line argument
request(process.argv[2], function (err, _res, body) {
  if (err) {
    // Log the error message if an error occurs
    console.log(err);
  } else {
    // Initialize an object to store the count of completed tasks by user ID
    const completedTasksByUsers = {};

    // Parse the response body as JSON
    body = JSON.parse(body);

    // Loop through each task in the response body
    for (let i = 0; i < body.length; ++i) {
      const userId = body[i].userId;
      const completed = body[i].completed;

      // Initialize the count for the user ID if not already done
      if (completed && !completedTasksByUsers[userId]) {
        completedTasksByUsers[userId] = 0;
      }

      // Increment the count for the user ID if the task is completed
      if (completed) {
        ++completedTasksByUsers[userId];
      }
    }

    // Print the completed tasks by user ID
    console.log(completedTasksByUsers);
  }
});
