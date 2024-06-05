#!/usr/bin/node
/**
 * This script prints the star wars characters
 * in the same order as the characters list in the /
 *films/endpoint
 */

const request = require('request');
const movieURL = 'https://swapi-api.hbtn.io/api/films/';
const movieId = `${process.argv[2]}/`;

request(`${movieURL}${movieId}`, async function (error, response, body) {
  if (error) {
    return console.error(error);
  }

  const characterURLs = JSON.parse(body).characters;

  for (const characterURL of characterURLs) {
    await new Promise(function (resolve, reject) {
      request(characterURL, function (error, response, body) {
        if (error) {
          return console.error(error);
        }

        const character = JSON.parse(body).name;
        console.log(character);
        resolve();
      });
    });
  }
});
