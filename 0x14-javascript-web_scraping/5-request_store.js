#!/usr/bin/node

const fs = require('fs');
const request = require('request');

// Send an HTTP GET request to the URL provided as the first command line argument
// Pipe the response data directly to a file specified as the second command line argument
request(process.argv[2]).pipe(fs.createWriteStream(process.argv[3]));
