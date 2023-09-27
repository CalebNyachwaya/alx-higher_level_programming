#!/usr/bin/node

// Import the 'fs' module for file system operations
const fs = require('fs');

// The callback function handles errors, if any, during the write operation
fs.writeFile(process.argv[2], process.argv[3], error => {
  // Check if an error occurred during the write operation
  if (error) {
    // If there's an error, log it to the console
    console.log(error);
  }
});
