function updateTable() {
  $.ajax({
    url: "http://localhost:8000/api/estudiantes",
    type: "GET",
    contentType: "application/json ; charset=utf8",
    dataType: "json",
    success: function (response) {
      var tabla = $("#myTable > tbody:last-child");
      tabla.empty();
      response.forEach((estudiantes) => {
        var id = estudiantes.id;
        var idcurso = estudiantes.idcurso;
        var nombres = estudiantes.nombres;
        var apellido_p = estudiantes.apellido_p;
        var apellido_m = estudiantes.apellido_m;
        var rut = estudiantes.rut;
        var telefono = estudiantes.telefono;
        var direccion = estudiantes.direccion;
        var fila =
          '<tr class="fila">' +
          '<td class="id">' +
          id +
          "</td>" +
          "<td>" +
          idcurso +
          "</td>" +
          "<td>" +
          nombres +
          "</td>" +
          "<td>" +
          apellido_p +
          "</td>" +
          '<td><button class="btn btn-success btn-ver" onclick="btnVer()"><i class="fas fa-eye"></i> Ver más</button></td>' +
          "<tr>";
        tabla.append(fila);
      });
    },
  });
}

updateTable();

$("#crearEstudianteBtn").click(() => {
  var nombres = $("#nombres").val();
  var apellido_p = $("#apellido_p").val();
  var apellido_m = $("#apellido_m").val();
  var rut = $("#rutcrear").val();
  var telefono = $("#telefono").val();
  var direccion = $("#direccion").val();

  var datos = {
    nombres: nombres,
    apellido_p: apellido_p,
    apellido_m: apellido_m,
    rut: rut,
    telefono: telefono,
    direccion: direccion,
  };

  console.log(datos);

  $.ajax({
    url: "http://localhost:8000/api/estudiante/",
    type: "POST",
    contentType: "application/json ; charset=utf8",
    data: JSON.stringify(datos),
    success: function (response) {
      updateTable();
    },
  });
});

function btnVer() {
  var button = event.target;
  var row = button.closest("tr");
  var idElement = row.querySelector(".id");
  var id = idElement.textContent;

  $.ajax({
    url: `http://localhost:8000/api/estudianteyapoderado/${id}`,
    type: "GET",
    contentType: "application/json ; charset=utf8",
    dataType: "json",
    success: (response) => {
      datos = { idestudiante: response.idestudiante };
      localStorage.setItem("lastReq", response.idestudiante);
      $(".ficha").removeClass("hide");
      function updateFicha() {
        $("#nombre-estudiante").html(
          response.estudiante_nombre +
            " " +
            response.estudiante_apellido_p +
            " " +
            response.estudiante_apellido_m
        );
        $("#rut-estudiante").html(response.rut);
        $("#contacto-estudiante").html(response.telefono);

        // Apoderados
        $("#nombre-apoderado-principal").html(
          response.apoderado_nombres +
            " " +
            response.apoderado_apellido_p +
            " " +
            response.apoderado_apellido_m
        );

        $("#telefono-apoderado-principal").html(
          "+56" + response.apoderado_telefono
        );

        $("#nombre-apoderado-suplente").html(
          response.apoderadosup_nombres +
            " " +
            response.apoderadosup_apellido_p +
            " " +
            response.apoderadosup_apellido_m
        );
        $("#telefono-apoderado-suplente").html(
          "+56" + response.apoderadosup_telefono
        );
      }
      updateFicha();
    },
  });
}

function btnEditarModal() {
  var button = event.target;
  var row = button.closest("tr");
  var idElement = row.querySelector(".id");
  var id = idElement.textContent;
  $("#modalEditar").modal("show");
  $("#editarBtn").click(() => {
    console.log(id);
    var nombres = $("#Enombres").val();
    var apellido_p = $("#Eapellido_p").val();
    var apellido_m = $("#Eapellido_m").val();
    var rut = $("#Erut").val();
    var telefono = $("#Etelefono").val();
    var direccion = $("#Edireccion").val();
    var datos = {
      id: id,
      nombres: nombres,
      apellido_p: apellido_p,
      apellido_m: apellido_m,
      rut: rut,
      telefono: telefono,
      direccion: direccion,
    };

    $.ajax({
      url: `http://127.0.0.1:8000/api/estudiante/${id}`,
      type: "PUT",
      contentType: "application/json ; charset=utf8",
      dataType: "json",
      data: JSON.stringify(datos),
      success: (response) => {
        $("#exampleModal").modal("show");
        updateTable();
      },
    });
  });
}

function btnBorrar() {
  var button = event.target;
  var row = button.closest("tr");
  var idElement = row.querySelector(".id");
  var id = idElement.textContent;

  var datos = {
    id: id,
  };

  $.ajax({
    url: `http://127.0.0.1:8000/api/estudiante/${id}`,
    type: "DELETE",
    data: JSON.stringify(datos),
    contentType: "application/json ; charset=utf8",
    dataType: "json",
    success: (response) => {
      updateTable();
    },
  });
}
