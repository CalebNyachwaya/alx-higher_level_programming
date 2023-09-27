#!/usr/bin/node

const request = require('request');

// Send an HTTP GET request to the URL provided as a command line argument
request(process.argv[2], function (error, response, body) {
  // Check if there is no error in the request
  if (!error) {
    // Parse the JSON response body and access the 'results' array
    const results = JSON.parse(body).results;

    // Count movies with a character ending with '/18/' in their 'characters' array
    const count = results.reduce((count, movie) => {
      // Check if there is a character with an ID ending with '/18/' in the 'characters' array
      return movie.characters.find((character) => character.endsWith('/18/'))
        ? count + 1 // Increment the count if found
        : count; // Keep the count unchanged if not found
    }, 0);

    // Log the count of movies with a specific character to the console
    console.log(count);
  }
});
