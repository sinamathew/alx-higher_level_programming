#!/usr/bin/node
// A script that counts the number of Star Wars characters with ID 18
// in a movie based on its episode number.

const request = require('request');
const url = process.argv[2]; // Episode number URL
const characterURL = 'https://swapi-api.alx-tools.com/api/people/18/'; // Character with ID 18

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const jsonData = JSON.parse(body);

    let characterCount = 0; // Initialize character count

    // Check if request was successful and data exists
    if (jsonData && jsonData.results) {
      for (const result of jsonData.results) {
        if (result.characters.includes(characterURL)) {
          characterCount++;
        }
      }
      console.log(characterCount);
    }
  }
});
