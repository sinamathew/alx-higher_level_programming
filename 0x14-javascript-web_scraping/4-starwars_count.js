#!/usr/bin/node
// A script that prints the title of a Star Wars movie using episode number.

const request = require('request');
const url = process.argv[2];
const people = "https://swapi-api.alx-tools.com/api/people/"

request(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const jsonData = JSON.parse(body);
  }
  let lostChars = 0;
  for (let i = 0; i < jsonData.results.length; i++) {
    for (let j = 0; j < jsonData.results.characters.length; j++) {
      if (jsonData.results.characters === people + "18/") {
        lostChars++;
      }}};
  console.log(lostChars);
};
