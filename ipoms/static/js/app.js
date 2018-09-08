var app=angular.module('mainApp',['ui.bootstrap']);

//解决angularjs 与 django 标签冲突问题
app.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{[');
    $interpolateProvider.endSymbol(']}');
});

//产品管理页 controller
app.controller('productCtrl', function($scope, $http, $modal) {
	//产品新建或编辑 弹出模态框
	$scope.productAddModal = function(action) {
	    //如果是新增，弹出无内容模态框
	    if(action == "add"){
	        var modalInstance = $modal.open({
                backdrop:false, //点击空白不隐藏
                templateUrl : 'addProduct?action=add',// script标签中定义的id
                controller : 'productAddCtrl',// modal对应的Controller
                size : 'md',
                resolve : {
                    data : function() {// data作为modal的controller传入的参数
                        console.log("source:"+action);
                        return "success";// 用于传递数据
                    }
                }
		    })
	    }

	    //如果是编辑，弹出对应产品的模态框
	    if(action == "edit"){
            //首先获取所有被选中的产品，默认取第一个来编辑
	        var productChecked = []
	        $("input[name='product-checkbox']:checked").each(function(i){
	            productChecked[i] = $(this).val()
	        })
            //如果都没选中，直接返回，什么也不做
            if(productChecked.length<1)return;

            url = "addProduct?action=edit&&"+"productCode="+productChecked[0]

	        var modalInstance = $modal.open({
                backdrop:false, //点击空白不隐藏
                templateUrl : url,// script标签中定义的id
                controller : 'productAddCtrl',// modal对应的Controller
                size : 'md',
                resolve : {
                    data : function() {// data作为modal的controller传入的参数
                        console.log("source:"+productChecked);
                        return "success";// 用于传递数据
                    }
                }
		    })
	    }
	};

	//产品删除
	$scope.deleteProduct = function(){
	    //首先获取所有被选中的产品
	    var productChecked = []
	    $("input[name='product-checkbox']:checked").each(function(i){
	        productChecked[i] = $(this).val()
	    })
        //如果都没选中，直接返回，什么也不做
        if(productChecked.length<1)return;

        //确认
        if (confirm("Are you sure to delete ?") == false) {
            return;
        }

        //ajax请求到后端
        $.ajax({
            type: "POST",
            url: "/ipoms/stock/deleteProduct",
            traditional:true,   //加上这项可以传递数组
            data: {"productChecked":productChecked},
            success: function(result,status){
                if(result == "success"){
                    //删除成功，刷新页面
                    window.location.href="/ipoms/stock/listProduct";
                }else{
                    swal("Sorry! error to delete the data.", "", "error");
                }

            }
        });
	}
});

// 产品管理页弹出模态框
app.controller('productAddCtrl', function($scope, $modalInstance, data) {
      // 在这里处理要进行的操作
      $scope.ok = function() {
          $modalInstance.close();
      };
      $scope.cancel = function() {
          $modalInstance.dismiss('cancel');
      }
});


// 新股状态页 controller
app.controller('stockStatusCtrl', function($scope, $http) {
    // 表格插件初始化
    var oTable = $('#table_stock_status').dataTable({
        "lengthMenu": [
            [5, 15, 20, -1],
            [5, 15, 20, "All"] // change per page values here
        ],
        // set the initial value
        "pageLength": 5,

        "language": {
            "lengthMenu": " _MENU_ records",
        },
        "columnDefs": [{ // set default column settings
            'orderable': true,
            'targets': [0]
        }, {
            "searchable": true,
            "targets": [0]
        }],
        "order": [
            [0, "asc"]
        ] // set first column as a default sort by asc
    });

});

// 新股状态流转页 controller
app.controller('stockOperationCtrl', function($scope, $http) {
    // 表格插件初始化
    var oTable = $('#table_stock_operation').dataTable({
        "lengthMenu": [
            [5, 15, 20, -1],
            [5, 15, 20, "All"] // change per page values here
        ],
        // set the initial value
        "pageLength": 5,

        "language": {
            "lengthMenu": " _MENU_ records",
        },
        "columnDefs": [{ // set default column settings
            'orderable': true,
            'targets': [0]
        }, {
            "searchable": true,
            "targets": [0]
        }],
        "order": [
            [0, "asc"]
        ] // set first column as a default sort by asc
    });

});


