let btns_text = document.querySelectorAll('#alpha')
let btn_shift = document.querySelector('.shift-alpha')
let btn_delete = document.querySelector('.delete-alpha')
//let btn_enter = document.getElementById('shift-alpha')
let chars_pass_field = []
let password_field = document.getElementById('pass')

btns_text.forEach(btn => {
    btn.addEventListener('click', () => {
        password_field.value += btn.innerText
        chars_pass = password_field.value.split('')
        console.log(chars_pass)
    })
})

btn_delete.addEventListener('click', () => {
    chars_pass_field.pop()
    console.log(chars_pass_field)
    password_field.value = chars_pass_field.join('')
})

btn_shift.addEventListener('click', () => {    
    btns_text.forEach(btn => {
        btn.classList.toggle('upper-alpha')
    })
})


