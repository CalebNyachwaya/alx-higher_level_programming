#!/usr/bin/node
// 9-logme.js

let line = 0;
exports.logMe = function (item) {
  console.log(line + ': ' + item);
  line++;
  return (line);
};
