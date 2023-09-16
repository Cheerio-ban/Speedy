
/*Javascript for the speedy app"*/

/* Create account*/
const create = document.getElementById('create')
const cancel = document.querySelector('#cancel')
const submit = document.querySelector('#submit')
const pop_up = document.querySelector('#pop')
const cancel_pop = document.querySelector('#message_cancel')
const button_message = document.querySelector('#pop button:lastchild')
const p = document.getElementsByTagName('p')

cancel.addEventListener('click', ()=>{

})

document.getElementById('create').addEventListener('click', ()=>{
    p.style.color = 'blue';
})

document.getElementsByClassName('input').addEventListener('focus', ()=>{
    p.style.color = 'blue';
})
