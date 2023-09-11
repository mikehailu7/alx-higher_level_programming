#!/usr/bin/node
// Author: Mikias hailu
const n = Math.floor(Number(process.argv[2]));
console.log(isNaN(n) ? 'Not a number' : `My number: ${n}`);
