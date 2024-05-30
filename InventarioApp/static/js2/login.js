function validarFormulario() {
    var nombre = document.getElementById("nombre-register").value.trim();
    var apellido = document.getElementById("apellido-register").value.trim();
    var email = document.getElementById("email-register").value.trim();
    var contrasenia = document.getElementById("contrasenia-register").value.trim();
    var confirmarContrasenia = document.getElementsByName("confirmarContrasenia-register").value.trim();

  
    if (nombre === "" || nombre.lenght >= 1 ) {
      alert("Por favor, ingrese su nombre completo.");
      return false;
    }

    if (apellido === "" || apellido.lenght >= 1) {
        alert("Por favor, ingrese su apellido completo.");
        return false;
      }
  
    if (!email.includes('@') || !email.includes('.com','.es','.cl')) {
        alert('El correo electrónico no es válido.');
        return false;
      }
  
    if (!contrasenia.test(contrasenia)) {
      alert("Por favor, ingrese un número de tarjeta válido.");
      return false;
    }
  
    alert("¡Reserva realizada con éxito!");
    return true;
  }