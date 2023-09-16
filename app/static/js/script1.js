
/*Javascript for the speedy app"*/

/* Create account*/
const create = document.getElementById('create')
const firstname = document.getElementById('firstname')
const cancel = document.querySelector('#cancel')
const submit = document.querySelector('#submit')
const pop_up = document.querySelector('#pop')
const cancel_pop = document.querySelector('#message_cancel')
const button_message = document.querySelector('#pop button:last-child')
const p = document.getElementsByTagName('p')

create.addEventListener('click', () => {
    console.log('created');
})

firstname.addEventListener('click', () => {
    console.log('clicked')
})

cancel.addEventListener('click', ()=>{

})

// document.getElementById('create').addEventListener('click', ()=>{
//     p.style.color = 'blue';
// })

// document.getElementsByClassName('input').addEventListener('focus', ()=>{
//     p.style.color = 'blue';
// })
