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

$('document').ready(function () {
})
