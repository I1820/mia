'use strict';

describe('Service: ModelService', function () {

  // load the service's module
  beforeEach(module('i1820UiApp'));

  // instantiate service
  var ModelService;
  beforeEach(inject(function (_ModelService_) {
    ModelService = _ModelService_;
  }));

  it('should do something', function () {
    expect(!!ModelService).toBe(true);
  });

});
