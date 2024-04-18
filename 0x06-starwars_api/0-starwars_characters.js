#!/usr/bin/node

const process = require('process');
const arg = process.argv[2];
const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/' + arg + '/';

request.get(url, async (error, response, body) => {
  if (error) console.log(error);
  const data = await JSON.parse(body);
  for (const character of data.characters) {
    request.get(character, async (error, response, body) => {
      if (error) console.log(error);
      const characterData = await JSON.parse(body);
      console.log(characterData.name);
    });
  }
});