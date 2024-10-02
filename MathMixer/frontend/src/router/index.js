import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../components/HomePage.vue'
import RegisterUsersPage from '@/components/RegisterUsersPage.vue'
import EnterPage from '@/components/EnterPage.vue'
import ProfilePage from '@/components/ProfilePage.vue'
import RegisterAgencyPage from '@/components/RegisterAgencyPage.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: HomePage
  },

  {
    path: '/register/users',
    name: 'RegisterUsers',
    component: RegisterUsersPage
  },

  {
    path: '/register/agency',
    name: 'RegisterAgency',
    component: RegisterAgencyPage
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