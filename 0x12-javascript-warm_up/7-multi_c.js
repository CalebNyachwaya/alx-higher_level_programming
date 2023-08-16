#!/usr/bin/node
/* access the commandline and remove the first 2 elements */
const args = process.argv.slice(2);
// convert string to value
const x = parseInt(args[0]);
let i = 0;
if (!isNaN(x)) {
  for (i = 0; i < x; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
