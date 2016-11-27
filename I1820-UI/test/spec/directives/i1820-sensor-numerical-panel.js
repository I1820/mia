'use strict';

describe('Directive: i1820SensorNumericalPanel', function () {

  // load the directive's module
  beforeEach(module('i1820UiApp'));

  var element,
    scope;

  beforeEach(inject(function ($rootScope) {
    scope = $rootScope.$new();
  }));

  it('should make hidden element visible', inject(function ($compile) {
    element = angular.element('<-i1820-sensor-numerical-panel></-i1820-sensor-numerical-panel>');
    element = $compile(element)(scope);
    expect(element.text()).toBe('this is the I1820SensorNumericalPanel directive');
  }));
});
