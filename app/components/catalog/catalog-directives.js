var vicApp = angular.module('catalogDirectives', [ ]);

vicApp.directive('catcontainer', function () {
    return{
        restrict : 'E',
        templateUrl: '/components/catalog/catcontainer.html',
        controller : ['$http', '$scope','$routeParams', function ($http, $scope, $routeParams) {
            
            if (typeof $routeParams.product === 'undefined') {
                console.dir('no parameter provided: '+ typeof $routeParams.product);
                }
            else {
                console.dir('parameter provided: '+ $routeParams.product);
                
                $http.get('/components/catalog/'+$routeParams.product+'.json').
                success(function(data) {
                    console.log($routeParams.product+".json loaded successfuly");
                    console.log("parameters: "+ $routeParams.product);
                    $scope.product = data;
                }).
                error(function () {
                    console.log("{{$routeParams.product}}.json NOT loaded successfuly");        
                });
            }

        }],
    }
});