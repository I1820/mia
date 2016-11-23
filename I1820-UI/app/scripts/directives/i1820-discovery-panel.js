'use strict';

/**
 * @ngdoc directive
 * @name i1820UiApp.directive:i1820DiscoveryPanel
 * @description
 * # i1820DiscoveryPanel
 */
angular.module('i1820UiApp')
  .directive('i1820DiscoveryPanel', function () {
    return {
      template: '<div></div>',
      restrict: 'E',
      link: function postLink(scope, element, attrs) {
        element.text('this is the i1820DiscoveryPanel directive');
      }
    };
  });
