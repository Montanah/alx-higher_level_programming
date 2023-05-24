#!/usr/bin/node

const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/';

function getCharacterName(characterUrl) {
  return new Promise((resolve, reject) => {
    request(characterUrl, function (error, response, body) {
      if (error) {
        reject(error);
      } else {
        const character = JSON.parse(body);
        resolve(character.name);
      }
    });
  });
}

async function getFilmCharacters(filmId) {
  try {
    const filmUrl = url + filmId + '/.json';
    const filmResponse = await new Promise((resolve, reject) => {
      request(filmUrl, function (error, response, body) {
        if (error) {
          reject(error);
        } else {
          resolve(body);
        }
      });
    });
    const characters = JSON.parse(filmResponse).characters;

    for (const characterUrl of characters) {
      const characterName = await getCharacterName(characterUrl);
      console.log(characterName);
    }
  } catch (error) {
    console.log(error);
  }
}

const filmId = process.argv[2];
getFilmCharacters(filmId);

