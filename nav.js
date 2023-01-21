const primaryNav = document.querySelector(".my-primary-navigation");
const navToggle = document.querySelector(".my-mobile-nav-toggle");

//bring the nav bar back in 
//opening the nav bar when clicked on button
navToggle.addEventListener("click", () => {
    const visibility = primaryNav.getAttribute("data-visible")
    
    if(visibility === "false"){
        primaryNav.setAttribute("data-visible", true);
        navToggle.setAttribute("aria-expanded",true);
    } else if(visibility === "true"){
        primaryNav.setAttribute("data-visible", false);
        navToggle.setAttribute("aria-expanded",false);
    }
});