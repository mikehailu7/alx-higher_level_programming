#!/usr/bin/node
// Author: Mikias Hailu
let cont = 0;
exports.logMe = function (item) { console.log(`${cont++}: ${item}`); };
