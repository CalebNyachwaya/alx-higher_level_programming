#!/usr/bin/node
/* access the commandline and remove the first 2 elements */
const args = process.argv.slice(2);

/* check if the first argument exists */
if (args[0] === undefined) {
  console.log('No argument');
} else if (args.length === 1) { /* check if only 1 argument exists */
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
