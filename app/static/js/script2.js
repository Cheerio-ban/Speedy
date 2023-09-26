
const cus_info = document.querySelector('.customer_information')
const acc_info = document.querySelector('#account_details')
const cus_button = document.querySelector('#show_cus')
const acc_button = document.querySelector('#show_acc')
const logout = document.querySelector('#logout')
const pop_up = document.querySelector('.pop')
const cancel_pop = document.querySelector('#message_no')
const back = document.querySelector('#back')
const tab_p = document.querySelectorAll('.tab p:first-child')
const tab_span = document.querySelectorAll('.tab p:first-child span')
const tab_p2 = document.querySelectorAll('.tab p:nth-child(2)')
const select = document.querySelector('#manage_account select')


if (acc_button !== null && cus_button !== null && cus_info !== null && acc_info !== null){
    acc_button.addEventListener('click', () => {
        cus_info.style.display = 'none'
        acc_info.style.display = 'block';
        
    })
    cus_button.addEventListener('click', () => {
        acc_info.style.display = 'none';
        cus_info.style.display = 'block';
    })   
}

logout.addEventListener('click', () => {
    pop_up.style.display = 'flex';
})

if (cancel_pop !== null){
    cancel_pop.addEventListener('click', () => {
        pop_up.style.display = 'none';
    })
}


if (back !== null){
    back.addEventListener('click', ()=>{
        window.history.back()
    })    
}

if (tab_p !== null && tab_p2 !== null){
    tab_p[0].addEventListener('mouseover', ()=>{
        tab_p[0].style.color = 'rgb(13, 24, 61)'
        tab_p2[0].style.display = 'block'
        tab_span[0].innerHTML ='&#8744;'

    })
    tab_p[0].addEventListener('mouseleave', ()=>{
        tab_p[0].style.color = '#110526'
        tab_p2[0].style.display = 'none'
        tab_span[0].innerHTML ='&#62;'
    })
    tab_p[1].addEventListener('mouseover', ()=>{
        tab_p[1].style.color = 'rgb(13, 24, 61)'
        tab_p2[1].style.display = 'block'
        tab_span[1].innerHTML ='&#8744;'
    })
    tab_p[1].addEventListener('mouseleave', ()=>{
        tab_p[1].style.color = '#110526'
        tab_p2[1].style.display = 'none'
        tab_span[1].innerHTML ='&#62;'
    })
} 

let currentUrl = window.location.href
let searchParams = new URLSearchParams(window.location.search);

if (select !== null){
    select.addEventListener('change', ()=>{
        const option = select.options[select.selectedIndex]; 
        searchParams.set("id", option.value)
        const updated = searchParams.toString();
        updateURL = window.location.pathname + '?' + updated
        window.history.pushState({}, "", updateURL)
    })
}


