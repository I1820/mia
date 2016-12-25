'use strict';

/**
 * @ngdoc function
 * @name i1820UiApp.controller:NavCtrl
 * @description
 * # NavCtrl
 * Controller of the i1820UiApp
 */
angular.module('i1820UiApp')
  .controller('NavCtrl', function ($scope, $location) {
    $scope.$watch(function () {
      return $location.path();
    }, function (path) {
      $scope.path = path;
      if (path.includes('plugin')) {
        $scope.activeView = 'plugin';
      } else if (path.includes('about')) {
        $scope.activeView = 'about';
      } else if (path.includes('agent')) {
        $scope.activeView = 'agent';
      } else {
        $scope.activeView = 'home';
      }
    });
  });
