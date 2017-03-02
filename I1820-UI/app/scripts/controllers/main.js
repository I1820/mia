'use strict';

/**
 * @ngdoc function
 * @name i1820UiApp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the i1820UiApp
 */
angular.module('i1820UiApp')
  .controller('MainCtrl', function ($scope, $http) {
    $http.get('/tenant').then(function (response) {
      $scope.tenant = response.data;
    });
  });
