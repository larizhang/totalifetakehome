import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import axios from "axios"

const client = axios.create({
	baseURL: "http://127.0.0.1:8000/",
	headers: {
		"Content-Type": "application/json"
	}
})

async function apiGetRequest(url) {
	try {
		const response = await client.get(url);
		return response.data;

	} catch (error) {
		console.error(error.message)
		throw new Error(error.message)
	}
}

async function apiPostRequest(url, data) {
	try {
		const response = await client.post(url, data);
		return response.data;

	} catch (error) {
		console.error(error.message)
		throw new Error(error.message)
	}
}

async function apiDeleteRequest(url) {
	try {
		const response = await client.delete(url);
		return response.data;

	} catch (error) {
		console.error(error.message)
		throw new Error(error.message)
	}
}

async function apiPutRequest(url, data) {
	try {
		const response = await client.put(url, data);
		return response.data;

	} catch (error) {
		console.error(error.message)
		throw new Error(error.message)
	}
}

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <div>
        <a href="https://vite.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>Vite + React</h1>
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
        <p>
          Edit <code>src/App.jsx</code> and save to test HMR
        </p>
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
    </>
  )
}

export default App
