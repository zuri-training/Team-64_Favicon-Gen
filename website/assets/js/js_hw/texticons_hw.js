document.addEventListener('DOMContentLoaded', () => {

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

    function saveTexticonToDrafts(e, texticon_id) {
        e.preventDefault();        
        let form_data = new FormData();
        form_data.append("texticon_id", texticon_id);     
        $.ajaxSetup({
            headers:{
            'X-CSRFToken': getCookie("csrftoken")
            },
            beforeSend: function() {
                $('#sgenerator_download_save_buttons').hide();
                $('#loader_hw').removeClass("displayNone");
            },
            complete: function(){
                $('#sgenerator_download_save_buttons').show();
                $('#loader_hw').addClass("displayNone");
                },
        });
        console.log( "texticon_id : ", texticon_id);
        jQuery.ajax({
            url: "/save_texticon",
            type: "POST",
            data: form_data,
            contentType: false,
            processData: false,
            success: function (response) {
                saveDraftsLinkId = "saveDraft_" + response.texticonId;
                saveDraftsLink = document.getElementById(saveDraftsLinkId).children[0];
                saveDraftsLink.href = "javascript:void(0)";
                saveDraftsLink.innerText = "Saved";
                saveDraftsLink.style.opacity = "0.3";
                saveDraftsLink.style.cursor = "default";
                
            },
            error: function (response) {
                alert("Something went wrong");
            }
        });
    }


    
    document.querySelectorAll(".button-drafts").forEach((element, index)=>{
    
        if (element.id) {
            element.children[0].addEventListener("click", function(e) {   

                if (element.children[0].href != "javascript:void(0)") {
                    e.preventDefault();
                    texticonId = parseInt(element.id.split("_")[1]);
                    saveTexticonToDrafts(e, texticonId)
                }                
            })
        }

    })

})