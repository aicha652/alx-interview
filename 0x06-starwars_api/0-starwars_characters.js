#!/usr/bin/node
const request = require('request');

const filmId = process.argv[2];

function getCharacter (url) {
  return new Promise((resolve, reject) => {
    request(url, { json: true }, (err, res, body) => {
      if (err) {
        reject(err);
        return;
      }
      resolve(body);
    });
  });
}

request(`https://swapi-api.alx-tools.com/api/films/${filmId}/`, { json: true }, (err, res, film) => {
  if (err) {
    return;
  }
  const promises = [];

  film.characters.forEach((url) => {
    promises.push(getCharacter(url));
  });

  Promise.all(promises).then((character) => {
    character.forEach((character) => {
      console.log(character.name);
    });
  });
});
