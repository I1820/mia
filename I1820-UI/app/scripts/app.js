'use strict';

/**
 * @ngdoc overview
 * @name i1820UiApp
 * @description
 * # i1820UiApp
 *
 * Main module of the application.
 */
angular
  .module('i1820UiApp', [
    'ngAnimate',
    'ngCookies',
    'ngResource',
    'ngRoute',
    'ngSanitize',
    'ngTouch',
    'btford.socket-io',
    'yaru22.angular-timeago'
  ])
  .config(function ($routeProvider) {
    $routeProvider
      .when('/', {
        templateUrl: 'views/main.html',
        controller: 'MainCtrl',
        controllerAs: 'main'
      })
      .when('/about', {
        templateUrl: 'views/about.html',
        controller: 'AboutCtrl',
        controllerAs: 'about'
      })
      .when('/agent/:agentId', {
        templateUrl: 'views/agent.html',
        controller: 'AgentCtrl',
        controllerAs: 'agent'
      })
      .when('/plugin', {
        templateUrl: 'views/plugin.html',
        controller: 'PluginCtrl',
        controllerAs: 'plugin'
      })
      .otherwise({
        redirectTo: '/'
      });
  })
  .factory('$socket', function (socketFactory) {
      return socketFactory();
  });
