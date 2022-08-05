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