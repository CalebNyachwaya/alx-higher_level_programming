#!/usr/bin/node
// remove the first 2 arguments
const args = process.argv.slice(2);
// convert string to integer
const x = parseInt(args[0]);
let i = 0;
let j = 0;
if (!isNaN(x)) {
  for (i = 0; i < x; i++) {
    let line = '';
    for (j = 0; j < x; j++) {
      line += 'X';
    }
    console.log(line);
  }
} else {
  console.log('Missing size');
}
