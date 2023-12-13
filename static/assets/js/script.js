document.addEventListener("DOMContentLoaded", function () {
  const botoMenu = document.querySelector("#menu_responsive");
  const navegador = document.querySelector("#div__navegador");
  const botonCerrarMenu = document.querySelector("#cerrar_menu_responsive");
 
  botoMenu.addEventListener("click", () => {
    navegador.classList.add("block");
    botoMenu.classList.add("none");
    botonCerrarMenu.classList.add("block");
  });
  botonCerrarMenu.addEventListener("click", () => {
    navegador.classList.remove("block");
    botoMenu.classList.remove("none");
    botonCerrarMenu.classList.remove("block");
  });
});

document.addEventListener("DOMContentLoaded", function () {
  var products = document.querySelectorAll(".product");

  setTimeout(function () {
      products.forEach(function (product) {
          product.style.opacity = "1";
          product.style.transform = "translateY(0)";
      });
  }, 500);
});

document.addEventListener("DOMContentLoaded", function () {
  const enviarForm = document.getElementById("enviar");
  const formulario = document.querySelector("#formularioCrearCuenta");
  function exibirAlerta() {
    const camposObligatorios = document.getElementsByClassName(
      "input__datos_personales"
    );
    let todosCamposLlenos = true;

    for (var i = 0; i < camposObligatorios.length; i++) {
      const valorCampo = camposObligatorios[i].value.trim();
      if (valorCampo === "") {
        todosCamposLlenos = false;
        break;
      }
    }

    if (todosCamposLlenos) {
      var msg =
        "Su cuenta fue creada correctamente! Haga click acá para seguir.";
      alert(msg);
      formulario.setAttribute("action", "/crearcuenta.html");

    } else {
      var msg =
        "Complete todos los campos para crear su cuenta. Haga click acá para seguir.";
      alert(msg);
    }
  }

  enviarForm.addEventListener("click", exibirAlerta);
});
