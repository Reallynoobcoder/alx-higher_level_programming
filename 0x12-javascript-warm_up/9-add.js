#!/usr/bin/node

const n1 = process.argv[2];
const n2 = process.argv[3];

function add (a, b) {
  return a + b;
}

const res = add(parseInt(n1), parseInt(n2));

console.log(res);
