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
    connection: {
      message: 'Connecting...',
      state: 'default'
    },
    states: {
    },
    rpi_ids: [],
    lamp_id: 1
  },
  methods: {
    on: function(event) {
	console.log("Hello")
	request = {
	    type: "PUT",
	    url: "http://iot.ceit.aut.ac.ir:58902/thing",
	    contentType: "application/json",
	    data : {
        	"type": "lamp",
        	"rpi_id": "066156d8-df62-5894-809b-d51ec5a2ff3d",
        	"device_id": "1:" + this.lamp_id,
        	"settings": {
            	  "on": true
        	}
    	   }
	};
	console.log(request);
	$.ajax({
	    type: "PUT",
	    url: "http://iot.ceit.aut.ac.ir:58902/thing",
	    contentType: "application/json",
	    data : {
        	type: "lamp",
        	rpi_id: "066156d8-df62-5894-809b-d51ec5a2ff3d",
        	device_id: "1:" + this.lamp_id,
        	settings: {
            	  on: true
        	}
    	   }
	});
      
    },
    checkData: function() {
	return Object.keys(this.states).length;
    }
  }
})

function onIndexLoad () {
  var socket = io.connect('http://iot.ceit.aut.ac.ir:58902/');
  socket.on('connect', function () {
    app.connection.message = 'Connected';
    app.connection.state = 'success';
  })
  socket.on('error', function () {
    app.connection.message = 'Error :(';
    app.connection.state = 'danger';
  })
  socket.on('log', function (message) {
    message = JSON.parse(message);
    for (var key in message.states) {
      if (message.states.hasOwnProperty(key)) {
        Vue.set(app.states, key, message.states[key]);
      }
    }
  })
}
