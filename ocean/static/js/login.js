var app=angular.module('loginApp',[]);

//解决angularjs 与 django 标签冲突问题
app.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{[');
    $interpolateProvider.endSymbol(']}');
});

app.controller('loginCtrl', function($scope, $http,$compile) {

    $scope.login = function () {
        var username = $scope.username;
        var password = $scope.password;
        result = {"username":username,"password":password};
        $http({
            method:'post',
            url:'/ocean/loginCheck',
            headers: {'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'}, //需要加上头
			data:$.param(result)
        }).success(function(response,status){
            if(response == "ok"){
                window.location.href="/ocean/index";
            }else{
                $("#error").css("display","block")
                $scope.message = response

            }


        });
    };

});