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

    });

    $scope.treedata =
    [
        { "label" : "User", "id" : "role1", "children" : [
            { "label" : "subUser1", "id" : "role11", "children" : [] },
            { "label" : "subUser2", "id" : "role12", "children" : [
                { "label" : "subUser2-1", "id" : "role121", "children" : [
                    { "label" : "subUser2-1-1", "id" : "role1211", "children" : [] },
                    { "label" : "subUser2-1-2", "id" : "role1212", "children" : [] }
                ]}
            ]}
        ]},
        { "label" : "Admin", "id" : "role2", "children" : [] },
        { "label" : "Guest", "id" : "role3", "children" : [] }
    ];

    $scope.$watch('home_treeview.currentNode', function(newObj, oldObj) {
        if($scope.home_treeview && angular.isObject($scope.home_treeview.currentNode)) {
            console.log('Node Selected!!');
            console.log($scope.home_treeview.currentNode);
        }
    }, false);
});