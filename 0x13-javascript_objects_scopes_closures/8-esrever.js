#!/usr/bin/node
exports.esrever = function (list) {
  const reverseList = [];
  for (const items of list) {
    reverseList.unshift(items);
  }
  return reverseList;
};
