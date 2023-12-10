const URL = 'http://localhost:4000';
const clientesTable = document.getElementById("clientesTable");

// Realizar la solicitud al servidor para obtener la lista de clientes
fetch(URL + "/clientes")
    .then(response => response.json())
    .then(clientes => {
        let html = '';

        clientes.forEach(element => {
            html = html + `<tr>
                <td>${element[0]}</td>
                <td>${element[1]}</td>
                <td>${element[2]}</td>
                <td>${element[3]}</td>
                <td>${element[4]}</td>
            </tr>`;
        });

        document.getElementById('clientesTable').innerHTML = html;
    })