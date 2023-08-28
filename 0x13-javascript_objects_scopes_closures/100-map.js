#!/usr/bin/node

/**
 * 100-map.js
 * imports an array and computes a new array
 */
const initList = require('./100-data.js').list;
const newList = initList.map((number, index) => number * index);

console.log(initList);
console.log(newList);
