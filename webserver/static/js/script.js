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

fileManager.controller('file_details', function($scope, $http, $route)
{
    $scope.deleteFile = function()
    {
        console.log('Try to delete '+ $scope.details.path)

        $http.delete('/file/'+ $scope.details.path).success(function(response)
        {
            alert(response.message);
            $route.reload();
        });
    };
});

fileManager.controller('directory_details', function($scope, $http, $route)
{
    $scope.deleteDirectory = function()
    {
        console.log('Try to delete '+ $scope.details.path)

        $http.delete('/file/'+ $scope.details.path).success(function(response)
        {
            alert(response.message);
            $route.reload();
        });
    };
});

fileManager.controller('treeViewController', function($scope, $http)
{
    $http.get('/files').success(function($response)
    {
        $scope.treedata = [ $response ];
    });
})
.directive('details', function($http, $compile) // http://stackoverflow.com/questions/13980896/watching-for-data-changes-in-an-angular-directive
{
    return {
        restrict: 'A',
        link: function(scope, element)
        {
            scope.$watch('home_treeview.currentNode', function(newObj, oldObj)
            {
                if(scope.home_treeview && angular.isObject(scope.home_treeview.currentNode))
                {
                    var path = scope.home_treeview.currentNode.id;

                    $http.get('/file/' + path).success(function(json)
                    {
                        var templatePath;

                        if(json.isFile)
                        {
                            templatePath = 'static/pages/file_detail.html';
                        }
                        else
                        {
                            templatePath = 'static/pages/directory_detail.html';
                        }

                        $http.get(templatePath).success(function(html)
                        {
                            var newScope = scope.$new();
                            newScope.details = json;

                            var template = angular.element(html);
                            var linkFn = $compile(template);
                            var templateCompiled = linkFn(newScope);

                            element.html('');
                            element.append(templateCompiled);
                        });
                    });
                }
            });
        }
    };
});