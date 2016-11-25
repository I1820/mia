'use strict';

describe('Service: thingService', function () {

  // load the service's module
  beforeEach(module('i1820UiApp'));

  // instantiate service
  var thingService;
  beforeEach(inject(function (_thingService_) {
    thingService = _thingService_;
  }));

  it('should do something', function () {
    expect(!!thingService).toBe(true);
  });

});
