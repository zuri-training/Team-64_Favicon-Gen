document.addEventListener('DOMContentLoaded', () => {

    const downloadBtn = document.getElementById("conv_download");
    const saveBtn1 = document.getElementById("conv_save1");
    const saveBtn2 = document.getElementById("conv_save2");

    const inputElement = document.getElementById("real-file");
    const uploadButton = document.getElementById("upload_button_hw");
    const dropZoneElement = document.getElementById("dropzone");

    dropZoneElement.addEventListener("click", (e) => {
      inputElement.click();
    });
  
    inputElement.addEventListener("change", (e) => {
      if (inputElement.files.length) {
        updateThumbnail(dropZoneElement, inputElement.files[0]);
        fileUploadedState();
      }
    });
  
    dropZoneElement.addEventListener("dragover", (e) => {
      e.preventDefault();
      dropZoneElement.classList.add("droparea--over");
    });
  
    ["dragleave", "dragend"].forEach((type) => {
      dropZoneElement.addEventListener(type, (e) => {
        dropZoneElement.classList.remove("droparea--over");
      });
    });
  
    dropZoneElement.addEventListener("drop", (e) => {
      e.preventDefault();
  
      if (e.dataTransfer.files.length) {
        inputElement.files = e.dataTransfer.files;
        updateThumbnail(dropZoneElement, e.dataTransfer.files[0]);
      }
  
      dropZoneElement.classList.remove("droparea--over");
      fileUploadedState();
    });

    function fileUploadedState() {
        uploadButton.setAttribute("class", "active");
        uploadButton.removeAttribute("disabled");
        downloadBtn.classList.remove("displayNone");
        saveBtn1.classList.remove("displayNone");
        saveBtn2.classList.remove("displayNone");
    }
    

});
  

  /**
   * Updates the thumbnail on a drop zone element.
   */
  function updateThumbnail(dropZoneElement, file) {
    let thumbnailElement = dropZoneElement.querySelector(".droparea__thumb");
  
    if (dropZoneElement.querySelector(".droparea .image")) {
      dropZoneElement.querySelector(".droparea .image").remove();
    }
    if (dropZoneElement.querySelector(".droparea .drag")) {
        dropZoneElement.querySelector(".droparea .drag").remove();
    }
  
    
    if (!thumbnailElement) {
      thumbnailElement = document.createElement("div");
      thumbnailElement.classList.add("droparea__thumb");
      dropZoneElement.appendChild(thumbnailElement);
    }
  
    thumbnailElement.dataset.label = file.name;
  
    
    if (file.type.startsWith("image/")) {
      const reader = new FileReader();
  
      reader.readAsDataURL(file);
      reader.onload = () => {
        thumbnailElement.style.backgroundImage = `url('${reader.result}')`;
      };
    } else {
      thumbnailElement.style.backgroundImage = null;
    }
  }