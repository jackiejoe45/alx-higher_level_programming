#!/usr/bin/node
/**
 * Square class that inherits from rectangle class
 */
class Square extends require('./4-rectangle') {
  constructor (size) {
    super(size, size);
  }
}
module.exports = Square;
