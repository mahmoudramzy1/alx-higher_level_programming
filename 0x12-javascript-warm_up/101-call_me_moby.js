#!/usr/bin/node
exports.callMeMoby = function(n, m) {
  for (let i = 0; i < n; i++) {
    m();
  }
};
