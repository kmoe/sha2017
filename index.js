//server
//receives HTTP

//calls libfreefare to write to hand

const express = require('express');

const app = express();

app.get('/', function (req, res) {
  res.send('Hello World!');
});

// okay so maybe when you get the index route it is some picture or something

// maybe there is another badge app that displays the current state

// like /r/place

// so need a simple data format. maybe grid. literally binary lololo

app.post('/posts', (req, res) => {
  console.log('received', res.body);

  // put it on the chip
});

app.listen(3000, function () {
  console.log('Example app listening on port 3000!');
});