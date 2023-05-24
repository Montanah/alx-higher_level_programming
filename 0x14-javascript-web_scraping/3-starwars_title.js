#!/usr/bin/node

const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/';

request(url + process.argv[2], function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});
