#!/usr/bin/node

let max = parseInt(process.argv[2]);
let second = parseInt(process.argv[3]);

if (process.argv.length <= 3) {
  console.log(0);
} else {
  for (let i = 4; i < process.argv.length; i++) {
    const current = parseInt(process.argv[i]);
    if (!isNaN(current)) {
      if (current > max) {
        second = max;
        max = current;
      } else if (current > second) {
        second = current;
      }
    }
  }
  console.log(second);
}
