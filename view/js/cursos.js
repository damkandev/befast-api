function updateTable() {
  $.ajax({
    url: "http://localhost:8000/api/cursos",
    type: "GET",
    contentType: "application/json ; charset=utf8",
    dataType: "json",
    success: function (response) {
      $.each(response, function (index, item) {
        var card = `<div class="col-md-4">
        <div class="card mb-4">
          <img src="../images/curso_banner.jpg" class="card-img-top" alt="...">
          <div class="card-body">
            <h5 class="card-title">${item.nivel}${item.letra}</spanid>
            </h5>
            <p class="card-text"><span>ID: <span id="idcurso">${item.idcurso}</span><br><span id="nivelcurso">Nivel: ${item.nivel}</span><br><span
                id="letracurso">Letra: ${item.letra}</span>
            </p>
            <button class="btn btn-primary" onclick="btnEditarModal()">Editar</button>
            <button class="btn btn-secondary btn-borrar" onclick="btnBorrar()">Eliminar</button>
          </div>
        </div>
      </div>`;
        $("#card-container").append(card);
      });
    },
  });
}

updateTable();

$("#crearEstudianteBtn").click(async () => {
  var nivel = $("#nivel").val();
  var letra = $("#letra").val();

  var datos = {
    nivel: nivel,
    letra: letra,
  };
  var response = await $.ajax({
    url: "http://localhost:8000/api/cursos/",
    type: "POST",
    contentType: "application/json; charset=utf8",
    data: JSON.stringify(datos),
  });

  console.log(response);

  updateTable();
});

function btnVer() {
  var button = event.target;
  var _id = $(this).closest("#idcurso");
  var id = _id.find;

  console.log(id);

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
  var cardElement = $(event.target).closest(".card");
  var idcursoElement = cardElement.find("#idcurso");
  var id = parseInt(idcursoElement.text());

  $("#modalEditar").modal("show");
  function datosModal() {
    $.ajax({
      url: `http://localhost:8000/api/curso/${id}`,
      type: "GET",
      contentType: "application/json ; charset=utf8",
      dataType: "json",
      success: (response) => {
        $("#ed_nivel").val(response.nivel);
        $("#ed_letra").val(response.letra);
      },
    });
  }

  datosModal();

  $("#editarBtn").click(async () => {
    var nivel = $("#ed_nivel").val();
    var letra = $("#ed_letra").val();
    var idcurso = id;

    var datos = {
      nivel: nivel,
      letra: letra,
      idcurso: idcurso,
    };
    var response = await $.ajax({
      url: `http://localhost:8000/api/curso/${id}`,
      type: "PUT",
      contentType: "application/json; charset=utf8",
      data: JSON.stringify(datos),
    });

    location.reload();
  });
}
