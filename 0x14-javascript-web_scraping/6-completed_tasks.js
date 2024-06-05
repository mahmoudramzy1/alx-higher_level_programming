#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
let mydict = {}
let count = 0
let id = null;

request(url, (err, res, body) => {
  if (err) {
    console.log(err);
  }
  list = JSON.parse(body)
  for (let i in list) {
    const item = list[i];
    if (id !== null && id !== item.userId) {
      mydict[id] = count;
      count = 0;
    }
    id = item.userId 
    if (item.completed === true)
      count++;
  }
  if (id !== null) {
    mydict[id] = count;
  }
  console.log(mydict);
});
