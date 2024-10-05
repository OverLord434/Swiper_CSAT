import { createRouter, createWebHistory } from 'vue-router';
import HomePage from '../components/HomePage.vue';
import RegisterUsersPage from '@/components/RegisterUsersPage.vue';
import EnterPage from '@/components/EnterPage.vue';
import RegisterAgencyPage from '@/components/RegisterAgencyPage.vue';
import ProfileAgencyPage from '@/components/ProfileAgencyPage.vue';
import ProfileUsersPage from '@/components/ProfileUsersPage.vue';
import ProductDiscussionPage from '@/components/ProductDiscussionPage.vue';

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
    path: '/profile/agency',
    name: 'ProfileAgency',
    component: ProfileAgencyPage
  },
  {
    path: '/profile/users',
    name: 'ProfileUsers',
    component: ProfileUsersPage
  },
  {
    path: '/product',
    name: 'ProductDiscussion',
    component: ProductDiscussionPage
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

router.beforeEach((to, from, next) => {
  const token = localStorage.getItem('token');
  if (to.path === '/profile/agency' || to.path === '/profile/users') {
    if (!token) {
      next('/enter');
    } else {
      next();
    }
  } else if (to.path === '/enter' && token) {
    next('/profile/users');
  } else {
    next();
  }
});

export default router;