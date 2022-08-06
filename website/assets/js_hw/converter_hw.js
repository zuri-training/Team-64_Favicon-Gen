document.addEventListener('DOMContentLoaded', () => {

    var convertFormId = document.getElementById("convertFormId");
    var fileInput = document.getElementById("myImgUploadInput");
    var uploadImgBtn = document.getElementById("upload_img_btn");
    var uploadImgBtnMsg = document.getElementById("upload_img_btn_msg");
    
    // function upload(url) {
        function getCookie(name) {
            let cookieValue = null;
            if (document.cookie && document.cookie !== '') {
                const cookies = document.cookie.split(';');
                for (let i = 0; i < cookies.length; i++) {
                    const cookie = cookies[i].trim();
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) === (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }

    uploadImgBtn.onclick = function (e) { 
        e.preventDefault();
        if(fileInput.files.length !== 0 ) {
            let uploaded_img = $('#myImgUploadInput').get(0).files[0];
            
            let form_data = new FormData();
            form_data.append("uploadedImg", uploaded_img);
            $.ajaxSetup({
                headers:{
                'X-CSRFToken': getCookie("csrftoken")
                },
                beforeSend: function() {
                    $('#upload_img_btn_group').hide();
                    $('#loader_hw').removeClass("displayNone");
                },
                complete: function(){
                    $('#upload_img_btn_group').show();
                    $('#loader_hw').addClass("displayNone");
                 },
            });
            jQuery.ajax({
                url: "/favicon_conversion",
                type: "POST",
                data: form_data,
                contentType: false,
                processData: false,
                xhrFields:{
                    responseType: 'blob'
                },
                success: function (response) {
                    var link = document.createElement('a');
                    link.href = window.URL.createObjectURL(response)
                    // link.href = response
                    // console.log(response)             
                    link.download = 'ZuriconGen_Favicon_Conversion.zip';
                    document.body.appendChild(link);
                    link.click();
                    
                },
                error: function (response) {
                    alert("Something went wrong")
                    // loading_btn.classList.add("d-none");
                    // upload_btn.classList.remove("d-none");
                }
            });
        } else {
            uploadImgBtnMsg.innerHTML = "Insert a file first"
        }
    }

    




})