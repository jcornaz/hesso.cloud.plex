// Module
var fileManager = angular.module('fileManager', ['ngRoute', 'angularTreeview', 'ngFileUpload']);

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
        var path = $scope.details.path;

        if(window.confirm("You are about to delete the file "+ path + "\n\nAre you sure?"))
        {
            console.log('Try to delete '+ path);

            $http.delete('/file/'+ path).success(function(response)
            {
                $route.reload();
            });
        }
    };
});

fileManager.controller('directory_details', function($scope, $http, $route, Upload, $timeout)
{
    $scope.deleteDirectory = function()
    {
        var path = $scope.details.path;

        if(window.confirm("You are about to delete the directory "+ path + "\n\nAre you sure?"))
        {
            console.log('Try to delete '+ $scope.details.path);

            $http.delete('/file/'+ path).success(function(response)
            {
                $route.reload();
            });
        }
    };

    $scope.uploadFiles = function (files)
    {
        var path = $scope.details.path;
        $scope.files = files;

        if (files && files.length)
        {
            Upload.upload({url: '/file/'+ path, data: { files: files } }).then(function (response)
            {
                $timeout(function ()
                {
                    $scope.result = response.data;
                });

                if(response.data.error)
                {
                    alert(response.data.message);
                }
                else
                {
                    $route.reload();
                }
            },
            function (response)
            {
                if (response.status > 0)
                {
                    $scope.errorMsg = response.status + ': ' + response.data;
                }
            },
            function (evt)
            {
                $scope.progress = Math.min(100, parseInt(100.0 * evt.loaded / evt.total));
            });
        }
    };

    $scope.createDirectory = function()
    {
        var directoryName = prompt('The name of the folder you would like create');
        if(directoryName)
        {
            var path = $scope.details.path
                        ? sprintf("%s/%s", $scope.details.path, directoryName)
                        : directoryName;

            $http.put('/file/'+ path).success(function(response)
            {
                $route.reload();
                if(response.error)
                {
                    console.log(response.message);
                }
            });
        }
    };
});

fileManager.controller('treeViewController', function($scope, $http)
{
    $http.get('/files').success(function($response)
    {
        $scope.treedata = [ $response ];
    });
})
.directive('details', function($http, $compile, $templateRequest)
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

                        $templateRequest(templatePath).then(function(html)
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