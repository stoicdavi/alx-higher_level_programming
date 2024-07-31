#!/usr/bin/node

const request = require('request');

const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + id;

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const characters = JSON.parse(body).characters;
    for (const chars in characters) {
      request(characters[chars], (error, response, body) => (error)
        ? console.log(error)
        : console.log(JSON.parse(body).name));
    }
  } else {
    console.log('Error code:' + response.statusCode);
  }
});
