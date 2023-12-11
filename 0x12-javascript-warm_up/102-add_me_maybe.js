#!/usr/bin/node

function addMeMaybe (n, theFunction) {
  theFunction(++n);
}
exports.addMeMaybe = addMeMaybe;
