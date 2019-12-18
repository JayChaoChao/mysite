
$(document).ready(function () {
    document.getElementById("btn").onclick=function () {
        console.log('点击了按钮')
        $.ajax({
            type:"get",
            url:"/ajaxshowstu/",
            dataType:"json",
            success:function (data,status) {
                console.log(data)
                var d=data['data']

                for(var i=0;i<d.length;i++){
                    document.write('<p>'+d[i][0]+'</p>')
                }

            }
        })
    }
})