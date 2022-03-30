
const createUser   = 'http://127.0.0.1:5000/api/v1/user/create'
const updateUser   = 'http://127.0.0.1:5000/api/v1/user/update/      '
const readOneUser  = 'http://127.0.0.1:5000/api/v1/user/get/     '
const readAllUsers = 'http://127.0.0.1:5000/api/v1/user/get/allusers'
const deleteUser   = 'http://127.0.0.1:5000/api/v1/user/delete/   '


const createTask  = 'http://localhost:5000/api/v1/task/create/    '
const readTasks   = 'http://localhost:5000/api/v1/task/mytasks/    '
const updateTask  = 'http://127.0.0.1:5000/api/v1/task/update/   '
const deleteTask  = 'http://127.0.0.1:5000/api/v1/user/delete/2'

const btnEnviar = document.getElementById('submitNewUser')
const firstName = document.getElementById('first_name')
const lastName  = document.getElementById('last_name')
const email	    = document.getElementById('email')
const password  = document.getElementById('password')
const cPassword = document.getElementById('confirm_password')




// let leertexto = (e) =>{datos[e.target.id] = e.target.value;
// 	console.log(datos);
// }

const datos = btnEnviar.addEventListener('click', 
	 function showUser(e)  {
		const user ={
			first_name 		  : firstName.value,
			last_name  		  : lastName.value,
			email      		  : email.value,
			password   		  : password.value,
			confirm_password  : cPassword.value
		}; 
		e.preventDefault();
		
		let options = {
			method : ['POST'],
			mode: 'no-cors',
			body : JSON.stringify(user),
			headers:{ 'Content-Type': 'application/json'}
	}

try {postNewUser(createUser, options)} 
catch (error) {console.warn(error);}
})




const postNewUser = async (url, options)=>{
	await fetch(url, options )
	.then((response)=>response.json())
	

	console.log(options);

};














	


//firstName.addEventListener('input', leertexto);
//lastName.addEventListener ('input', leertexto);
//email.addEventListener    ('input', leertexto);
//password.addEventListener ('input', leertexto);
//cPassword.addEventListener('input', leertexto);
//btnEnviar.addEventListener('click', leertexto);




$(document).ready(function(){
	// Activate tooltip
	$('[data-toggle="tooltip"]').tooltip();
	
	// Select/Deselect checkboxes
	var checkbox = $('table tbody input[type="checkbox"]');
	$("#selectAll").click(function(){
		if(this.checked){
			checkbox.each(function(){
				this.checked = true;                        
			});
		} else{
			checkbox.each(function(){
				this.checked = false;                        
			});
		} 
	});
	checkbox.click(function(){
		if(!this.checked){
			$("#selectAll").prop("checked", false);
		}
	});
});


//
//
//<tr>
//	<td>
//		<span class="custom-checkbox">
//			<input type="checkbox" id="checkbox1" name="options[]" value="1">
//			<label for="checkbox1"></label>
//		</span>
//	</td>
//	<td>Thomas Hardy</td>
//	<td>thomashardy@mail.com</td>
//	<td>89 Chiaroscuro Rd, Portland, USA</td>
//	<td>(171) 555-2222</td>
//	<td>
//		<a href="#editEmployeeModal" class="edit" data-toggle="modal"><i class="material-icons" data-toggle="tooltip" title="Edit">&#xE254;</i></a>
//		<a href="#deleteEmployeeModal" class="delete" data-toggle="modal"><i class="material-icons" data-toggle="tooltip" title="Delete">&#xE872;</i></a>
//	</td>
//</tr>




const urlCRUD = 'http://127.0.0.1:5000/api/v1/'

const crearUsuario = async (usuario)=>{
    const resp = await fetch (createUser, {
        method :   'POST',
        body   :   JSON.stringify(usuario),
        headers:  {
            'Content-type': 'application/JSON'
        }
    })
    
    return  await resp.json();
    
}