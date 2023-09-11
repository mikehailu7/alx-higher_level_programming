#!/usr/bin/node
//Auhtor: Mikias Hailu
module.exports = class Rectangle {
	constructor (w, h) {
		if (w > 0 && h > 0) { [this.width, this.height] = [w, h]; }
	}
	print () {
		for (let m = 0; m < this.height; m++) console.log('X'.repeat(this.width));
	}
};
