// File: app.js
const express = require('express');
const app = express();
const port = 3000;

app.get('/', (req, res) => {
  res.send('Hello from Express.js in a Docker Container!');
});

// Penting: Server harus listen di 0.0.0.0 agar bisa diakses dari luar container
app.listen(port, '0.0.0.0', () => {
  console.log(`Express app listening at http://0.0.0.0:${port}`);
});