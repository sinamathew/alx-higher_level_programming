#!/usr/bin/node
let i, x, myMsg;
if (parseInt(process.argv[2])) {
  x = parseInt(process.argv[2]);
  myMsg = 'C is fun';
  for (i = 0; i < x; i++) {
    console.log(myMsg);
  }
} else {
  myMsg = 'Missing number of occurrences';
  console.log(myMsg);
}
