#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let occurence = 0;
  for (const whatever in list) {
    if (whatever === searchElement) {
      occurence += 1;
    }
  }
  return occurence;
};
