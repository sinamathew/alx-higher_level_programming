#!/usr/bin/node
const noMsg = 'undefined';
const args = process.argv;
if (args[3]) {
  console.log(args[2] + ' is ' + args[3]);
} else if (args[2]) {
  console.log(args[2] + ' is ' + noMsg);
} else {
  console.log(noMsg + ' is ' + noMsg);
}
