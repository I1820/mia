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

    this.getState = function (agentId, deviceId, type, state) {
      var msg = {
        'agent_id': agentId,
        'device_id': deviceId,
        'type': type,
        'states': [state]
      };
      $http.post('thing', msg).then(function (response) {
      });
    };

    this.setSetting = function () {
    };
  });
