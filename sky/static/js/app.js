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
        order_type = $("#orderType").val();
        result = {"app_name": $scope.app_name, "order_type": order_type};

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

    /* 开始发布页
    $scope.deployPage = function(order_code, order_type){
        if(order_type == 1){
            window.location.href="/sky/deploy/deployOrder?orderCode=" + order_code;
        }else if(order_type == 2){
            window.location.href="/sky/deploy/deployOrderSql?orderCode=" + order_code;
        }
    }*/

    // 查看日志
    $scope.showLog = function(index){
        swal($("#deploy-log-"+index).val())
    }

    // 发布，（手工上传升级包方式）
    $scope.deploy = function(order_code,current_env,module_name){
        //首先获取所有被选中的产品，默认取第一个来编辑
	    var deployChecked = []
	    $("input[name='deploy-checkbox']:checked").each(function(i){
	        deployChecked[i] = $(this).val()
	    })
        //如果都没选中，直接返回，什么也不做
        if(deployChecked.length<1)return;

        // 弹出模态框，防止乱动
        $('#myModal').modal({backdrop:'static',keyboard:false});

	    //ajax请求到后端
        $.ajax({
            type: "POST",
            url: "/sky/deploy/saveDeploy",
            traditional:true,   //加上这项可以传递数组
            data: {"deployChecked":deployChecked, "orderCode":order_code, "currentEnv":current_env, "moduleName":module_name},
            success: function(result,status){
                // 隐藏模态框
                $('#myModal').modal('hide');
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
    $scope.rollback = function(order_code,current_env,module_name){
        swal({
            title: "确定要回滚?",
            //text: "Once rollback, you will not be able to recover this imaginary file!",
            icon: "warning",
            buttons: true,
            dangerMode: true,
        })
        .then((willRollback) => {
            if (willRollback) {
                //首先获取所有被选中的产品，默认取第一个来编辑
                var deployChecked = []
                $("input[name='deploy-checkbox']:checked").each(function(i){
                    deployChecked[i] = $(this).val()
                })
                //如果都没选中，直接返回，什么也不做
                if(deployChecked.length<1)return;

                // 弹出模态框，防止乱动
                $('#myModal').modal({backdrop:'static',keyboard:false});

                //ajax请求到后端
                $.ajax({
                    type: "POST",
                    url: "/sky/deploy/saveRollback",
                    traditional:true,   //加上这项可以传递数组
                    data: {"deployChecked":deployChecked, "orderCode":order_code, "currentEnv":current_env, "moduleName":module_name},
                    success: function(result,status){
                        // 隐藏模态框
                        $('#myModal').modal('hide');
                        if(result == "success"){
                            swal("Yes! rollback success.", "", "success").then((value) => {
                                window.location.href="/sky/deploy/deployOrder?orderCode=" + order_code;
                            });
                        }else{
                            swal("Sorry! rollback error.", "", "error").then((value) => {
                                window.location.href="/sky/deploy/deployOrder?orderCode=" + order_code;
                            });
                        }
                    }
                });
            } else {
                swal("放弃回滚!");
            }
        });
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

    // 预览sql文件
    $scope.review = function(index){
        //alert($("div[name='sql_review']:hidden").length)
        $("#sql_review_"+index).show()
    }

    // 发布sql
    $scope.deploySql = function(){
        count_hidden = $("div[name='sql_review']:hidden").length;
        if(count_hidden == 0){
            order_code = $("#order-code").val();
            host_ip = $("#host-ip").val();
            module_name = $("#module-name").val();
            current_env = $("#current-env").val();
            data = {"orderCode":order_code, "currentEnv":current_env, "moduleName":module_name, "hostIp":host_ip};

            // 弹出模态框，防止乱动
            $('#myModal').modal({backdrop:'static',keyboard:false});

            $http({
                method:'post',
                url:'/sky/deploy/saveDeploySql',
                headers: {'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'}, //需要加上头
                data:$.param(data),
            }).success(function(result,status){
                // 隐藏模态框
                $('#myModal').modal('hide');
                if(result == "success"){
                    swal("Yes! deploy success.", "", "success").then((value) => {
                        window.location.href="/sky/deploy/deployOrderSql?orderCode=" + order_code;
                    });
                }else{
                    swal("Sorry! deploy error.", "", "error").then((value) => {
                        window.location.href="/sky/deploy/deployOrderSql?orderCode=" + order_code;
                    });
                }
            });
        }
    }


});
