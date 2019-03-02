var FormValidation = function () {

    // 修改密码页验证
    var pwdValidation = function() {
        // for more info visit the official plugin documentation:
            // http://docs.jquery.com/Plugins/Validation

            var form2 = $('#form_pwd_change');
            var error2 = $('.alert-danger', form2);
            var success2 = $('.alert-success', form2);

            form2.validate({
                errorElement: 'span', //default input error message container
                errorClass: 'help-block help-block-error', // default input error message class
                focusInvalid: false, // do not focus the last invalid input
                ignore: "",  // validate all fields including form hidden input

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

                submitHandler: function (form) {
                    success2.show();
                    error2.hide();
                    //form[0].submit(); // submit the form
                    var oldPwd = $("#oldPwd").val();
                    var newPwd1 = $("#newPwd1").val();
                    var newPwd2 = $("#newPwd2").val();
                    if(newPwd1 != newPwd2){
                        swal("两次输入的密码不同!", "", "error")
                    }else{
                        //ajax请求到后端
                        $.ajax({
                            type: "POST",
                            url: "/ocean/config/savePwd",
                            data: {"oldPwd":oldPwd, "newPwd":newPwd1},
                            success: function(result,status){
                                if(result == "success"){
                                    swal("Yes! save success.", "", "success")
                                }else{
                                    swal(result, "", "error")
                                }
                            }
                        });
                    }
                }
            });
    }

    // 新增task 页面验证
    var taskValidation = function() {
        // for more info visit the official plugin documentation: 
            // http://docs.jquery.com/Plugins/Validation

            var form2 = $('#form_task_add');
            var error2 = $('.alert-danger', form2);
            var success2 = $('.alert-success', form2);

            // sql验证
            jQuery.validator.addMethod("sql", function(value, element){
	            var reg = /^select count/;
	            return this.optional(element)||(reg.test(value));
	        }, "只能是select语句");
 

            form2.validate({
                errorElement: 'span', //default input error message container
                errorClass: 'help-block help-block-error', // default input error message class
                focusInvalid: false, // do not focus the last invalid input
                ignore: "",  // validate all fields including form hidden input
                rules: {
                    name: {
                        minlength: 2,
                        required: true
                    },
                    email: {
                        required: true,
                        email: true
                    },
                    email: {
                        required: true,
                        email: true
                    },
                    url: {
                        required: true,
                        url: true
                    },
                    threshold: {
                        required: true,
                        number: true
                    },
                    digits: {
                        required: true,
                        digits: true
                    },
                    creditcard: {
                        required: true,
                        creditcard: true
                    },
                    sql: {
                        required: true,
                        sql: true
                    },
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

                submitHandler: function (form) {
                    success2.show();
                    error2.hide();
                    form[0].submit(); // submit the form
                }
            });


    }



    return {
        //main function to initiate the module
        init: function () {

            pwdValidation();
            taskValidation();


        }

    };

}();

jQuery(document).ready(function() {
    FormValidation.init();
});