#!/usr/bin/node
/* access the commandline and remove the first 2 elements */
const args = process.argv.slice(2);
console.log(args[0] + ' is ' + args[1]);
