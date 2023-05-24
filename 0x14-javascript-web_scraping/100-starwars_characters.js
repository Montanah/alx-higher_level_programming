#!/usr/bin/node

const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/';

request(url + process.argv[2] + '/.json', function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const characters = JSON.parse(body).characters;
  for (const i in characters) {
    request(characters[i], function (err, resp, bod) {
      if (err) {
        console.log(err);
      }
      console.log(JSON.parse(bod).name);
    });
  }
});
