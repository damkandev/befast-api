function updateTable() {
  $.ajax({
    url: "http://localhost:8000/api/inspectores",
    type: "GET",
    contentType: "application/json ; charset=utf8",
    dataType: "json",
    success: function (response) {
      var tabla = $('#myTable > tbody:last-child')
      tabla.empty()
      response.forEach(inspectores => {
        var id = inspectores.id;
        var nombres = inspectores.nombres;
        var apellido_p = inspectores.apellido_p;
        var apellido_m = inspectores.apellido_m;
        var rut = inspectores.rut;
        var telefono = inspectores.telefono;
        var direccion = inspectores.direccion
        var fila = '<tr class="fila">' + '<td class="id">' + id + '</td>' + '<td>' + nombres + '</td>' + '<td>' + apellido_p + '</td>' + '<td>' + apellido_m + '</td>' + '<td>' + rut + '</td>' + '<td>' + telefono + '</td>' + '<td>' + direccion + '</td>' + '<td><button class="btn btn-success btn-ver" onclick="btnVer()"><i class="fas fa-eye"></i></button> <button onclick="btnEditarModal()" class="btn btn-warning btn-editar"><i class="fas fa-edit"></i></button> <button class="btn btn-danger btn-borrar" onclick="btnBorrar()"><i class="fas fa-trash"></i></button></td>' + '<tr>'
        tabla.append(fila)
      })
    }
  })
}

updateTable()


$('#crearInspectorBtn').click(() => {
  var nombres = $('#nombres').val()
  var apellido_p = $('#apellido_p').val()
  var apellido_m = $('#apellido_m').val()
  var rut = $('#rut').val()
  var telefono = $('#telefono').val()
  var direccion = $('#direccion').val()

  var datos = {
    "nombres": nombres,
    "apellido_p": apellido_p,
    "apellido_m": apellido_m,
    "rut": rut,
    "telefono": telefono,
    "direccion": direccion
  }

  $.ajax({
    url: "http://localhost:8000/api/inspector/",
    type: "POST",
    contentType: "application/json ; charset=utf8",
    data: JSON.stringify(datos),
    success: function (response) {
      updateTable()

    }
  })
})

function btnVer() {
  var button = event.target
  var row = button.closest('tr')
  var idElement = row.querySelector('.id')
  var id = idElement.textContent;


  $.ajax({
    url: `http://localhost:8000/api/inspector/${id}`,
    type: "GET",
    contentType: "application/json ; charset=utf8",
    dataType: "json",
    success: (response) => {
      $('#tituloModal').html(response.nombres);
      $('#contenidoModal').html(`<b>Nombres:</b>\n ${response.nombres}\n<b>Apellido Paterno:</b>\n ${response.apellido_p}\n<b>Apellido Materno:</b> \n${response.apellido_m}\n<b>RUT:</b> \n${response.rut}\n<b>Telefono:</b>\n ${response.telefono}\n<b>Dirección:</b>\n ${response.direccion}`);
      $('#modalVer').modal('show');
    }
  });
}

function btnEditarModal() {
  var button = event.target
  var row = button.closest('tr')
  var idElement = row.querySelector('.id')
  var id = idElement.textContent;
  $('#modalEditar').modal('show')
  $('#editarBtn').click(() => {
    console.log(id);
    var nombres = $('#Enombres').val()
    var apellido_p = $('#Eapellido_p').val()
    var apellido_m = $('#Eapellido_m').val()
    var rut = $('#Erut').val()
    var telefono = $('#Etelefono').val()
    var direccion = $('#Edireccion').val()
    var datos = {
      "id": id,
      "nombres": nombres,
      "apellido_p": apellido_p,
      "apellido_m": apellido_m,
      "rut": rut,
      "telefono": telefono,
      "direccion": direccion
    }

    $.ajax({
      url: `http://127.0.0.1:8000/api/inspector/${id}`,
      type: "PUT",
      contentType: "application/json ; charset=utf8",
      dataType: "json",
      data: JSON.stringify(datos),
      success: (response) => {
        $('#exampleModal').modal('show');
        updateTable()
      }
    });
  })
}

function btnBorrar() {
  var button = event.target
  var row = button.closest('tr')
  var idElement = row.querySelector('.id')
  var id = idElement.textContent;

  var datos = {
    "id": id
  }

  $.ajax({
    url: `http://127.0.0.1:8000/api/inspector/${id}`,
    type: "DELETE",
    data: JSON.stringify(datos),
    contentType: "application/json ; charset=utf8",
    dataType: "json",
    success: (response) => {
      updateTable()
    }
  });
}