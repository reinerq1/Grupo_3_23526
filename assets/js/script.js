document.addEventListener("DOMContentLoaded", function () {
  const botoMenu = document.querySelector("#menu_responsive");
  const navegador = document.querySelector("#div__navegador");
  const botonCerrarMenu = document.querySelector("#cerrar_menu_responsive");
  console.log(navegador.classList);
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