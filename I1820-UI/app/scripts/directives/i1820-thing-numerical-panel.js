'use strict';

/**
 * @ngdoc directive
 * @name i1820UiApp.directive:i1820ThingNumericalPanel
 * @description
 * # i1820SensorNumericalPanel
 */
angular.module('i1820UiApp')
  .directive('i1820ThingNumericalPanel', function ($interval, ModelService, ThingService) {
    return {
      templateUrl: 'views/templates/thing-numerical-panel.html',
      restrict: 'E',
      scope: {
        agentId: '=',
        type: '=',
        thingId: '=',
      },
      link: function ($scope) {
        $scope.states = [];
        $scope.settings = [];

        ModelService.getModel($scope.type).then(function (data) {
          if (typeof(data.states) !== undefined) {
            $scope.states = data.states;
          }
          if (typeof(data.settings) !== undefined) {
            $scope.settings = data.settings;
          }
          if ($scope.states.length !== 0) {
            $interval($scope.refresh, 1000);
          }
        });

        $scope.values = {};

        $scope.refresh = function () {
          ThingService.getState($scope.agentId, $scope.thingId,
                                $scope.type, []).then(function (data) {
            $scope.values = data;
          });
        };

        $scope.turn = function (setting, value) {
          ThingService.setSetting($scope.agentId, $scope.thingId, $scope.type, setting, value);
        };
      }
    };
  });
