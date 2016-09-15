/*
 * +===============================================
 * | Author:        Parham Alvani (parham.alvani@gmail.com)
 * |
 * | Creation Date: 09-09-2016
 * |
 * | File Name:     index.js
 * +===============================================
 */
window.onload = onIndexLoad

var app = new Vue({
  el: '#app',
  data: {
    status: {
      message: 'Connecting...',
      type: 'default'
    },
    messages: [{
      id: '123',
      ip: '192.168.12.2',
      humidity: 25
    }]
  }
})

function onIndexLoad () {
  var socket = io.connect('ws://192.168.1.9:1373/temperature')
  socket.on('connect', function () {
    app.status.message = 'Connected'
    app.status.type = 'success'
  })
  socket.on('error', function () {
    app.status.message = 'Error :('
    app.status.type = 'danger'
  })
  socket.on('message', function (message) {
    console.log(message)
  })
}
