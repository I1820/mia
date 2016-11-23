'use strict';

describe('Service: DiscoveryService', function () {

  // load the service's module
  beforeEach(module('i1820UiApp'));

  // instantiate service
  var DiscoveryService;
  beforeEach(inject(function (_DiscoveryService_) {
    DiscoveryService = _DiscoveryService_;
  }));

  it('should do something', function () {
    expect(!!DiscoveryService).toBe(true);
  });

});
