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
        $scope.statistics = [];
        $scope.events = [];

        ModelService.getModel($scope.type).then(function (data) {
          if (data.hasOwnProperty('states')) {
            $scope.states = data.states;
          }
          if (data.hasOwnProperty('settings')) {
            $scope.settings = data.settings;
          }
          if (data.hasOwnProperty('statistics')) {
            $scope.statistics = data.statistics;
          }
          if (data.hasOwnProperty('events')) {
            $scope.events = data.events;
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
