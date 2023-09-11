#!/usr/bin/node
// Author: Mikias Hailu
exports.nbOccurences = function (list, searchElement) {
	return list.reduce((count, current) => current === searchElement ? count + 1 : count, 0);
};
