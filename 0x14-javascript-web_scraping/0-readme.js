#!/usr/bin/node
// A script that reads and prints the content of a file

const fs = require('fs');
fs.readFile(path, 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
