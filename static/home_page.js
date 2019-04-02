

function addnew(){
    $("#ModalExample").modal('toggle');
    $("#ModalExample").on('click', '#add_course', function(e) {
        console.log("ayee")
        e.preventDefault();
        let post_body = {}
        post_body['course_id']=$("#course_id").val()
        $.post('/add_course',post_body,(data)=>{
            if(data.toString()=="True"){
                $("#ModalExample").modal('toggle');
                fetch_members_and_populate_courses();
            }
        })
    })

}
function hide_some(){   
    // document.getElementById('sidebar').style.visibility='hidden';
    document.getElementById('heading').style.visibility='hidden';
    $("#fail").css('display','none')
    $($("ul")[1]).css('display','none')
}



function fetch_members_and_populate_courses(){
    let html_str='';
    $.get('/mycourses',(data)=>{
        if(data){
            console.log(data)
            for(i=0;i<data.length;i++){

                html_str+=render_user_html(data[i])
            }
            if(i==0){
                html_str+="<center><span>No Courses yet add them by clicking this booty here</span></center>"
            }
            html_str+='</br><center><a href="#" onclick="addnew()"><i style="font-size:24px" class="fa">&#xf067;</i></a></center>'
            $("#mycontent").html(html_str)
            
        }
        
        
    })
    
}

function render_user_html(name){
   let html_str=`  <div class="media text-muted pt-3">
   <img src="static/idea.svg" class="bd-placeholder-img mr-2 rounded" width="32" height="42" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice" focusable="false" role="img" ></img>
   <div class="media-body pb-3 mb-0 small lh-125 border-bottom border-gray">
     <div class="d-flex justify-content-between align-items-center w-100">
       <a href="/mycourses/`+name+`" style="text-decoration:none"><strong class="text-gray-dark">`+name+`</strong></a>
       <a href="#" onclick="remove_course('`+name+`')" ><i style="font-size:24px" class="fa">&#xf068;</i></a>
     </div>
     
   </div>
 </div>

    `
 return html_str;
}

function remove_course(i){
    var $modal = $('#exampleModal');
    //console.log('Now end mee right fekin nowww')
    $modal.modal("show");
    $("#exampleModal").on('click', '#paramsOkay', function(e) {
        $("#exampleModal").modal("hide");
        
        $.post('/delete_course',{course_id:i},(data)=>{
            if(data.toString()=='True'){
                fetch_members_and_populate_courses();
            }
                
        })
    
    });
   
}
$(document).ready(()=>{
    hide_some();
    fetch_members_and_populate_courses();
    
    
})