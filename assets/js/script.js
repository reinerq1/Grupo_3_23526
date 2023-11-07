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
