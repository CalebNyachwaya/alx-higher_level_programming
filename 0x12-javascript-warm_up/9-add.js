#!/usr/bin/node
// remove the first 2 arguments
const args = process.argv.slice(2);
// convert string to integer
const a = parseInt(args[0]);
const b = parseInt(args[1]);
// define function
function add (a, b) {
  return a + b;
}
const result = add(a, b);
console.log(result);
