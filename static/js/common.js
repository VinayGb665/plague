function sign_out(){
    sessionStorage.removeItem('user')
    $.post('/signout',(data)=>{
        console.log('Sign out request response: ',data)
        if(data){
            window.location.href="/login"
        }
    })
}