#!/usr/bin/node

module.exports = class Rectangle {
    constructor (w = 0, h = 0) {
        if (typeof w !== 'number' || typeof h !== 'number' || w <= 0 || h <= 0) {
            throw new Error('Invalid dimensions. Width and height must be positive numbers.');
        }
        this.width = w;
        this.height = h;
    }
}

