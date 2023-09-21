const accounts = document.getElementsByClassName('acc')
const next = document.querySelector('#next')
const previous = document.querySelector('#previous')
const amount = document.querySelector('#amount_in')
const am_err = document.querySelector('#err')
const acc_num = document.querySelector('#acc_no')
const no_err = document.querySelector('#no_err')

let index=0;
let i = 0;

let currentUrl = window.location.href
let searchParams = new URLSearchParams(window.location.search);

const id="id"
let arg;

next.addEventListener('click', ()=>{
    if (index < accounts.length){
        accounts[index+1].style.display = 'block'
        accounts[index].style.display = "none"
        amount.value = ""
        if (document.contains(am_err)){
            am_err.innerHTML = ""
        }
        arg = accounts[index+1].getAttribute("id") 
        searchParams.set(id, arg)
        const updated = searchParams.toString();
        const updateURL = window.location.pathname + '?' + updated
        window.history.pushState({}, "", updateURL)
        index += 1;
    }

})

previous.addEventListener('click', ()=>{
    if (index >= 1){
        accounts[index].style.display = 'none'
        accounts[index-1].style.display = "block"
        
        amount.value = ''
        if (document.contains(am_err)){
            am_err.innerHTML = ""
        }
        arg = accounts[index-1].getAttribute("id")
        searchParams.set(id, arg)
        const updated = searchParams.toString();
        const updateURL = window.location.pathname + '?' + updated
        window.history.pushState({}, "", updateURL)
        index -= 1;
    }
})

amount.addEventListener('input', (event)=>{
    if (Number(event.target.value) < 50){
        event.target.style.color = 'red';
    }
    else{
        event.target.style.color = 'black';
    }
})


