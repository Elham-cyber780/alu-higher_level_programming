#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request(url, (err, response, body) => {
  if (!err) {
    const films = JSON.parse(body).results;
    let count = 0;

    for (let i = 0; i < films.length; i++) {
      const characters = films[i].characters;
      for (let j = 0; j < characters.length; j++) {
        if (characters[j].endsWith('/people/18/')) {
          count += 1;
        }
      }
    }

    console.log(count);
  }
});
