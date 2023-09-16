
/*Javascript for the speedy app"*/

/* Create account*/
const firstname = document.getElementById('firstname')
const cancel = document.querySelector('#cancel')
const submit = document.querySelector('#submit')
const pop_up = document.querySelector('.pop')
const cancel_pop = document.querySelector('#message_no')
const button_message = document.querySelector('#pop button:last-child')
const p = document.getElementsByTagName('p')

cancel.addEventListener('click', () => {
    pop_up.style.display = 'flex';
})

cancel_pop.addEventListener('click', () => {
    pop_up.style.display = 'none';
})


