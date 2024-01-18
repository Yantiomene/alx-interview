#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

function getName (characterList, i) {
  if (i === characterList.length) {
    return;
  }
  request(characterList[i], function (err, response, body) {
    if (err === null) {
      const people = JSON.parse(body);
      console.log(people.name);
      getName(characterList, i + 1);
    }
  });
}

request(url, function (err, response, body) {
  if (err === null) {
    const film = JSON.parse(body);
    const characters = film.characters;

    getName(characters, 0);
  }
});
