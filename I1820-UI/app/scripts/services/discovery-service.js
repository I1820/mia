'use strict';

/**
 * @ngdoc service
 * @name i1820UiApp.DiscoveryService
 * @description
 * # DiscoveryService
 * Service in the i1820UiApp.
 */
angular.module('i1820UiApp')
  .service('DiscoveryService', function () {
    // AngularJS will instantiate a singleton by calling "new" on this function
    var Agents = {};

    var fetchAgents = function () {
      $.getJSON('discovery', function (result) {
        Agents = result;
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
  });
