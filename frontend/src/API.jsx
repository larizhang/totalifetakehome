import axios from "axios";

const client = axios.create({
    baseURL: "http://127.0.0.1:8000/",
    headers: {
        "Content-Type": "application/json"
    }
})

// wraps the get request to make it nicer for use in functions
async function apiGetRequest(url) {
    try {
        const response = await client.get(url);
        return response.data;

    } catch (error) {
        console.error(error.message)
        throw new Error(error.message)
    }
}

export {apiGetRequest};