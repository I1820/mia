var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http);
var bodyParser = require('body-parser');


app.use(bodyParser.text());

app.get('/', function(req, res){
    res.sendFile(__dirname + '/index.html');
});



var lastSocket;
app.post('/api', function (req, res) {
    console.log("Post request to /api");
    io.emit('chat message', req.body);
    console.log("Post request to /api");
    res.send('Success');
});


io.on('connection', function(socket){
    console.log('a user connected');
    lastSocket = socket;
    socket.on('chat message', function(msg){
        console.log(msg);
    });

});



http.listen(3000, function(){
    console.log('listening on *:3000');
});