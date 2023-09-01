// Verificar si hay un token almacenado en sessionStorage
const token = sessionStorage.getItem('token');

function checkToken() {
  if (!token) {
    document.addEventListener('DOMContentLoaded', function (event) {
      window.location.href = "./index.html"
    })
  }
}

checkToken()

document.getElementById('cerrarSesion').addEventListener('click', () => {
  checkToken()
  sessionStorage.clear()
})