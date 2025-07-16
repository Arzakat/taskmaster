const express = require('express');
const app = express();
const port = 3000;

const inmuebles = [
    { id: 1, direccion: "Calle 123", precio: 150000 },
    { id: 2, direccion: "Carrera 45", precio: 200000 },
];

app.get('/', (req, res) => {
    res.send("¡Bienvenido a la API de Inmuebles!");
});

app.get('/inmuebles', (req, res) => {
    res.json(inmuebles);
});

app.listen(port, () => {
    console.log(`Servidor escuchando en http://localhost:${port}`);
});