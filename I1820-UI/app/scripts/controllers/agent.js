'use strict';

/**
 * @ngdoc function
 * @name i1820UiApp.controller:AgentCtrl
 * @description
 * # AgentCtrl
 * Controller of the i1820UiApp
 */
angular.module('i1820UiApp')
  .controller('AgentCtrl', function ($scope, $routeParams) {
    $scope.agentId = $routeParams.agentId;
  });
