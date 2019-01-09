var app=angular.module('mainApp',['ui.bootstrap']);

//解决angularjs 与 django 标签冲突问题
app.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{[');
    $interpolateProvider.endSymbol(']}');
});


// 加密异步返回
app.controller('encryptCtrl', function($scope, $http,$compile) {

    $scope.encrypt_pwd = function () {
        var password = $scope.password;
        result = {"password":password};
        $http({
            method:'post',
            url:'/sky/cmdb/encrypt',
            headers: {'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'}, //需要加上头
			data:$.param(result)
        }).success(function(response,status){
            $scope.password_ = response["password"]
            $scope.encrypt_str = response["encrypt_str"]
        });
    };

});


// 组件管理
app.controller('moduleCtrl', function($scope, $http, $compile) {

    //新增组件
    $scope.moduleAdd = function(){
        window.location.href="/sky/cmdb/addModule";
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

        window.location.href="/sky/cmdb/editModule?moduleName="+moduleChecked[0];

    }

});


// 发布单管理
app.controller('orderCtrl', function($scope, $http, $compile) {

    //新建发布单页，关联系统
    $scope.appChange = function(){
        result = {"app_name": $scope.app_name}

        $http({
            method:'post',
            url:'/sky/cmdb/getModulesByApp',
            headers: {'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'}, //需要加上头
			data:$.param(result),
        }).success(function(response,status){
            modules = response.split(",")
            $scope.modules = modules
        });
    }

    // 开始发布页
    $scope.deployPage = function(order_code){
        window.location.href="/sky/deploy/deployOrder?orderCode=" + order_code;
    }

    // 发布
    $scope.deploy = function(order_code,current_env,module_name){
        //首先获取所有被选中的产品，默认取第一个来编辑
	    var deployChecked = []
	    $("input[name='deploy-checkbox']:checked").each(function(i){
	        deployChecked[i] = $(this).val()
	    })
        //如果都没选中，直接返回，什么也不做
        if(deployChecked.length<1)return;

	    //ajax请求到后端
        $.ajax({
            type: "POST",
            url: "/sky/deploy/saveDeploy",
            traditional:true,   //加上这项可以传递数组
            data: {"deployChecked":deployChecked, "orderCode":order_code, "currentEnv":current_env, "moduleName":module_name},
            success: function(result,status){
                if(result == "success"){
                    swal("Yes! deploy success.", "", "success").then((value) => {
                        window.location.href="/sky/deploy/deployOrder?orderCode=" + order_code;
                    });
                }else{
                    swal("Sorry! deploy error.", "", "error").then((value) => {
                        window.location.href="/sky/deploy/deployOrder?orderCode=" + order_code;
                    });
                }
            }
        });
    }

    //回滚
    $scope.rollback = function(order_code){
        swal("rollback");
    }

    //md5校验
    $scope.md5check = function(order_code){
        //首先获取所有被选中的产品，默认取第一个来编辑
	    var deployChecked = []
	    $("input[name='deploy-checkbox']:checked").each(function(i){
	        deployChecked[i] = $(this).val()
	    })
        //如果都没选中，直接返回，什么也不做
        if(deployChecked.length<1)return;
        //显示隐藏块
        $("#md5-check").show()

        //ajax请求到后端
        $http({
            method:'post',
            url: "/sky/deploy/md5Check",
            headers: {'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'}, //需要加上头
			data:$.param({"hostIp":deployChecked[0], "orderCode":order_code})
        }).success(function(response,status){
            $scope.md5_form_list = response["md5_form_list"]
            $scope.result_all = response["result_all"]
        })
    }

});
