#!/usr/bin/node

const request = require('request');

const url = 'http://swapi.co/api/films/';

request(url + process.argv[2], function(err, response, body) {
  if (err) {
   console.log(err);
   return;
  } else {
  console.log(JSON.parse(body).title);
  }
});
