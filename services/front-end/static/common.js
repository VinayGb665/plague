function sign_out(){
    sessionStorage.removeItem('user')
    $.post('/signout',(data)=>{
        console.log(data)
        if(data){
            window.location.href="/login"
        }
    })
}