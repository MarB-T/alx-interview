#!/usr/bin/node

const request = require('request');
const arg = process.argv[2];

async function retPro (url) {
  return new Promise(function (resolve, reject) {
    request(url, function (err, res, body) {
      resolve(JSON.parse(body).name);
      if (err) throw err;
    });
  });
}

async function chars () {
  return new Promise(function (resolve, reject) {
    request(`https://swapi-api.alx-tools.com/api/films/${arg}`, function (err, res, bod) {
      resolve(JSON.parse(bod).characters);
      if (err) throw err;
    });
  });
}

async function names () {
  const thischars = await chars();
  for (let i = 0; i < thischars.length; i++) {
    console.log(await retPro(thischars[i]));
  }
}

names();
