#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  }
  let total = 0;
  const respBody = JSON.parse(body).results;
  for (const i in respBody) {
    const characters = respBody[i].characters;
    for (const j in characters) {
      if (characters[j].search('18') !== -1) {
        total++;
        break;
      }
    }
  }
  console.log(total);
});
