import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../components/HomePage.vue'
import RegisterPage from '@/components/RegisterPage.vue'
import EnterPage from '@/components/EnterPage.vue'
import ProfilePage from '@/components/ProfilePage.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: HomePage
  },

  {
    path: '/register',
    name: 'Register',
    component: RegisterPage
  },

  {
    path: '/enter',
    name: 'Enter',
    component: EnterPage
  },

  {
    path: '/profile',
    name: 'Profile',
    component: ProfilePage
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router