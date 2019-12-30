import axios from 'axios'
import {Loading} from 'element-ui'

let loading;
let requestCount = 0

const service = axios.create({
  baseURL: 'http://47.98.155.211:8080',
  timeout: 8000
})

function showLoadingOnTable() {
  if(requestCount === 0) {
    loading = Loading.service({
      target: '.el-tabs',
      fullscreen: true,
      text: '正在加载'
    })
  }
  requestCount++;
}

function hideLoading() {
  if(requestCount <= 0) return;
  requestCount--;
  if(requestCount === 0)
    loading.close();
}

service.interceptors.request.use(
  config => {
    showLoadingOnTable();
    return config;
  },
  error => {
    hideLoading();
    return Promise.reject(error)
  }
)
service.interceptors.response.use(
  response => {
    hideLoading();
    return response.data;
  },
  error => {
    hideLoading();
    return Promise.reject(error)
  }
)

export default service

