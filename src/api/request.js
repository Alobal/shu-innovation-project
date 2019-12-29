import axios from 'axios'

const service = axios.create({
  baseURL: 'http://47.98.155.211:8080',
  timeout: 8000
})

export default service

