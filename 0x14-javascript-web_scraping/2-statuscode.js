#!/usr/bin/node

// Import the 'request' module for making HTTP requests
const request = require('request');

// Use the 'request.get' method to send an HTTP GET request to the URL provided as a command line argument
request.get(process.argv[2]).on('response', function (response) {
  // When a response is received, this callback function is executed
  // Log the status code of the HTTP response to the console
  console.log(`code: ${response.statusCode}`);
});
