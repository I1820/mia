'use strict';

/**
 * @ngdoc function
 * @name i1820UiApp.controller:PluginCtrl
 * @description
 * # PluginCtrl
 * Controller of the i1820UiApp
 */
angular.module('i1820UiApp')
  .controller('PluginCtrl', function ($scope, $http, $interval) {
    $scope.plugins = {};

    var fetchPlugins = function () {
      $http.get('/plugin').then(function (response) {
        $scope.plugins = response.data;
      });
    };

    $interval(fetchPlugins, 5000);
  });
