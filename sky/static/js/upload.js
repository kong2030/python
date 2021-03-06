var FormValidation = function () {

    // validation using icons
    var handleUpload = function() {
        // for more info visit the official plugin documentation: 
            // http://docs.jquery.com/Plugins/Validation

            var form = $('#form_order_add');
            var error2 = $('.alert-danger', form);
            var success2 = $('.alert-success', form);

            form.validate({
                errorElement: 'span', //default input error message container
                errorClass: 'help-block help-block-error', // default input error message class
                focusInvalid: false, // do not focus the last invalid input
                ignore: "",  // validate all fields including form hidden input
                rules: {
                    name: {
                        minlength: 2,
                        required: true
                    }
                },

                invalidHandler: function (event, validator) { //display error alert on form submit              
                    success2.hide();
                    error2.show();
                    App.scrollTo(error2, -200);
                },

                errorPlacement: function (error, element) { // render error placement for each input type
                    var icon = $(element).parent('.input-icon').children('i');
                    icon.removeClass('fa-check').addClass("fa-warning");  
                    icon.attr("data-original-title", error.text()).tooltip({'container': 'body'});
                },

                highlight: function (element) { // hightlight error inputs
                    $(element)
                        .closest('.form-group').removeClass("has-success").addClass('has-error'); // set error class to the control group   
                },

                unhighlight: function (element) { // revert the change done by hightlight
                    
                },

                success: function (label, element) {
                    var icon = $(element).parent('.input-icon').children('i');
                    $(element).closest('.form-group').removeClass('has-error').addClass('has-success'); // set success class to the control group
                    icon.removeClass("fa-warning").addClass("fa-check");
                },
                // 表单验证通过后，提交ajax请求上传文件
                submitHandler: function (form) {
                    success2.show();
                    error2.hide();

                    //$("#submit").attr("disabled", true);
                   // $("#cancel").attr("disabled", true);

                   // form[0].submit(); // submit the form
                    var formData = new FormData();
                    formData.append("appSystem", $("#appSystem").val());
                    formData.append("module", $("#module").val());
                    formData.append("orderType", $("#orderType").val());
                    formData.append("updateFile", document.getElementById("updateFile").files[0]);  // get upload file ,dom object
                    formData.append("remark", $("#remark").val());
                    $.ajax({
                        url: "/sky/deploy/saveOrder",
                        type: "POST",
                        data: formData,
                        cache: false,
                        contentType: false,
                        processData: false,
                        beforeSend: function(){
                            // 弹出模态框，防止乱动
                            $('#myModal').modal({backdrop:'static',keyboard:false});
                        },
                        success: function(result,status){
                            // 隐藏模态框
                            $('#myModal').modal('hide');
                            if(result == "success"){
                                swal("Yes! upload success.", "", "success").then((value) => {
                                    window.location.href= "/sky/deploy/listOrder";
                                });
                            }else{
                                swal("Sorry! upload error.", "", "error");
                            }
                        },
                        error: function(result,status){
                                swal("Sorry! upload error.", "", "error");
                        }
                    });
                }
            });


    }

    return {
        //main function to initiate the module
        init: function () {
            handleUpload();
        }
    };

}();

jQuery(document).ready(function() {
    FormValidation.init();
});