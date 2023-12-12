#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let c = 0;
  for (let i = 0; i < list.legth; i++) {
    if (list[i] === searchElement) {
      c++;
    }
  }
  return c;
};
