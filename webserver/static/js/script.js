// Module
var fileManager = angular.module('fileManager', ['ngRoute']);

// configure our routes
fileManager.config(function($routeProvider) {
    $routeProvider

    // route for the home page
    .when('/', {
        templateUrl : 'static/pages/home.html',
        controller  : 'mainController'
    })

    // route for the about page
    .when('/about', {
        templateUrl : 'static/pages/about.html',
        controller  : 'aboutController'
    })
});

// create the controller and inject Angular's $scope
fileManager.controller('mainController', function($scope) {


});

// create the controller and inject Angular's $scope
fileManager.controller('aboutController', function($scope, $http) {

    $http.get("/about").success(function(response)
    {
        $scope.version = response.version;
    });

});