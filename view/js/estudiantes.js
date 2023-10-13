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

$(document).ready(() => {
  $.ajax({
    url: "http://127.0.0.1:8000/api/cursos/",
    type: "GET",
    contentType: "application/json ; charset=utf8",
    dataType: "json",
    success: function (response) {
      var opt = $("#idcurso");

      response.forEach((cursos) => {
        var id = cursos.idcurso;
        var nivel = cursos.nivel;
        var letra = cursos.letra;
        var opcion =
          '<option value="' + id + '">' + nivel + letra + "</option>";
        console.log(opcion);
        opt.append(opcion);
      });
    },
  });
});

$("#crearEstudianteBtn").click(async () => {
  var nombres = $("#nombres").val();
  var idcurso = $("#idcurso").val();
  var apellido_p = $("#apellido_p").val();
  var apellido_m = $("#apellido_m").val();
  var rut = $("#rutcrear").val();
  var telefono = $("#telefono").val();
  var direccion = $("#direccion").val();

  async function buscarRUT(sup, rut) {
    var url = sup
      ? `http://localhost:8000/api/apoderadosuprut/${rut}`
      : `http://localhost:8000/api/apoderadorut/${rut}`;

    console.log(rut)
    console.log(url);

    try {
      var response = await $.ajax({
        url: url,
        type: "GET",
        contentType: "application/json; charset=utf8",
        dataType: "json",
      });

      // Verifica si es apoderado (sup === false) para obtener idapoderado
      if (sup === false) {
        return response.idapoderado; // Cambia a idapoderado
      } else {
        return response.idapoderadosup; // Mantén idapoderadosup
      }
    } catch (error) {
      throw error;
    }
  }

  try {
    var idapoderadosup = await buscarRUT(
      true,
      parseInt(document.getElementById("rutapoderadosup").value)
    );
    var idapoderado = await buscarRUT(
      false,
      parseInt(document.getElementById("rutapoderado").value)
    );
    var avatar = $("#avatarestudiante").val();
    console.log(avatar, idapoderado, idapoderadosup);

    var datos = {
      nombres: nombres,
      idcurso: idcurso,
      apellido_p: apellido_p,
      apellido_m: apellido_m,
      rut: rut,
      telefono: telefono,
      direccion: direccion,
      idapoderado: idapoderado,
      idapoderadosup: idapoderadosup,
      avatar: avatar,
    };

    console.log(datos)
    
    var response = await $.ajax({
      url: "http://localhost:8000/api/estudiante/",
      type: "POST",
      contentType: "application/json; charset=utf8",
      data: JSON.stringify(datos),
    });

    console.log(response);

    updateTable();
  } catch (error) {
    console.error(error);
  }
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
      localStorage.setItem("idestudiante", response.idestudiante);
      localStorage.setItem("idapoderado", response.idapoderado);
      localStorage.setItem("idapoderadosup", response.idapoderadosup);

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

        $("#avatar").attr("src", response.avatar);
      }
      updateFicha();
    },
  });
}

function btnEditarModal() {
  var id = localStorage.getItem("idestudiante");
  $("#modalEditar").modal("show");
  function datosModal() {
    $.ajax({
      url: `http://localhost:8000/api/estudianteyapoderado/${id}`,
      type: "GET",
      contentType: "application/json ; charset=utf8",
      dataType: "json",
      success: (response) => {
        $("#ed_nombres").val(response.estudiante_nombre);
        $("#ed_idcurso").val(response.idcurso);
        $("#ed_apellido_p").val(response.estudiante_apellido_p);
        $("#ed_apellido_m").val(response.estudiante_apellido_m);
        $("#ed_rutcrear").val(response.estudiante_rut);
        $("#ed_telefono").val(response.estudiante_telefono);
        $("#ed_direccion").val(response.estudiante_direccion);
        $("#ed_rutapoderado").val(response.apoderado_rut);
        $("#ed_rutapoderadosup").val(response.apoderadosup_rut);
        $("#ed_avatarestudiante").val(response.avatar);
      },
    });
  }

  datosModal();

  $("#editarBtn").click(async () => {
    var nombres = $("#ed_nombres").val();
    var idcurso = $("#ed_idcurso").val();
    var apellido_p = $("#ed_apellido_p").val();
    var apellido_m = $("#ed_apellido_m").val();
    var rut = $("#ed_rutcrear").val();
    var telefono = $("#ed_telefono").val();
    var direccion = $("#ed_direccion").val();

    async function buscarRUT(sup, rut) {
      var url = sup
        ? `http://localhost:8000/api/apoderadosup/${rut}`
        : `http://localhost:8000/api/apoderado/${rut}`;

      console.log(url);

      try {
        var response = await $.ajax({
          url: url,
          type: "GET",
          contentType: "application/json; charset=utf8",
          dataType: "json",
        });

        // Verifica si es apoderado (sup === false) para obtener idapoderado
        if (sup === false) {
          return response.idapoderado; // Cambia a idapoderado
        } else {
          return response.idapoderadosup; // Mantén idapoderadosup
        }
      } catch (error) {
        throw error;
      }
    }

    try {
      var idapoderadosup = await buscarRUT(
        true,
        parseInt($("#ed_rutapoderadosup").val())
      );
      var idapoderado = await buscarRUT(
        false,
        parseInt($("#ed_rutapoderado").val())
      );
      var avatar = $("#ed_avatarestudiante").val();
      console.log(avatar);

      var datos = {
        nombres: nombres,
        idcurso: idcurso,
        apellido_p: apellido_p,
        apellido_m: apellido_m,
        rut: rut,
        telefono: telefono,
        direccion: direccion,
        idapoderado: idapoderado,
        idapoderadosup: idapoderadosup,
        avatar: avatar,
        id: id,
      };
      var response = await $.ajax({
        url: `http://localhost:8000/api/estudiante/${id}`,
        type: "PUT",
        contentType: "application/json; charset=utf8",
        data: JSON.stringify(datos),
      });

      console.log(response);

      updateTable();
    } catch (error) {
      console.error(error);
    }
  });

  function btnBorrar() {
    var id = localStorage.getItem("idestudiante");

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
}
