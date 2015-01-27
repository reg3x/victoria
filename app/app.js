var vicApp = angular.module('vicApp', [
    'ngRoute',
    'vicController',
    'homeDirectives',
    'catalogDirectives',
    'cartDirectives'
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
            templateUrl: '/components/home/home.html'
        }).
        when('/catalog/', {
            templateUrl: '/components/catalog/catalog.html'
        }).
        when('/catalog/:product', {
            templateUrl: '/components/catalog/catalog.html'
        }).
        when('/cart/', {
            templateUrl: '/components/cart/cart.html'
        }).
        otherwise({
            redirectTo: '/'
        });
} ]);

//add config for headers
//add SPA router