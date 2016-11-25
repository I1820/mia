'use strict';

describe('Controller: AgentCtrl', function () {

  // load the controller's module
  beforeEach(module('i1820UiApp'));

  var AgentCtrl,
    scope;

  // Initialize the controller and a mock scope
  beforeEach(inject(function ($controller, $rootScope) {
    scope = $rootScope.$new();
    AgentCtrl = $controller('AgentCtrl', {
      $scope: scope
      // place here mocked dependencies
    });
  }));

  it('should attach a list of awesomeThings to the scope', function () {
    expect(AgentCtrl.awesomeThings.length).toBe(3);
  });
});
