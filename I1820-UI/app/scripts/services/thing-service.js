'use strict';

/**
 * @ngdoc service
 * @name i1820UiApp.ThingService
 * @description
 * # thingService
 * Service in the i1820UiApp.
 */
angular.module('i1820UiApp')
  .service('ThingService', function ($http, $interval) {
    // AngularJS will instantiate a singleton by calling "new" on this function

    this.getState = function (agentId, deviceId, type, state, retval) {
      var msg = {
        'agent_id': agentId,
        'device_id': deviceId,
        'type': type,
        'states': [state]
      };
      var _getState = function () {
        $http.post('thing', msg).then(function (response) {
          retval = response.data[state];
        });
      };
      $interval(_getState, 1000);
    };

    this.setSetting = function () {
    };
  });
