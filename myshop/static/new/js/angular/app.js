  
    //console.log("SECTION", SECTION);
    var MyShop = angular.module('MyShop', ["ngRoute"]);

	MyShop.config(['$interpolateProvider', function($interpolateProvider) {
      $interpolateProvider.startSymbol('{[');
      $interpolateProvider.endSymbol(']}');
    }]);

	
    MyShop.config(['$routeProvider', function($routeProvider, SECTION) {
    	var SECTION = 'hcl';
	    $routeProvider.
	      when('/', {
	        templateUrl: '/'+SECTION+'/dashboard',
	        controller: 'SummaryController'
	      }).
	      when('/statistics', {
	        templateUrl: '/'+SECTION+'/statistics',
	        controller: 'SummaryController'
	      }).
	      when('/timeseries', {
	        templateUrl: '/'+SECTION+'/timeseries',
	        controller: 'TimeseriesController'
	      }).
	      when('/phones', {
	        templateUrl: 'partials/phone-list.html',
	        controller: 'PhoneListCtrl'
	      }).
	      when('/phones/:phoneId', {
	        templateUrl: 'partials/phone-detail.html',
	        controller: 'PhoneDetailCtrl'
	      }).
	      otherwise({        
	        redirectTo: '/'
	      });
  	}]);

    