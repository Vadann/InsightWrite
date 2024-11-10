//this is Java Script back end file for login_signup page
const wrapper = document.querySelector('.wrapper');
const loginLink = document.querySelector('.login-link');
const registerLink = document.querySelector('.register-link');
const btnPopup = document.querySelector('.btnLogin-popup');
const iconClose = document.querySelector('.icon-close');


//clicking sign-up and login function
registerLink.addEventListener('click', ()=> {
    wrapper.classList.add('active')
});

loginLink.addEventListener('click', ()=> {
    wrapper.classList.remove('active')
});

//clicking Login on navbar function to display login field
btnPopup.addEventListener('click', ()=> {
    wrapper.classList.add('active-popup')
});

//clicking on close button function for the middle field
iconClose.addEventListener('click', ()=> {
    wrapper.classList.remove('active-popup')
});
