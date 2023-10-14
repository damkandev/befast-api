function secondsToString(seconds) {
  var hour = Math.floor(seconds / 3600);
  hour = (hour < 10)? '0' + hour : hour;
  var minute = Math.floor((seconds / 60) % 60);
  minute = (minute < 10)? '0' + minute : minute;
  var second = seconds % 60;
  second = (second < 10)? '0' + second : second;
  return hour + ':' + minute;
}


function updateTable(search, termino) {
  if(search === false){
    $.ajax({
      url: "http://localhost:8000/api/atrasos",
      type: "GET",
      contentType: "application/json ; charset=utf8",
      dataType: "json",
      success: function (response) {
        $.each(response, function (index, item) {
          var card = `<div class="col-md-4">
          <div class="card mb-4" tilt>
            <div  class="card-body atraso">
              <div class="top">
                <div class="left">
                  <img src="${item.avatar}" alt="">
                </div>
                <div class="right"> 
                  <p class="atitle">Nombre Alumno</p>
                  <p class="anombre">${item.nombres} ${item.apellido_p} ${item.apellido_m}</p>
                  <p class="info">Curso: ${item.nivel + item.letra} | RUT: ${item.rut}</p>
                </div>
              </div>
              <div class="bottom">
                <p class="infob"><b>Fecha:</b> ${item.fecha} <b>Hora Entrada:</b> ${secondsToString(item.hora)} </p>
                <div class="buttons">
                  <button class="print"><img src="../images/impresora.svg" alt=""></button>
                </div>
              </div>
            </div>
          </div>
        </div>`;
          $("#card-container-cards").append(card);
          VanillaTilt.init(document.querySelector(".atraso"), {
            max: 25,
            speed: 400,
            glare: true,
            "max-glare":0.8
          });
    
          VanillaTilt.init(document.querySelectorAll(".atraso"));
        });
      },
    });
  } else if(search === true) {
    $.ajax({
      url: `http://localhost:8000/api/atraso/${termino}`,
      type: "GET",
      contentType: "application/json ; charset=utf8",
      dataType: "json",
      success: function (response) {
        $.each(response, function (index, item) {
          var card = `<div class="col-md-4">
          <div class="card mb-4" tilt>
            <div  class="card-body atraso">
              <div class="top">
                <div class="left">
                  <img src="${item.avatar}" alt="">
                </div>
                <div class="right"> 
                  <p class="atitle">Nombre Alumno</p>
                  <p class="anombre">${item.nombres} ${item.apellido_p} ${item.apellido_m}</p>
                  <p class="info">Curso: ${item.nivel + item.letra} | RUT: ${item.rut}</p>
                </div>
              </div>
              <div class="bottom">
                <p class="infob"><b>Fecha:</b> ${item.fecha} <b>Hora Entrada:</b> ${secondsToString(item.hora)} </p>
                <div class="buttons">
                  <button class="print"><img src="../images/impresora.svg" alt=""></button>
                </div>
              </div>
            </div>
          </div>
        </div>`;
          $("#card-container-cards").append(card);
          VanillaTilt.init(document.querySelector(".atraso"), {
            max: 25,
            speed: 400,
            glare: true,
            "max-glare":0.8
          });
    
          VanillaTilt.init(document.querySelectorAll(".atraso"));
        });
      },
    });
    
  }
  
}

updateTable(false, "")

document.addEventListener("DOMContentLoaded", function(){
  function captarInput(){
    input = document.getElementById("searachinpt")
    input.addEventListener("keyup", function(event){
      var valor = input.value;
      if(!valor){
        document.getElementById("card-container-cards").innerHTML = "";
        updateTable(false, "damian");
      } else {
        document.getElementById("card-container-cards").innerHTML = "";
        updateTable(true, valor);

      }
    })
    
  }

  captarInput()
})




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
      url: `http://localhost:8000/api/atraso/${id}`,
      type: "PUT",
      contentType: "application/json; charset=utf8",
      data: JSON.stringify(datos),
    });

    location.reload();
  });
}
