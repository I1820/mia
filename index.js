/*
 * +===============================================
 * | Author:        Parham Alvani (parham.alvani@gmail.com)
 * |
 * | Creation Date: 09-09-2016
 * |
 * | File Name:     index.js
 * +===============================================
 */
window.onLoad = onIndexLoad

var app = new Vue({
  el: '#app',
  data: {
    messages: [{
      id: '123',
      ip: '192.168.12.2',
      humidity: 25
    }]
  }
})

function onIndexLoad () {
  var ws = new WebSocket('ws://www.example.com/socketserver')
  ws.onmessage = function (message) {
    app.message.push(message.data)
  }
}
