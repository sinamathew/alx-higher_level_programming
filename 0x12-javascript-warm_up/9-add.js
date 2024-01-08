#!/usr/bin/node
function add (a, b) {
  const args = process.argv;
  a = parseInt(args[2]);
  b = parseInt(args[3]);
  console.log(a + b);
}
add();
