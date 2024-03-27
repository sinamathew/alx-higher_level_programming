#!/usr/bin/node
// Short script to count completed tasks per user (filtering users with none)

const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) console.error('Error:', error);
  else {
    const completedTasks = JSON.parse(body)
      .filter(task => task.completed) // Filter completed tasks
      .reduce((acc, task) => {
        acc[task.userId] = (acc[task.userId] || 0) + 1; // Count tasks by userId
        return acc;
      }, {}); // Initialize accumulator as empty object

    console.log(Object.entries(completedTasks).filter(([id, count]) => count > 0)); // Filter users with no completed tasks
  }
});
