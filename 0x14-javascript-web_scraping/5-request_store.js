#!/usr/bin/node
const request = require('request');
const fs = require('fs');
function savePage (url, filePath) {
  // Make the request
  request(url, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
      return;
    }

    // Write the body to the file
    fs.writeFile(filePath, body, 'utf8', err => {
      if (err) {
        console.error(err);
      }
    });
  });
}

// Get the URL and file path from the command line arguments
const url = process.argv[2];
const filePath = process.argv[3];

// Save the page
savePage(url, filePath);
