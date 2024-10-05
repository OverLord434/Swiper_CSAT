import './assets/main.css'
import 'swiper/swiper-bundle.css'
import axios from 'axios';
import router from './router/index.js'
import { createApp } from 'vue'
import App from './App.vue'

// Настройка интерсептора для Axios
axios.interceptors.request.use(config => {
  const token = localStorage.getItem('token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
}, error => {
  return Promise.reject(error);
});

createApp(App).use(router).mount('#app')
