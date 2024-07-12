//function showLoadingSpinner(event) {
//    event.preventDefault();  // Evita la acción predeterminada del evento
//    document.getElementById('loading-spinner').style.display = 'block';
//   setTimeout(() => {
//        window.location.href = event.target.href;
//    }, 2000); // Retraso en milisegundos (por ejemplo, 2000ms = 2 segundos)
//}


function showLoadingSpinner(event) {
    event.preventDefault();  // Evita la acción predeterminada del evento
    //const spinner = document.getElementById('loading-spinner');
    const successMessage = document.getElementById('success-message');
    const successMessage1 = document.getElementById('success-message1');
    const successMessage2 = document.getElementById('success-message2'); // Nombre corregido para el tercer mensaje

    //spinner.style.display = 'block';
    successMessage.style.display = 'block';
    successMessage1.style.display = 'none';
    successMessage2.style.display = 'none';

    setTimeout(() => {
        //spinner.style.display = 'none';
        successMessage.style.display = 'none';
        successMessage1.style.display = 'block';
        
        //setTimeout(() => {
            //successMessage.style.display = 'none';
            //successMessage1.style.display = 'block';

            setTimeout(() => {
                successMessage1.style.display = 'none';
                successMessage2.style.display = 'block';

                setTimeout(() => {
                    // Simulamos la redirección a una página de pago
                    window.location.href = event.target.href;
                }, 1500); // Muestra el tercer mensaje por 3 segundos antes de redirigir
            }, 1500); // Duración antes de mostrar el tercer mensaje
        //}, 1500); // Duración antes de mostrar el segundo mensaje
    }, 2000); // Duración del spinner
}


// function verificarContrasenas() {
//     var password1 = document.getElementById("password1").value;
//     var password2 = document.getElementById("password2").value;

//     if (password1 !== password2) {
//         document.getElementById("password1").focus();
//         return false;  // Evita que se envíe el formulario si las contraseñas no coinciden
//     }
//     return true;  // Permite que se envíe el formulario si las contraseñas coinciden
// }


// // Agregar el evento onSubmit al formulario para llamar a la función verificarContrasenas
// document.getElementById("validacion").onsubmit = function() {
//     verificarContrasenas();
// };