#!/usr/bin/node
//Auhtor: Mikias Hailu
function add (a, b) {
	return a + b;
}
console.log(add(Number(process.argv[2]), Number(process.argv[3])));
