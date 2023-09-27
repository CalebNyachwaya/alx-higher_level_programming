#!/usr/bin/node

const request = require('request');

// Send an HTTP GET request to the URL provided as a command line argument
request(process.argv[2], function (error, response, body) {
  // Check if there is no error in the request
  if (!error) {
    // Parse the JSON response body into an array of 'todos'
    const todos = JSON.parse(body);

    // Initialize an object to store the count of completed todos for each user
    const completed = {};

    // Iterate through each 'todo' and count completed todos per user
    todos.forEach((todo) => {
      if (todo.completed && completed[todo.userId] === undefined) {
        completed[todo.userId] = 1;
      } else if (todo.completed) {
        completed[todo.userId] += 1;
      }
    });

    // Log the 'completed' object containing the counts per user to the console
    console.log(completed);
  }
});
