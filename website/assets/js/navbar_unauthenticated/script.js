document.addEventListener('DOMContentLoaded', () => {
    // Copy to clipboard
    let copyToClipboardBtn = document.getElementById("copyToClipboardBtn");
    if (copyToClipboardBtn) {
        copyToClipboardBtn.addEventListener("click", (e) => {
            copyToClipboardFct();
        });
    }
    


    let authUserInitial = document.getElementById("authUserInitial");
    if (authUserInitial)
    {
        authUserInitial.innerText = authUserInitial.innerText.charAt(0)
    }
    
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
    // const menu = document.querySelector('.menu-icon')
    const menu = document.querySelector('.triple_bar_menu')

    const mobile = document.querySelector('.mobile-menu')
    const nav = document.querySelector('.navbar_ma')

    menu.addEventListener('click', () => {
    menu.classList.toggle('active')
    mobile.classList.toggle('active')
    //   nav.classList.toggle('no-scroll')
    })

    /**
     * Copy to clipboard
     */
    function copyToClipboardFct() {
        /* Get the text field */
        var copyText = document.getElementById("htmlCodeText");
      
        var textArea = document.createElement("textarea");
        textArea.value = copyText.innerText;
        // Avoid scrolling to bottom
        textArea.style.top = "0";
        textArea.style.left = "0";
        textArea.style.position = "fixed";
        
        document.body.appendChild(textArea);
        textArea.focus();
        textArea.select();

        try {
            var successful = document.execCommand('copy');
            var msg = successful ? 'successful' : 'unsuccessful';
            // console.log('Fallback: Copying text command was ' + msg);
          } catch (err) {
            // console.error('Fallback: Oops, unable to copy', err);
          }
        
        document.body.removeChild(textArea);
        /* Select the text field */
        // copyText.select();
        // copyText.setSelectionRange(0, 99999); /* For mobile devices */
      
         /* Copy the text inside the text field */
        // navigator.clipboard.writeText(copyText.innerHTML);
      
        /* Alert the copied text */
        // alert("Copied the text: " + copyText.innerHTML);
    }
      
})
