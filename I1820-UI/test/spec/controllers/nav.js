'use strict';

describe('Controller: NavCtrl', function () {

  // load the controller's module
  beforeEach(module('i1820UiApp'));

  var NavCtrl,
    scope;

  // Initialize the controller and a mock scope
  beforeEach(inject(function ($controller, $rootScope) {
    scope = $rootScope.$new();
    NavCtrl = $controller('NavCtrl', {
      $scope: scope
      // place here mocked dependencies
    });
  }));

  it('should attach a list of awesomeThings to the scope', function () {
    expect(NavCtrl.awesomeThings.length).toBe(3);
  });
});
