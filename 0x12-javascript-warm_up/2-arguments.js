#!/usr/bin/node
let x = process.argv[2];
let y = process.argv[3];
if (x === undefined)
	console.log('No argument');
else
	if (y === undefined)
		console.log('Argument found');
	else
		console.log('Arguments found');
