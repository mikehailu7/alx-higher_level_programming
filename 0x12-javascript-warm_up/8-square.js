#!/usr/bin/node
//Author: Mikias Hailu
const m = Math.floor(Number(process.argv[2]));
if (isNaN(m)) {
	console.log('Missing size');
} else {
	for (let n = 0; n < m; n++) {
		let r = '';
		for (let d = 0; d < m; d++) r = r + 'X';
		console.log(r);
	}
}
