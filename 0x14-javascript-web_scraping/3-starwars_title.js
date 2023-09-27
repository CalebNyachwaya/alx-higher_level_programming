#!/usr/bin/node

// Import the 'request' module for making HTTP requests
const request = require('request');

// Import the 'argv' object from the 'process' module to access command line arguments
const { argv } = require('process');

// Define the base URL for the Star Wars API
const BaseUrl = 'https://swapi-api.hbtn.io/api';

// Send an HTTP GET request to fetch information about a specific film
request(BaseUrl + '/films/' + argv[2], (error, response, body) => {
  // Handle any errors that may occur during the request
  if (error) {
    // Log the error to the console
    console.error(error);
  }

  // Parse the JSON response body and log the film title to the console
  console.log(JSON.parse(body).title);
});
