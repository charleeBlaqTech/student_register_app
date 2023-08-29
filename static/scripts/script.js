const tutorForm = document.querySelector('#form-for-tutor')
const studentForm = document.querySelector('#form-for-student')
const asideBarNav = document.querySelector('#aside-nav-ul')


asideBarNav.addEventListener('click', (event)=>{
    event.preventDefault();
    
        if(event.target.getAttribute("id") === "add-new-std"){
            studentForm.classList.toggle("showForms");
            tutorForm.classList.remove('showForms');
        }else if(event.target.getAttribute('id') === "add-new-tut"){
            tutorForm.classList.toggle("showForms");
            studentForm.classList.remove('showForms');
        }
          

})
