#!/usr/bin/node
let i;
const args = parseInt(process.argv);
for (i = 2; i < (args.length - 1); i++) {
  const bigNum = 0;
  if (bigNum < args[i]) {
    bigNum = args[i];
  }
}
console.log(bigNum);
