#!/usr/bin/node
const args = process.argv.slice(2);

if (args.length <= 1) {
  console.log(0);
} else {
  const numbers = args.map(Number); // Convert arguments to integers
  numbers.sort((a, b) => b - a); // Sort the integers in descending order
  console.log(numbers[1]); // Print the second largest integer
}
