'use strict';

/**
 * @ngdoc service
 * @name i1820UiApp.DiscoveryService
 * @description
 * # DiscoveryService
 * Service in the i1820UiApp.
 */
angular.module('i1820UiApp')
  .service('DiscoveryService', function ($http, $interval) {
    // AngularJS will instantiate a singleton by calling "new" on this function
    var Agents = {};

    var fetchAgents = function () {
      $http.get('discovery').then(function (response) {
        Agents = response.data;
      });
    };

    this.refresh = function () {
      fetchAgents();
    };

    this.query = function (agentId) {
      if (agentId) {
        return Agents[agentId];
      } else {
        return Agents;
      }
    };

    $interval(fetchAgents, 5000);
  });
