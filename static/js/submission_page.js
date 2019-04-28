data = new FormData();
$(document).ready(()=>{
    $("#username").html("Hi, "+sessionStorage.getItem('user'))
    $("#lil_head").css('visibility','hidden')
        $("#file").on('change',(event)=>{

        $.each($('#file')[0].files, function(i, file) {
            data.append('file-'+i, file);
            
            $('.custom-file-label').html(file.name);
            
        });
        
    })
    $("#sub").on('click',(e)=>{
        e.preventDefault();
         data.set("courseid",$("#courseid").val())
         data.set("ass_name",$("#assname").val())

         console.log('Sending: ',data)
        $.post({
            url: '/postme',
            type: 'POST',
            data: data,
            cache: false,
            dataType: 'json',
            processData: false, // Don't process the files
            contentType: false, // Set content type to  false as jQuery will tell the server its a query string request
            success: function(data, textStatus, jqXHR){
                
                if(data=="True"){
                    $("#succ").css('display','block');
                    $("#fail").css('display','none');
                    $("#formcard").attr("class","card text-center border-success mb-3");
                }
                else{
                    $("#fail").css('display','block');
                    $("#succ").css('display','none');
                    $("#formcard").addClass("card text-center border-danger mb-3");
                }
            },
            fail:(xhr, textStatus, errorThrown)=>{
                console.log("Failed");
            }   
        })    
    })
    
})
