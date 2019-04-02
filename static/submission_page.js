data = new FormData();
$(document).ready(()=>{
    
    $("#file").on('change',(event)=>{

        $.each($('#file')[0].files, function(i, file) {
            data.append('file-'+i, file);
            console.log(file)
            $('.custom-file-label').html(file.name);
            
        });
        
    })
    $("#sub").on('click',(e)=>{
        e.preventDefault();
        //console.log("aaaa   ")
         //data.append("courseid","challehannu");
         data.append("courseid",$("#courseid").val())
         data.append("ass_name",$("#assname").val())

         console.log(data)
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
                }
                else{
                    $("#fail").css('display','block');
                    $("#succ").css('display','none');
                }
            },
            fail:(xhr, textStatus, errorThrown)=>{
                console.log("adfklyjhcag");
            }   
        })    
    })
    
})
