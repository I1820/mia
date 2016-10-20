/*
 * +===============================================
 * | Author:        Parham Alvani (parham.alvani@gmail.com)
 * | Author:        Iman Tabrizian (tabrizian@outlook.com)
 * |
 * | Creation Date: 09-09-2016
 * |
 * | File Name:     index.js
 * +===============================================
 */

/* global Vue : Vue.js */
/* global $   : JQuery */
/* global Plotly   : Plotly.js */

var app = new Vue({
  el: '#app',
  data: {
    rpis: {},
    endpoint: '',
    states: {},
    things: []
  },
  created: function () {
    this.refresh()
    $('time.timeago').timeago()
  },
  updated: function () {
    $('time.timeago').timeago()
  },
  watch: {
    endpoint: function () {
      if (typeof this.endpoint === 'string') {
        this.things = this.rpis[this.endpoint]['things']
      }
    }
  },
  methods: {
    refresh: function () {
      $.get('discovery', function (data, status) {
        app.rpis = JSON.parse(data)
      })
    },
    drawCurrent: function (value) {
      var degrees = 180 - value
      var radius = 0.5
      var radians = degrees * Math.PI / 180
      var x = radius * Math.cos(radians)
      var y = radius * Math.sin(radians)

      var mainPath = 'M -.0 -0.025 L .0 0.025 L ',
      pathX = String(x),
      space = ' ',
      pathY = String(y),
      pathEnd = ' Z';
      var path = mainPath.concat(pathX,space,pathY,pathEnd);

      var layout = {
        shapes:[{
          type: 'path',
          path: path,
          fillcolor: '850000',
          line: {
            color: '850000'
          }
        }],
        title: 'Current Gauge',
        height: 300,
        width: 300,
        xaxis: {zeroline:false, showticklabels:false,
          showgrid: false, range: [-1, 1]},
          yaxis: {zeroline:false, showticklabels:false,
            showgrid: false, range: [-1, 1]}
      };


      var data = [
        {
        type: 'scatter',
        x: [0],
        y: [0],
        marker: {size: 28, color: '850000'},
        showlegend: false,
        name: 'A',
        text: value,
        hoverinfo: 'text+name'
      }, {
        values: [50 / 6, 50 / 6, 50 / 6, 50 / 6, 50 / 6, 50 / 6, 50],
        rotation: 90,
        text: ['TOO FAST!', 'Pretty Fast', 'Fast', 'Average', 'Slow', 'Super Slow', ''],
        textinfo: 'text',
        textposition: 'inside',
        marker: {colors: ['rgba(14, 127, 0, .5)', 'rgba(110, 154, 22, .5)',
          'rgba(170, 202, 42, .5)', 'rgba(202, 209, 95, .5)',
          'rgba(210, 206, 145, .5)', 'rgba(232, 226, 202, .5)',
          'rgba(255, 255, 255, 0)']},
          labels: ['151-180', '121-150', '91-120', '61-90', '31-60', '0-30', ''],
          hoverinfo: 'label',
          hole: 0.5,
          type: 'pie',
          showlegend: false
      }
      ]
      Plotly.newPlot('current', data, layout)
    },
    fetch: function (type, data, deviceId) {
      var payload = {
        type: type,
        rpi_id: this.endpoint,
        device_id: deviceId,
        states: data
      }
      $.post('thing', JSON.stringify(payload), function (data, status) {
        var message = JSON.parse(data)
        for (var key in message) {
          if (message.hasOwnProperty(key)) {
            message[key].time = new Date(message[key].time).toLocaleString()
            Vue.set(app.states, key, message[key])
          }
        }
      })
    },
    turn: function (command, deviceId) {
      var payload = {
        type: 'lamp',
        rpi_id: this.endpoint,
        device_id: deviceId,
        settings: {
          on: command
        }
      }
      $.ajax({
        url: 'thing',
        type: 'PUT',
        contentType: 'application/json',
        data: JSON.stringify(payload)
      })
    }
  }
})

// Trig to calc meter point
// Path: may have to change to create a better triangle
$('document').ready(function () {
})
