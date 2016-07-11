/**
 * Created by yangbo on 2016-4-16.
 */
var app = angular.module("book", []);

app.controller("indexCtrl", ["$scope", "$http", function ($scope, $http) {

    $scope.keyValue = "";

    $scope.add = function () {
        $http({
            method: "GET",
            url: "/getList/add/" + $scope.keyValue
        }).success(function (data) {
            if(data == "success"){
                $scope.getList();
            }
        })
    };

    $scope.down = function (title,desc) {

        $http({
            method: "GET",
            url: "/getList/down/"+title+"/"+desc.split("/")[0]
        }).success(function (data) {
            $scope.Downlist = data;
        })
    };


    $scope.getDList = function (tag) {
        $http({
            method: "GET",
            url: "/getList/getDList/"+tag
        }).success(function (data) {
            $scope.Dlist = data;
        })
    };

    $scope.getList = function () {
        $http({
            method: "GET",
            url: "/getList"
        }).success(function (data) {
            $scope.list = data;
        })
    };



    $scope.getList();
}]);