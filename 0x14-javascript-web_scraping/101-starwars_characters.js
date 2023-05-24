#!/usr/bin/node

const request = require('request-promise');

const url = 'https://swapi-api.alx-tools.com/api/films/';

async function getFilmCharacters (filmId) {
  try {
    const response = await request(url + filmId + '/.json');
    const characters = JSON.parse(response).characters;

    for (const characterUrl of characters) {
      const characterResponse = await request(characterUrl);
      const character = JSON.parse(characterResponse);
      console.log(character.name);
    }
  } catch (error) {
    console.log(error);
  }
}

const filmId = process.argv[2];
getFilmCharacters(filmId);
