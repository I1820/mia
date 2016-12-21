'use strict';

/**
 * @ngdoc directive
 * @name i1820UiApp.directive:i1820ThingNumericalPanel
 * @description
 * # i1820SensorNumericalPanel
 */
angular.module('i1820UiApp')
  .directive('i1820ThingNumericalPanel', function ($interval, $socket, ModelService, ThingService) {
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

        var stateWatcher;
        $scope.values = {};
        var refreshStates = function () {
          ThingService.getState($scope.agentId, $scope.thingId,
                                $scope.type, []).then(function (data) {
            for (var i in data) {
              $scope.values[i] = data[i];
            }
          });
        };

        var refreshEvents = function (event) {
          event = JSON.parse(event);
          if (event['agent_id'] === $scope.agentId &&
              event['device_id'] === $scope.thingId &&
                event['type'] === $scope.type) {
            for (var i in event.state) {
              $scope.values[i] = event.state[i];
            }
          }
        };

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
            stateWatcher = $interval($scope.refresh, 5000);
          }

          if ($scope.events.length !== 0) {
            $socket.addListener('event', refreshEvents);
          }
        });

        $scope.$on('$destroy', function () {
          if ($scope.states.length !== 0) {
            $interval.cancel(stateWatcher);
          }

          if ($scope.events.length !== 0) {
            $socket.removeListener('event', refreshEvents);
          }
        });


        $scope.refresh = refreshStates;

        $scope.turn = function (setting, value) {
          ThingService.setSetting($scope.agentId, $scope.thingId, $scope.type, setting, value);
        };
      }
    };
  });
