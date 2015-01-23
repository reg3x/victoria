var vicApp = angular.module('vicApp', [
    'ngRoute',
    'vicController',
    'homeDirectives',
    'catalogDirectives'
]);

vicApp.directive('navbar', function () {
    return {
        'restrict': 'E',
        'templateUrl': 'components/navbar/navbar.html'
    };
});



vicApp.config(['$routeProvider',function ($routeProvider) {
    $routeProvider.
        when('/', {
            templateUrl: '/components/home/home.html',
        }).
        when('/catalog', {
            templateUrl: '/components/catalog/catalog.html'
        }).
        otherwise({
            redirectTo: '/'
        });
} ]);

//add config for headers
//add SPA router