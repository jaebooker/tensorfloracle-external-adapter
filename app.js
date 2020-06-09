const createRequest = require('./index').createRequest
var request = new XMLHttpRequest()
const express = require('express')
const bodyParser = require('body-parser')
const app = express()
const port = process.env.EA_PORT || 8080

app.use(bodyParser.json())

var spawn = require('child_process').spawn,
  py    = spawn('python', ['keras.py']),
  data = [1,2,3,4,5,6,7,8,9],
  dataString = '';

py.stdout.on('data', function(data){
    dataString += data.toString();
  });
py.stdout.on('end', function(){
    console.log('Sum of numbers=',dataString);
  });
py.stdin.write(JSON.stringify(data));
py.stdin.end();

app.post('/', (req, res) => {
  // Open a new connection, using the GET request on the URL endpoint
  request.open('GET', 'https://ipfs.infura.io:5001/api/v0/object/stat?arg=hash', true)
  request.onload = function() {
    // Begin accessing JSON data here
    var data = JSON.parse(this.response)

    data.forEach(model => {
      console.log(model)
    })
  }
  // Send request
  request.send()
  console.log('POST Data: ', req.body)
  createRequest(req.body, (status, result) => {
    console.log('Result: ', result)
    res.status(status).json(result)
  })
})

app.listen(port, () => console.log(`Listening on port ${port}!`))
