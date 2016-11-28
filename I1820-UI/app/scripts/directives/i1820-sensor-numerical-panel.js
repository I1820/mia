'use strict';

/**
 * @ngdoc directive
 * @name i1820UiApp.directive:i1820SensorNumericalPanel
 * @description
 * # i1820SensorNumericalPanel
 */
angular.module('i1820UiApp')
  .directive('i1820SensorNumericalPanel', function ($interval, ModelService, ThingService) {
    return {
      templateUrl: 'views/templates/sensor-numerical-panel.html',
      restrict: 'E',
      scope: {
        agentId: '=',
        type: '=',
        thingId: '=',
      },
      link: function ($scope) {
        $scope.states = [];

        ModelService.getModel($scope.type).then(function (data) {
          $scope.states = data.states;
        });

        $scope.values = {};

        $scope.refresh = function () {
          ThingService.getState($scope.agentId, $scope.thingId,
                                $scope.type, []).then(function (data) {
            $scope.values = data;
          });
        };

        $interval($scope.refresh, 1000);
      }
    };
  });
