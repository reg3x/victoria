vicServices = angular.module('vicServices', [])

.factory('Panty', function ($resource) {
    return $resource('http://127.0.0.1:8000/panty');
});