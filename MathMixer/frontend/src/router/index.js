import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../components/HomePage.vue'
import RegisterUsersPage from '@/components/RegisterUsersPage.vue'
import EnterPage from '@/components/EnterPage.vue'
import ProfilePage from '@/components/ProfilePage.vue'

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

router.beforeEach((to, from, next) => {
  const token = localStorage.getItem('token');
  if (to.path === '/profile/agency' || to.path === '/profile/users') {
    if (!token) {
      next('/enter');
    } else {
      next();
    }
  } else if (to.path === '/enter' && token) {
    next('/profile');
  } else {
    next();
  }
});

export default router