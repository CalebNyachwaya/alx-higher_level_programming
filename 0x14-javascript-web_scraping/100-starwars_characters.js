#!/usr/bin/node

const request = require('request');
const { argv } = require('process');

const BaseUrl = 'https://swapi-api.hbtn.io/api/films/';

// Define a function 'MakeRequest' that returns a promise for making HTTP requests
function MakeRequest (url) {
  return new Promise(function (resolve, reject) {
    request(url, (error, response, body) => {
      // If the request is successful (status code 200), resolve the promise with the response body
      if (!error && response.statusCode === 200) {
        resolve(body);
      } else {
        // If there's an error or a non-200 status code, reject the promise with an error
        reject(error);
      }
    });
  });
}

// Define an asynchronous function 'main' to fetch movie characters and display their names
async function main () {
  // Fetch information about the specified movie
  const movie = await MakeRequest(BaseUrl + argv[2]);
  // Extract the 'characters' array from the movie data
  const characters = JSON.parse(movie).characters;

  // Iterate through each character and fetch and display their names asynchronously
  characters.forEach(async function (element) {
    // Fetch information about the character
    const character = await MakeRequest(element);
    // Extract and log the character's name
    const CharacterName = JSON.parse(character).name;
    console.log(CharacterName);
  });
}

// Call the 'main' function to start the asynchronous operations
main();
