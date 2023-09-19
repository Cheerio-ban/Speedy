
const cus_info = document.querySelector('.customer_information')
const acc_info = document.querySelector('#account_details')
const cus_button = document.querySelector('#show_cus')
const acc_button = document.querySelector('#show_acc')



acc_button.addEventListener('click', () => {
    cus_info.style.display = 'none'
    acc_info.style.display = 'block';
    
})


cus_button.addEventListener('click', () => {
    acc_info.style.display = 'none';
    cus_info.style.display = 'block';
})