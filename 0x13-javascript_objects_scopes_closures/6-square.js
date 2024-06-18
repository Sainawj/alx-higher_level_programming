#!/usr/bin/node
const Square = require('./5-square.js');
class ExtendedSquare extends Square {
  charPrint(c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        console.log(c.repeat(this.width));
      }
    }
  }
}
module.exports = ExtendedSquare;
