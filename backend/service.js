const express = require('express');
const axios = require('axios');
const path = require('path');

const app = express();
app.use(express.json());
app.use(express.static(path.join(__dirname, 'public')));

app.post('/summarize', async (req, res) => {
    const { url } = req.body;
    try {
        const response = await axios.post('http://localhost:5001/summarize', { url });
        res.json(response.data);
    } catch (err) {
        console.error(err.message);
        res.status(500).json({ error: 'Failed to summarize article' });
    }
});

app.listen(3000, () => console.log('Node.js server running on http://localhost:3000'));
