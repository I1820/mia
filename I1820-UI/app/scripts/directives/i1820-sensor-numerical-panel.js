'use strict';

/**
 * @ngdoc directive
 * @name i1820UiApp.directive:i1820SensorNumericalPanel
 * @description
 * # i1820SensorNumericalPanel
 */
angular.module('i1820UiApp')
  .directive('i1820SensorNumericalPanel', function () {
    return {
      template: '<div></div>',
      restrict: 'E',
      link: function postLink(scope, element, attrs) {
        element.text('this is the I1820SensorNumericalPanel directive');
      }
    };
  });
