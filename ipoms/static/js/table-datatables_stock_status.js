jQuery(document).ready(function() {
    var table = $('#table_stock_status');

    var oTable = table.dataTable({

        // Uncomment below line("dom" parameter) to fix the dropdown overflow issue in the datatable cells. The default datatable layout
        // setup uses scrollable div(table-scrollable) with overflow:auto to enable vertical scroll(see: assets/global/plugins/datatables/plugins/bootstrap/dataTables.bootstrap.js).
        // So when dropdowns used the scrollable div should be removed.
        //"dom": "<'row'<'col-md-6 col-sm-12'l><'col-md-6 col-sm-12'f>r>t<'row'<'col-md-5 col-sm-12'i><'col-md-7 col-sm-12'p>>",

        "lengthMenu": [
            [5, 15, 20, -1],
            [5, 15, 20, "All"] // change per page values here
        ],

        // Or you can use remote translation file
        //"language": {
        //   url: '//cdn.datatables.net/plug-ins/3cfcc339e89/i18n/Portuguese.json'
        //},

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

$("#btn-cl").click(function(){
    $("button[name='stock-status']").removeClass("blue green")
    $("button[name='stock-status']:not(#btn-cl)").addClass("green")
    $("#btn-cl").addClass("blue")

    //ajax请求到后端
    $.ajax({
         type: "POST",
         url: "/ipoms/stock/getStock",
         data: {"status":2},
         success: function(result,status){
            alert("status")
         }
    })
});