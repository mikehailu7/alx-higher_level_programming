#!/usr/bin/node
// Author: Mikias Hailu
module.exports = class Square extends require('./5-square.js') {
	charPrint (c) {
		if (c === undefined) {
			this.print();
		} else {
			for (let m = 0; m < this.height; m++) console.log(c.repeat(this.width));
		}
	}
};
