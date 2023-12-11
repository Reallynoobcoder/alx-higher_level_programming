#!/usr/bin/node

const size = parseInt(process.argv[2]);

if (isNaN(parseInt(size)) || !size) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    for (let j = 0; j < size; j++) {
      console.log('X');
    }
    console.log('');
  }
}
