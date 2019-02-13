var app=angular.module('mainApp',['ui.bootstrap']);

//解决angularjs 与 django 标签冲突问题
app.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{[');
    $interpolateProvider.endSymbol(']}');
});

// 修改密码
app.controller('configCtrl', function($scope, $http, $modal) {
	//产品新建或编辑 弹出模态框
	$scope.pwdChange = function() {
	    var modalInstance = $modal.open({
            backdrop:false, //点击空白不隐藏
            templateUrl : '/ocean/config/pwdPage',// script标签中定义的id
            controller : 'pwdChangeCtrl',// modal对应的Controller
            size : 'md',
            resolve : {
                data : function() {// data作为modal的controller传入的参数

                    return "success";// 用于传递数据
                }
            }
		})
	}
});

// 修改密码弹出模态框
app.controller('pwdChangeCtrl', function($scope, $modalInstance, data) {
      // 在这里处理要进行的操作
      $scope.ok = function() {
          $modalInstance.close();
      };
      $scope.cancel = function() {
          $modalInstance.dismiss('cancel');
      }
});

// 加密异步返回
app.controller('encryptCtrl', function($scope, $http,$compile) {

    $scope.encrypt_pwd = function () {
        var password = $scope.password;
        result = {"password":password};
        $http({
            method:'post',
            url:'/ocean/cmdb/encrypt',
            headers: {'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'}, //需要加上头
			data:$.param(result)
        }).success(function(response,status){
            $scope.password_ = response["password"]
            $scope.encrypt_str = response["encrypt_str"]
        });
    };

});


// cmdb管理
app.controller('cmdbCtrl', function($scope, $http, $compile) {

    //新增组件
    $scope.moduleAdd = function(){
        window.location.href="/ocean/cmdb/addModule";
    }

    //编辑组件
    $scope.moduleEdit = function(){
        //首先获取所有被选中的产品，默认取第一个来编辑
	    var moduleChecked = []
	    $("input[name='module-checkbox']:checked").each(function(i){
	        moduleChecked[i] = $(this).val()
	    })
        //如果都没选中，直接返回，什么也不做
        if(moduleChecked.length<1)return;

        window.location.href="/ocean/cmdb/editModule?moduleId="+moduleChecked[0];
    }

});


// website管理
app.controller('websiteCtrl', function($scope, $http, $compile) {

    //新增网址
    $scope.websiteAdd = function(){
        window.location.href="/ocean/config/addWebsite";
    }

    //编辑网址
    $scope.websiteEdit = function(){
        //首先获取所有被选中的，默认取第一个来编辑
	    var websiteChecked = []
	    $("input[name='website-checkbox']:checked").each(function(i){
	        websiteChecked[i] = $(this).val()
	    })
        //如果都没选中，直接返回，什么也不做
        if(websiteChecked.length<1)return;

        window.location.href="/ocean/config/editWebsite?websiteId="+websiteChecked[0];
    }

});
