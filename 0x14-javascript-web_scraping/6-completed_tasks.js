#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const dict = {};
  const respBody = JSON.parse(body);
  for (const i in respBody) {
    if (respBody[i].completed === true) {
      if (dict[respBody[i].userId]) {
        dict[respBody[i].userId]++;
      } else {
        dict[respBody[i].userId] = 1;
      }
    }
  }
  console.log(dict);
});
