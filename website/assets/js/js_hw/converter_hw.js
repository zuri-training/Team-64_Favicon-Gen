document.addEventListener('DOMContentLoaded', () => {

    var current_username = document.getElementById("current_username");
    var convertFormId = document.getElementById("convertFormId");
    var fileInput = document.getElementById("real-file");
    var convertImgBtn = document.getElementById("conv_download");
    var saveImgBtn = document.getElementById("conv_save1");
    
    const downloadBtn = document.getElementById("conv_download");
    const saveBtn1 = document.getElementById("conv_save1");
    const saveBtn2 = document.getElementById("conv_save2");

    // var convertFormId = document.getElementById("convertFormId");
    // var fileInput = document.getElementById("myImgUploadInput");
    // var convertImgBtn = document.getElementById("convert_img_btn");
    // var saveImgBtn = document.getElementById("save_img_btn");
    // var convertImgBtnMsg = document.getElementById("convert_img_btn_msg");
    
    
    // function upload(url) {
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    function sendConvertRequest(e, saved_to_drafts) { 
        e.preventDefault();
        if(fileInput.files.length !== 0 ) {
            let uploaded_img = $('#real-file').get(0).files[0];
            var saved = saved_to_drafts;
            let form_data = new FormData();
            form_data.append("saved_to_drafts", saved);
            form_data.append("uploadedImg", uploaded_img);
            
            $.ajaxSetup({
                headers:{
                'X-CSRFToken': getCookie("csrftoken")
                },
                beforeSend: function() {
                    $('#conv_download').hide();
                    $('#conv_save1').hide();
                    $('#loader_hw').removeClass("displayNone");
                },
                complete: function(){
                    $('#conv_download').show();
                    $('#conv_save1').show();
                    // $('#upload_img_btn_group').show();
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
                    fileInput.value =null;
                    const dropZoneElement = document.getElementById("dropzone");
                    let thumbnailElement = dropZoneElement.querySelector(".droparea__thumb");
                    thumbnailElement.remove()
                    downloadBtn.classList.add("displayNone");
                    saveBtn1.classList.add("displayNone");
                    saveBtn2.classList.add("displayNone");

                    var installSectionLink = document.createElement('a');
                    installSectionLink.href = "#section_install_hw"
                    document.body.appendChild(installSectionLink);
                    installSectionLink.click();
                    // installSectionLink.remove();

                    var link = document.createElement('a');
                    if (!saved) {
                        link.href = window.URL.createObjectURL(response)      
                        link.download = 'ZuriconGen_Favicon_Generation.zip';
                    } else {
                        link.href = "/drafts"
                    } 
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
            // convertImgBtnMsg.innerHTML = "Insert a file first"
        }
    }

    
    convertImgBtn.addEventListener("click", function(e){
        if (current_username) {
            console.log("You clicked on convert")
            sendConvertRequest(e, 0)
        }
        
    })
    saveImgBtn.addEventListener("click", function(e){
        if (current_username) {
            console.log("You clicked on save")
            sendConvertRequest(e, 1)
        }
        
    })




})