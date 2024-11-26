const express = require('express');
const cors = require('cors');
const dotenv = require('dotenv');

dotenv.config();

const app = express();
const PORT = 5000;

app.use(express.json());
app.use(cors());

app.use('/api/registration', require('./routes/confirmation.js'));

app.get('/', (req, res) => {
    res.send("Demo Day");
});

app.listen(PORT, () => {
    console.log("App listening at port", PORT);
});