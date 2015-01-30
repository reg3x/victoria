var vicApp = angular.module('catalogDirectives', [ ]);

vicApp.directive('catcontainer', function () {
    return{
        restrict : 'E',
        templateUrl: '/components/catalog/catalog-container.html',
        controller : ['$http', '$scope','$routeParams', 'Panty', function ($http, $scope, $routeParams, Panty) {
            
            if (typeof $routeParams.product === 'undefined') {
                console.dir('no parameter provided: '+ typeof $routeParams.product);

                $http.get('/components/catalog/all.json').
                success(function(data) {
                    console.log("all.json loaded successfuly");
                    console.log("parameters: "+ $routeParams.product);
                    $scope.product = data;
                }).
                error(function () {
                    console.log("{{$routeParams.product}}.json NOT loaded successfuly");        
                });
                
            }
            else {
                console.dir('parameter provided: '+ $routeParams.product);
                      
                //added to test REST API
                Panty.query(function (data) {
                      $scope.product = data;
                });

                /* --- this code works with the mockup data
                $http.get('/components/catalog/'+$routeParams.product+'.json').
                success(function(data) {
                    console.log($routeParams.product+".json loaded successfuly");
                    console.log("parameters: "+ $routeParams.product);
                    $scope.product = data;
                }).
                error(function () {
                    console.log("{{$routeParams.product}}.json NOT loaded successfuly");        
                });
                */  
            }

        }],
    }
});