#!/usr/bin/node
/* access the commandline and remove the first 2 elements */
const args = process.argv.slice(2);

if (args[0] !== undefined) {
  console.log(args[0]);
} else {
  console.log('No argument');
}
