#!/usr/bin/node
// Author: Mikias Hailu
exports.esrever = function (list) {
	return list.reduceRight(function (array, current) {
		array.push(current);
		return array;
	}, []);
};
