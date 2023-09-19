
/*Javascript for the speedy app"*/

/* Create account*/
const cancel = document.querySelector('#cancel')
const pop_up = document.querySelector('.pop')
const cancel_pop = document.querySelector('#message_no')

cancel.addEventListener('click', () => {
    pop_up.style.display = 'flex';
})

cancel_pop.addEventListener('click', () => {
    pop_up.style.display = 'none';
})




const cus_button = document.querySelector('#show_cus')
const p = document.querySelector('.title')

cus_button.addEventListener('click', () => {
    cus_info.style.display = 'none';
})


