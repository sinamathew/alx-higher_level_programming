#!/usr/bin/node
// A script that display the status code of a GET request.

const request = require('request');
const url = process.argv[2];

request(url, (err, response) => {
  if (err) {
    console.error(err);
  }
  console.log('Code:', response && response.statusCode);
});
