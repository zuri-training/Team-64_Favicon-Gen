  
document.addEventListener('DOMContentLoaded', () => {
    console.log("DRAFTS PAAGE LOADED")
    let close = document.getElementsByClassName("x");
    let select = document.getElementsByClassName("select_jol");
    let control = document.getElementsByClassName("favicon-control");
    const search = document.getElementsByName("search")[0];
    const folder = document.getElementsByClassName("folder");
    for (let i = 0; i < close.length; i++) {
        close[i].addEventListener("click", function() {
        control[i].style.display = "none";
    })
    }

    for (let i = 0; i < select.length; i++) {
        select[i].addEventListener("click", function() {
            select[0].classList.remove("active2");
            select[1].classList.remove("active2");
            select[i].classList.add("active2");
            // console.log(i);
            switch (i){
                
                case 0:
                // search.placeholder ="Search Downloads";
                document.getElementsByClassName("download")[0].classList.remove("hide");
                document.getElementsByClassName("drafts")[0].classList.add("hide");
                break;
                case 1:
                // search.placeholder = "Search Drafts";
                document.getElementsByClassName("download")[0].classList.add("hide");
                document.getElementsByClassName("drafts")[0].classList.remove("hide");
                // folder.forEach(element => {
                //   element.style.display = "none";
                // })
                break;
            }
        })
    }



    // /////////////////////////////////////////////////////////////

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

    function sendDeleteFaviconRequest(e, zip_id) {
        e.preventDefault();
        var zipId = zip_id;
        console.log("zip_id :",zip_id)
        // svgContent.setAttribute('value', texticonSvg);
        
        let form_data = new FormData();
        form_data.append("zip_id", zipId);    
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
        jQuery.ajax({
            url: "/delete_favicon",
            type: "POST",
            data: form_data,
            contentType: false,
            processData: false,
            xhrFields:{
                responseType: 'blob'
            },
            success: function (response) {
                console.log("deleted successfully")
                // var link = document.createElement('a');
                // link.href = "/drafts"               
                // document.body.appendChild(link);
                // link.click();
                
            },
            error: function (response) {
                alert("Something went wrong");
            }
        });
    }


    // downloadGenerationBtn.onclick = sendGenerationRequest(0) 
    // saveGenerationBtn.onclick = sendGenerationRequest(1) 

    // downloadGenerationBtn.addEventListener("click", function(e){
    //     sendGenerationRequest(e, 0)
    // })
    // saveGenerationBtn.addEventListener("click", function(e){
    //     sendGenerationRequest(e, 1)
    // })

})