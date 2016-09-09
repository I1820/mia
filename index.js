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
  var ws = new WebSocket('wss://www.example.com/socketserver')
  ws.onerror = function (event) {
    app.status.message = 'Error :('
    app.status.type = 'error'
  }
  ws.onmessage = function (event) {
    var message = event.data
    app.message.push(message)
  }
}
