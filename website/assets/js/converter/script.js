
// Drag and Drop function

// const initApp = () => {
//     const droparea = document.querySelector('.droparea');

//     const active = () => droparea.classList.add("blue-border");

//     const inactive = () => droparea.classList.remove("blue-border");

//     const prevents = (e) => e.preventDefault();

//     ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(evtName => {
//         droparea.addEventListener(evtName, prevents);
//     });

//     ['dragenter', 'dragover'].forEach(evtName => {
//         droparea.addEventListener(evtName, active);
//     });

//     ['dragleave', 'drop'].forEach(evtName => {
//         droparea.addEventListener(evtName, inactive);
//     });

//     droparea.addEventListener("drop", handleDrop);

// }

// document.addEventListener("DOMContentLoaded", initApp);

// const handleDrop = (e) => {
//     const dt = e.dataTransfer;
//     const files = dt.files;
//     const fileArray = [...files];
//     console.log(files); // FileList
//     console.log(fileArray);
// } 


// //Upload Image function

// const realFileBtn = document.getElementById("real-file");
// const customBtn = document.getElementById("custom-button");

// customBtn.addEventListener("click", function() {
//     realFileBtn.click()
// })