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
      message: 'connecting',
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
  ws.onerror = function (error) {
    app.status.message = error
    app.status.type = 'error'
  }
  ws.onmessage = function (message) {
    app.message.push(message.data)
  }
}
