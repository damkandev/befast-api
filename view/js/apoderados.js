function updateTable() {
  $.ajax({
    url: "http://localhost:8000/api/apoderados",
    type: "GET",
    contentType: "application/json ; charset=utf8",
    dataType: "json",
    success: function (response) {
      var tabla = $("#myTable > tbody:last-child");
      tabla.empty();
      response.forEach((apoderados) => {
        var id = apoderados.idapoderado;
        var nombres = apoderados.nombres;
        var apellido_p = apoderados.apellido_p;
        var telefonos = apoderados.telefono;
        var fila =
          '<tr class="fila">' +
          '<td class="id">' +
          id +
          "</td>" +
          "<td>" +
          nombres +
          "</td>" +
          "<td>" +
          apellido_p +
          "</td>" +
          "<td>" +
          telefonos +
          "</td>" +
          '<td><button class="btn btn-success btn-ver" onclick="btnVer()"><i class="fas fa-eye"></i> Ver más</button></td>' +
          "<tr>";
        tabla.append(fila);
      });
    },
  });
}

updateTable();

$("#crearEstudianteBtn").click(async () => {
  var nombres = $("#nombres").val();
  var apellido_p = $("#apellido_p").val();
  var apellido_m = $("#apellido_m").val();
  var rut = $("#rutcrear").val();
  var telefono = $("#telefono").val();

  var datos = {
    nombres: nombres,
    apellido_p: apellido_p,
    apellido_m: apellido_m,
    rut: rut,
    telefono: telefono,
  };
  var response = await $.ajax({
    url: "http://localhost:8000/api/apoderado/",
    type: "POST",
    contentType: "application/json; charset=utf8",
    data: JSON.stringify(datos),
  });

  console.log(response);

  updateTable();
  {
    console.error(error);
  }
});

function btnVer() {
  var button = event.target;
  var row = button.closest("tr");
  var idElement = row.querySelector(".id");
  var id = idElement.textContent;

  $.ajax({
    url: `http://localhost:8000/api/apoderado/${id}`,
    type: "GET",
    contentType: "application/json ; charset=utf8",
    dataType: "json",
    success: (response) => {
      localStorage.setItem("idapoderado", response.idapoderado);

      $(".ficha").removeClass("hide");
      function updateFicha() {
        $("#nombre-apoderado").html(
          response.nombres +
            " " +
            response.apellido_p +
            " " +
            response.apellido_m
        );
        $("#rut-apoderado").html(response.rut);
        $("#contacto-apoderado").html(response.telefono);
      }
      updateFicha();
    },
  });
}

function btnEditarModal() {
  var id = localStorage.getItem("idapoderado");
  $("#modalEditar").modal("show");
  function datosModal() {
    $.ajax({
      url: `http://localhost:8000/api/apoderado/${id}`,
      type: "GET",
      contentType: "application/json ; charset=utf8",
      dataType: "json",
      success: (response) => {
        $("#ed_nombres").val(response.nombres);
        $("#ed_apellido_p").val(response.apellido_p);
        $("#ed_apellido_m").val(response.apellido_m);
        $("#ed_rutcrear").val(response.rut);
        $("#ed_telefono").val(response.telefono);
      },
    });
  }

  datosModal();

  $("#editarBtn").click(async () => {
    var nombres = $("#ed_nombres").val();
    var apellido_p = $("#ed_apellido_p").val();
    var apellido_m = $("#ed_apellido_m").val();
    var rut = $("#ed_rutcrear").val();
    var telefono = $("#ed_telefono").val();

    var datos = {
      nombres: nombres,
      apellido_p: apellido_p,
      apellido_m: apellido_m,
      rut: rut,
      telefono: telefono,
      id: id,
    };
    var response = await $.ajax({
      url: `http://localhost:8000/api/apoderado/${id}`,
      type: "PUT",
      contentType: "application/json; charset=utf8",
      data: JSON.stringify(datos),
    });

    console.log(response);

    updateTable();
  });

  function btnBorrar() {
    var id = localStorage.getItem("idapoderado");

    var datos = {
      id: id,
    };

    $.ajax({
      url: `http://127.0.0.1:8000/api/apoderado/${id}`,
      type: "DELETE",
      data: JSON.stringify(datos),
      contentType: "application/json ; charset=utf8",
      dataType: "json",
      success: (response) => {
        updateTable();
      },
    });
  }
}
