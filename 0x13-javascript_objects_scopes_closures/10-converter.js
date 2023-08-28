#!/usr/bin/node
// 10-converter.js

exports.converter = function (base) {
  return function (x) {
    return x.toString(base);
  };
};
