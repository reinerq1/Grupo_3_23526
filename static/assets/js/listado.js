const URL = "http://localhost:4000"



fetch(URL + '/administrador') // Obtener los productos
    .then(res => res.json()) // Convertir la respuesta a JSON
    .then(data => { // Mostrar los datos en consola
        let html = ''; // Variable para guardar el HTML
        console.log(data);

        data.forEach(element => {

            html = html + `<tr>
        <td>${element.Id_Cliente}</td>
        <td>${element.Nombre}</td>
        <td>${element.Email}</td>
        <td>${element.Genero}</td>
        <td>${element.Fecha_Nacimiento}</td>
        <td><a href="modificar.html?codigo=${element.Id_Cliente}">Modificar</a></td>
        <td><button class="alert" onclick="eliminar(${element.Id_Cliente});">Eliminar</button></td>
    </tr>`;
        });

        console.log(document.getElementById('administrador'));
        document.getElementById('administrador').innerHTML = html;
    })

    .catch (error => {
        console.error('Error en la solicitud:', error);
});