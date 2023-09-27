#!/usr/bin/node

const request = require('request');
const url = 'http://swapi.co/api/films/';
let id = parseInt(process.argv[2], 10);
let characters = [];

// Send an HTTP GET request to the SWAPI films endpoint
request(url, function (err, response, body) {
  if (err == null) {
    const resp = JSON.parse(body);
    const results = resp.results;

    // Adjust the 'id' to find films within a specific range
    if (id < 4) {
      id += 3;
    } else {
      id -= 3;
    }

    // Iterate through the film results to find the one with a matching 'episode_id'
    for (let i = 0; i < results.length; i++) {
      if (results[i].episode_id === id) {
        characters = results[i].characters;
        break;
      }
    }

    // Iterate through the 'characters' array and send requests to fetch character names
    for (let j = 0; j < characters.length; j++) {
      request(characters[j], function (err, response, body) {
        if (err == null) {
          // Parse the response body and log the character's name to the console
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
