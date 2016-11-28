'use strict';

/**
 * @ngdoc service
 * @name i1820UiApp.ModelService
 * @description
 * # ModelService
 * Service in the i1820UiApp.
 */
angular.module('i1820UiApp')
  .service('ModelService', function ($http) {
    // AngularJS will instantiate a singleton by calling "new" on this function

    this.getModel = function (type) {
      return $http.get('/model/' + type).then(function (response) {
        if (typeof response.data === 'object') {
          return response.data;
        }
      });
    };
  });
