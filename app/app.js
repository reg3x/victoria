var vicApp = angular.module('vicApp', ['vicController']);

vicApp.directive('navbar', function () {
    return {
        'restrict': 'E',
        'templateUrl': 'components/navbar/navbar.html'
    };
});

vicApp.directive('carousel', function () {
    return{
        'restrict': 'E',
        'templateUrl': 'components/carousel/carousel.html',
    };
});

//add config for headers
//add SPA router