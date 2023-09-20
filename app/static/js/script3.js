const user = document.getElementsByClassName('user')
const next = document.querySelector('#next')
const previous = document.querySelector('#previous')

let index=0;
let i = 0;
next.addEventListener('click', ()=>{
    if (index < user.length){
        user[index+1].style.display = 'block'
        user[index].style.display = "none"
        index += 1;
    }
})

previous.addEventListener('click', ()=>{
    if (index >= 1){
        user[index].style.display = 'none'
        user[index-1].style.display = "block"
        index -= 1;
    }
})

