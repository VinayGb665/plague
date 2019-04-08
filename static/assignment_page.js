function generate(e){
    var ass_name = e.target.nextElementSibling.id;
    var thresh = e.target.nextElementSibling.value;
    var spinner = e.target.previousElementSibling;
    course=location.href.substr(location.href.lastIndexOf('/') + 1)
    spinner.style.display = ""
    e.target.style.display = "none"
    // $("#generate_btn").css('display','none')
    //  $("#spinner").show()
    console.log('clicked')
    $.post('/generate',{ass_name:ass_name,thresh:thresh,course:course},(data)=>{
        if(data){
            // console.log(data)
            
            $("#mod_bod").html('');
            spinner.style.display = "none"
            $("#mod_bod").html(data);
            $('.dataframe')[0].setAttribute('class','table table-borderless table-dark')
            $('table')[0].setAttribute('border','0')
            $('table')[0].setAttribute('width','400')
            e.target.style.display = ""
            $("#ModalExample").modal('toggle');
            $("#generate_btn").css('display','')
            disp_thresh(thresh)
            
        }
    })

    
}
function disp_thresh(a){
    let ar = $('td')
    for(i=0;i<ar.length;i++){
        if(Number(ar[i].innerHTML)>a){
            console.log('aaa')
            ar[i].style.backgroundColor ="red";
            ar[i].style.borderRadius ="1%";
            // ar[i].css('border-radius','5%')
        }
    }
}


function addnew(){
    // $("#ModalExample").modal('toggle');
    // $("#ModalExample").on('click', '#add_mem', function(e) {
    //     console.log("ayee")
    //     e.preventDefault();
    //     let post_body = {}
    //     post_body['username']=$("#new_name").val()
    //     post_body['email']=$("#new_mail").val()
    //     post_body['password']="test123"
    //     $.post('/add_member',post_body,(data)=>{
    //         if(data.toString()=="Done"){
    //             $("#ModalExample").modal('toggle');
    //             fetch_members_and_populate();
    //         }
    //     })
    // })
    window.location.href = "/"

}
function hide_some(){   
    // document.getElementById('sidebar').style.visibility='hidden';
    document.getElementById('heading').style.visibility='hidden';
    $("#fail").css('display','none')
    $($("ul")[1]).css('display','none')
    $('body').css('overflow','auto')
}



function fetch_members_and_populate(){
    let html_str='';
    course=location.href.substr(location.href.lastIndexOf('/') + 1)
    $.get('/listass/'+course,(data)=>{
        if(data){
            
            for(i=0;i<data.length;i++){

                html_str+=render_user_html(data[i].ass,data[i].thresh,course)
            }
            if(i==0){
                html_str+="<center><span>No users yet add them by clicking this booty here</span></center>"
            }
            html_str+='</br><center><a href="#" onclick="addnew()"><i style="font-size:24px" class="fa">&#xf067;</i></a></center>'
            $("#mycontent").html(html_str)
            event_listeners();
        }
        
        
    })
    
}

function render_user_html(name,thresh,course){
   let html_str=`  <div class="media text-muted pt-3">
   <img src="/static/assignment.svg" class="bd-placeholder-img mr-2 rounded" width="32" height="32" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice" focusable="false" role="img" aria-label="Placeholder: 32x32"><title>Placeholder</title><rect width="100%" height="100%" fill="#007bff"/></img>
   <div class="media-body pb-3 mb-0 small lh-125 border-bottom border-gray">
   
     
     <div class="d-flex justify-content-between align-items-center w-100">
     

       <strong class="text-gray-dark">`+name+`</strong>
       <div >
       <div class="spinner-border m-1" style="display:none"  role="status">
       <span class="sr-only">Loading...</span>
     </div>
       <button id="generate_btn" class="btn btn-danger"  style="margin-right:20px">Generate</button>       
   <input style="width:50px;visibility:hidden;border:1px solid #1284e8;border-radius:10%;padding:3px;" value="`+thresh+`"  id="`+name+`"/>
       
       <a style="text-decoration:none" class="setter" href="#" ><img src="/static/settings.svg" class="bd-placeholder-img mr-2 rounded" width="22" height="22" role="img"></img></a>
       
           
      </div>
     </div>
    
     <span class="d-block">`+course+`</span>
   </div>
 </div>

    `
 return html_str;
}

function event_listeners(){
$("button").click((e)=>{
    generate(e);
})
$(".setter").click((e)=>{
    e.preventDefault();
    let threshEl = e.target.parentElement.previousElementSibling;
    threshEl.style.visibility="";
    setTimeout(() => {
        threshEl.style.visibility="hidden";
    }, 5000);
})
   
}
function remove_user(i){
    var $modal = $('#exampleModal');
    //console.log('Now end mee right fekin nowww')
    $modal.modal("show");
    $("#exampleModal").on('click', '#paramsOkay', function(e) {
        $("#exampleModal").modal("hide");
    $.post('/delete',{user:i},(data)=>{
        console.log(data)
        fetch_members_and_populate()
    })
    
    });
   
}
$(document).ready(()=>{
    hide_some();
    fetch_members_and_populate();
    
    
})