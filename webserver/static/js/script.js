// Module
var fileManager = angular.module('fileManager', ['ngRoute', 'angularTreeview']);

// configure our routes
fileManager.config(function($routeProvider)
{
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

fileManager.controller('mainController', function($scope)
{

});

fileManager.controller('aboutController', function($scope, $http)
{
    $http.get('/about').success(function(response)
    {
        $scope.version = response.version;
    });

});

fileManager.controller('file_details', function($scope)
{
    $scope.deleteFile = function(path)
    {
        console.log("Deleting file ...");
    };
});

fileManager.controller('treeViewController', function($scope, $http, $sce)
{
    $http.get('/files').success(function($response)
    {
        $scope.treedata = [ $response ];
    });

/*    $scope.$watch('home_treeview.currentNode', function(newObj, oldObj)
    {
        if($scope.home_treeview && angular.isObject($scope.home_treeview.currentNode))
        {
            var path = $scope.home_treeview.currentNode.id;

            $http.get('/file/' + path).success(function(html)
            {
                $scope.details = $sce.trustAsHtml(html);
            });
        }
    }, false);*/
});

fileManager.directive("details", function()
{
    return { // Cannot add a new line here
        linker: function($scope, $http)
        {
            console.log('Directive called.')

            if($scope.home_treeview && angular.isObject($scope.home_treeview.currentNode))
            {
                var path = $scope.home_treeview.currentNode.id;
                var html = 'no template';

                $http.get('/file/' + path).success(function(html)
                {
                    template = html;
                });
            }
        }
    };
});

fileManager.directive('test', function()
{
    return {
        linker: function(scope, element)
        {
            console.log('Entered into directive.');
            element.append('Hello');
        }
    };
});