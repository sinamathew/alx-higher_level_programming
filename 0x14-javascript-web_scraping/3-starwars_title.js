#!/usr/bin/node
// A script that prints the title of a Star Wars movie using episode number.

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';
const _id = process.argv[2];

request(url + _id, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const jsonData = JSON.parse(body);
    console.log(jsonData.title);
  }
});
