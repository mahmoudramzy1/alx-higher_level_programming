#!/usr/bin/node
let x = process.argv[2];
x = Number(x);
if (typeof x !== 'number') {
  console.log('Not a number');
} else {
  console.log(`My number: ${x}`);
}
