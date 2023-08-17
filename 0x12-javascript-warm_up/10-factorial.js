#!/usr/bin/node
// remove the first 2 arguments
const args = process.argv.slice(2);
// convert from string to int
const x = parseInt(args[0]);
// define function
function factorial (x) {
  if (isNaN(x)) {
    return 1;
  } else if (x === 1) {
    return 1;
  } else {
    return x * factorial(x - 1);
  }
}
const result = factorial(x);
console.log(result);
