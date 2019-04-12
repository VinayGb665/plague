function hide_some(){   
    document.getElementById('sidebar').style.visibility='hidden';
    document.getElementById('heading').style.visibility='hidden';
    $("#fail").css('display','none')
}

function add_event_listeners(){

    $("#login_form").on('submit',(e)=>{
        e.preventDefault();
        let body={'username':$("#inputEmail").val(),'password':$("#inputPassword").val()}
        $.post('/login',body,(data)=>{
            
            if(data[0].toString()=="True"){
                sessionStorage.setItem('user',data[1])
                if(data[2]==1){
                    sessionStorage.setItem('isAdmin',true)
                    window.location.href="/admin"
                }
                window.location.href="/home"
            }
            else{
                console.log('Error with logging in')
                $("#fail").css('display','block');
            }
        })
    })
}

$(document).ready(()=>{

hide_some()
//  ||
//  ||
//  \/
add_event_listeners();

})