'use strict';

describe('Directive: i1820DiscoveryPanel', function () {

  // load the directive's module
  beforeEach(module('i1820UiApp'));

  var element,
    scope;

  beforeEach(inject(function ($rootScope) {
    scope = $rootScope.$new();
  }));

  it('should make hidden element visible', inject(function ($compile) {
    element = angular.element('<i1820-discovery-panel></i1820-discovery-panel>');
    element = $compile(element)(scope);
    expect(element.text()).toBe('this is the i1820DiscoveryPanel directive');
  }));
});
