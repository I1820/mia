'use strict';

/**
 * @ngdoc service
 * @name i1820UiApp.ThingService
 * @description
 * # thingService
 * Service in the i1820UiApp.
 */
angular.module('i1820UiApp')
  .service('ThingService', function ($http) {
    // AngularJS will instantiate a singleton by calling "new" on this function

    this.getState = function (agentId, thingId, type, states) {
      var msg = {
        'agent_id': agentId,
        'device_id': thingId,
        'type': type,
        'states': states
      };
      return $http.post('/thing', msg).then(function (response) {
        if (typeof response.data === 'object') {
          return response.data;
        }
      });
    };

    this.setSetting = function (agentId, thingId, type, setting, value) {
      var msg = {
        'agent_id': agentId,
        'device_id': thingId,
        'type': type,
        'settings': {}
      };
      msg.settings[setting] = value;
      return $http.put('/thing', msg).then(function (response) {
        if (typeof response.data === 'object') {
          return response.data;
        }
      });

    };
  });
