async function realizarInicioSesion() {
  event.preventDefault()
  const correo = document.getElementById('email').value;
  const contrasena = document.getElementById('password').value;

  const response = await fetch('http://localhost:8000/api/login', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ correo, contrasena })
  });

  const data = await response.json();
  if (response.ok) {
    const token = data.token;
    if (token == "error") {
      alert("Contraseña o Correo Electronico incorrectos")
    } else {
      sessionStorage.setItem('token', token)
      window.location.href = 'home.html'
    }
    // 
    // 
  } else {
    // Error en el inicio de sesión. Mensaje de error en data.error.
    alert('Error en el inicio de sesión: ' + data.error);
  }
}