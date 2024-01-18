#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(url, function (err, response, body) {
  if (err === null) {
    const film = JSON.parse(body);
    const characters = film.characters;
    for (const charac of characters) {
      request(charac, function (err, response, body) {
        if (err === null) {
          const people = JSON.parse(body);
          console.log(people.name);
        }
      });
    }
  }
});
