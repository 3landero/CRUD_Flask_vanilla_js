
const url = 'http://127.0.0.1:5000/api/v1/user/get/allusers'
const url_delete_user = 'http://127.0.0.1:5000/api/v1/user/delete/'
const url_create_user = 'http://localhost:5000/api/v1/user/create'
const url_edit_user = 'http://127.0.0.1:5000/api/v1/user/update/'

const contenedor = document.querySelector('tbody')
let resultados = ''
const modalUser = new bootstrap.Modal(document.getElementById('modalUser'))
const formUsuario = document.querySelector('form')
const firstName = document.getElementById('nombre')
const lastName = document.getElementById('apellido')
const email = document.getElementById('email')
const password = document.getElementById('password')
const passwordConfirm = document.getElementById('confirmPassword')
let opcion = ''

btnCrear.addEventListener('click', ()=>{
    firstName.value = '';
    lastName.value = '';
    email.value = '';
    password.value = '';
    passwordConfirm.value = '';
    modalUser.show();
    opcion = 'crear';

});

//Function that shows all the registers

const mostrar = (users)=> {
   // const {users} = data;
    users.forEach(user => {
        resultados += 
        `<tr>
        <td>${user.id} </td>
        <td>${user.nombre} </td>
        <td>${user.apellido} </td>
        <td>${user.email} </td>
        <td class = 'text-center'><a class = 'btnEditar btn btn-primary'> Editar </a> <a class = 'btnBorrar btn btn-danger'> Borrar </a> </td>
        </tr>`
    });
    contenedor.innerHTML =resultados ;    
}


//MOSTRAR TODOS LOS REGISTROS
const getAll =()=>{
    fetch(url)
    .then(response => response.json())
    .then(data=> {
        let {users} = data;
        mostrar(users)
    })
    .catch(error=> console.log(error));
}

getAll()



//---- EVENT HANDLER------

const on = (element, event, selector, handler)=>{
    element.addEventListener(event, e =>{
        if(e.target.closest(selector)){
            handler(e)
        }
    })
};

//------BORRAR REGISTRO
on(document, 'click', '.btnBorrar', e =>{
    const fila = e.target.parentNode.parentNode;
    const id = fila.firstElementChild.innerHTML;

    alertify.confirm("Esta seguro de borrar este registro?",
    function(){
      fetch(url_delete_user+id,{
          method: 'DELETE'
      })
      .then(res=>res.json())
      .then(()=> location.reload())
    },
    function(){
      alertify.error('Cancel');
    })

})



//-------------EDITAR------
let idForm = 0

on(document, 'click', '.btnEditar', e =>{
    const fila = e.target.parentNode.parentNode
    //const id = fila.firstElementChild.innerHTML
    idForm       = fila.children[0].innerHTML
    const nombreForm   = fila.children[1].innerHTML
    const apellidoForm = fila.children[2].innerHTML
    const emailForm    = fila.children[3].innerHTML
  // console.log(`ID: ${idForm} - Nombre: ${nombreForm} - Apellido: ${apellidoForm}- E-mail: ${emailForm} `);

firstName.value = nombreForm
lastName.value = apellidoForm
email.value = emailForm
//password = .values
//passwordConfirm = .values
opcion = 'editar';
modalUser.show();
});

//---crear editar usuario -----
formUsuario.addEventListener('submit', (e)=>{
    e.preventDefault();
    if(opcion === 'crear'){
        fetch(url_create_user, {
            method: 'POST',
            headers : {
                'Content-Type': 'application/json'
            },
            body : JSON.stringify({
                first_name: firstName.value,
                last_name : lastName.value,
                email: email.value,
                password  : password.value,
                confirm_password : passwordConfirm.value     
             })
        })
        .then(response => response.json())
        .then(data =>{
            const nuevoUser = [];
            nuevoUser.push(data);  
        })
        .then(response => location.reload())
        
        
        
    };
    if(opcion === 'editar'){
        console.log(idForm);
        fetch(url_edit_user + idForm, {
            method: 'PUT',
            headers : {
                'Content-Type': 'application/json'
            },
            body : JSON.stringify({
                first_name: firstName.value,
                last_name : lastName.value,
                email: email.value,
                password  : password.value,
                confirm_password : passwordConfirm.value     
             })
        })
        .then(response => response.json())
        .then(response => location.reload())
        
    };
    modalUser.hide()
    
    
    
});