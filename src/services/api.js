import axios from 'axios';

export default axios.create({
    baseURL: 'http://localhost:8000/',
    headers: {
        'Content-Type': 'application/octet-stream',
        'Access-Control-Allow-Headers': '*',
    },
});