vicServices = angular.module('vicServices', [])

.factory('pantyService', function ($resource) {
    return $resource('http://127.0.0.1:8000/catalog/panty');
})

.factory('brasierService', function ($resource) {
    return $resource('http://127.0.0.1:8000/catalog/brasier');
})

.factory('leggingService', function ($resource) {
    return $resource('http://127.0.0.1:8000/catalog/legging');
})

.factory('creamService', function ($resource) {
    return $resource('http://127.0.0.1:8000/catalog/cream');
})

.factory('butterService', function ($resource) {
    return $resource('http://127.0.0.1:8000/catalog/butter');
})

.factory('fraganceService', function ($resource) {
    return $resource('http://127.0.0.1:8000/catalog/fragance');
});