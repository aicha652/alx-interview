#!/usr/bin/node

const process = require('process');
const arg = process.argv[2];
const request = require('request');
const options = { json: true };
const url = 'https://swapi-api.alx-tools.com/api/films/' + arg + '/';

request(url, options, async (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  for (const character of body.characters) {
    await new Promise((resolve) => {
      request(character, options, (error, response, body) => {
        if (error) {
          console.error(error);
          resolve();
        }
        console.log(body.name);
        resolve();
      });
    });
  }
});
