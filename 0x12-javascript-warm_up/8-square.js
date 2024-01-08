#!/usr/bin/node
let i, x, sqrt;
if (parseInt(process.argv[2])) {
  x = parseInt(process.argv[2]);
  sqrt = 'X';
  for (i = 0; i < x; i++) {
    console.log(sqrt.repeat(x));
  }
} else {
  sqrt = 'Missing size';
  console.log(sqrt);
}
