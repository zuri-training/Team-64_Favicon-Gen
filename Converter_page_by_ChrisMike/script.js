//Navbar Active State
document.querySelectorAll('.nav-link').forEach(link => {
    if(link.href === window.location.href) {
        link.setAttribute('aria-current', 'page')
    }
})

//Hamburger-Menu nav-link Active State 
document.querySelectorAll('.mobile-nav-link').forEach(link => {
    if(link.href === window.location.href) {
        link.setAttribute('aria-current', 'page')
    }
}) 

//Hamburger-Menu Open & Close
const menu = document.querySelector('.menu-icon')
const mobile = document.querySelector('.mobile-menu')
const nav = document.querySelector('.navbar_ma')

menu.addEventListener('click', () => {
  menu.classList.toggle('active')
  mobile.classList.toggle('active')
  nav.classList.toggle('no-scroll')
})

// Drag and Drop function

const initApp = () => {
    const droparea = document.querySelector('.droparea');

    const active = () => droparea.classList.add("blue-border");

    const inactive = () => droparea.classList.remove("blue-border");

    const prevents = (e) => e.preventDefault();

    ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(evtName => {
        droparea.addEventListener(evtName, prevents);
    });

    ['dragenter', 'dragover'].forEach(evtName => {
        droparea.addEventListener(evtName, active);
    });

    ['dragleave', 'drop'].forEach(evtName => {
        droparea.addEventListener(evtName, inactive);
    });

    droparea.addEventListener('drop', handleDrop);

}

document.addEventListener("DOMContentLoaded", initApp);

const handleDrop = (e) => {
    const dt = e.dataTransfer;
    const files = dt.files;
    const fileArray = [...files];
}

//Upload Image and Browse function

const realFileBtn = document.getElementById("real-file");
const browseLink = document.getElementById("browse");
const customBtn = document.getElementById("custom-button");

customBtn.addEventListener("click", function() {
    realFileBtn.click()
})

browseLink.addEventListener("click", function() {
    realFileBtn.click()

})

//Upload Image button bgcolor change 
const btn = document.getElementById('custom-button');
btn.addEventListener('click', function onClick(event) {
    event.target.style.backgroundColor = "var(--blue)" ;
})
