#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request(url, (err, response, body) => {
  if (!err) {
    const todos = JSON.parse(body);
    const completedByUser = {};

    for (let i = 0; i < todos.length; i++) {
      const todo = todos[i];
      if (todo.completed) {
        const userId = todo.userId;
        if (completedByUser[userId] === undefined) {
          completedByUser[userId] = 0;
        }
        completedByUser[userId] += 1;
      }
    }

    console.log(completedByUser);
  }
});
