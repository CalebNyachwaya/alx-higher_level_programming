#!/usr/bin/node
// 100-map.js

const list = require('./100-data.js').list;
console.log(list);
console.log(list.map((item, index) => item * index));
