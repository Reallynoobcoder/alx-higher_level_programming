#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];
const characterId = 18;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode === 200) {
    const films = JSON.parse(body).results;
    let count = 0;
    films.forEach(film => {
      const characters = film.characters;
      if (characters.some(url => url.includes('/' + characterId + '/'))) {
        count++;
      }
    });
    console.log(count);
  }
});
