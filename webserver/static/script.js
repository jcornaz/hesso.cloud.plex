// Module
var fileManager = angular.module('fileManager', ['ngRoute']);

// configure our routes
fileManager.config(function($routeProvider) {
    $routeProvider

    // route for the home page
    .when('/', {
        templateUrl : 'pages/home.html',
        controller  : 'mainController'
    })

    // route for the about page
    .when('/about', {
        templateUrl : 'pages/about.html',
        controller  : 'aboutController'
    })

});

// create the controller and inject Angular's $scope
fileManager.controller('mainController', function($scope) {


});

// create the controller and inject Angular's $scope
fileManager.controller('aboutController', function($scope) {


});