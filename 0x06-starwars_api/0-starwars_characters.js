#!/usr/bin/node
const argv = process.argv[2];
const urlFilm = 'https://swapi-api.alx-tools.com/api/films/';
const url = `${urlFilm}${argv}/`;

const req = require('request');
const util = require('util');
const request = util.promisify(req);

async function star (url) {
  const body = await (await request(url)).body;
  const pot = JSON.parse(body);
  const people = pot.characters;
  for (const character of people) {
    const bod = await (await request(character)).body;
    const person = JSON.parse(bod);
    console.log(person.name);
  }
}

star(url);
