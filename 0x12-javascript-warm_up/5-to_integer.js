#!/usr/bin/node
/* access the commandline and remove the first 2 elements */
const args = process.argv.slice(2);
// convert string to value
const value = parseInt(args[0]);
if (isNaN(value)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + value);
}
