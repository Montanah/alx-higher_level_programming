#!/usr/bin/node

const request = require('request');
const syncRequest = require('sync-request');
const url = 'https://swapi-api.alx-tools.com/api/films/';
request(url + process.argv[2] + '/.json', function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const characters = JSON.parse(body).characters;
  for (const i in characters) {
    const res = syncRequest('GET', characters[i]);
    console.log(JSON.parse(res.body).name);
  }
});
