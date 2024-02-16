#!/usr/bin/node
const arg = process.argv[2];
const urlFilm = 'https://swapi-api.alx-tools.com/api/films/';
const url = `${urlFilm}${argv}/`;


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
    request(url, function (err, res, bod) {
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
