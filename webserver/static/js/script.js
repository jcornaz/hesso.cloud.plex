// Module
var fileManager = angular.module('fileManager', ['ngRoute', 'angularTreeview']);

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

fileManager.controller('mainController', function($scope) {


});

fileManager.controller('aboutController', function($scope, $http) {

    $http.get('/about').success(function(response)
    {
        $scope.version = response.version;
    });

});

fileManager.controller('treeViewController', function($scope, $http) {

    $http.get('/files').success(function($response)
    {
        $scope.treedata =
        [
            $response
        ];
    });

    $scope.$watch('home_treeview.currentNode', function(newObj, oldObj) {
        if($scope.home_treeview && angular.isObject($scope.home_treeview.currentNode)) {
            console.log('Node Selected!!');
            console.log($scope.home_treeview.currentNode);
        }
    }, false);
});