#!/usr/bin/node
//Author: Mikias Hailu
function factorial (n) {
  return m === 0 || isNaN(m) ? 1 : m * factorial(m - 1);
}
console.log(factorial(Number(process.argv[2])));
