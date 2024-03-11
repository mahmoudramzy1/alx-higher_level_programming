#!/usr/bin/node
let x = process.argv[2];
x = Number(x);
if (typeof(x) != Number){
  console.log('Not a number');
} else {
  console.log(`My number: ${x}`);
}
