import Vue from 'vue'
import VueRouter from 'vue-router'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',

    component: () => import('../views/Landing.vue')
  },
  {
    path: '/signup',
    name: 'SignUp',
    
    component: () => import('../views/SignUp.vue')
  },
  {
    path: '/signin',
    name: 'SignIn',
    
    component: () => import('../views/SignIn.vue')
  },
  {
    path: '/home',
    name: 'HomePage',

    component: () => import('../views/Homepage.vue')
  },
  {
    path: '/matches',
    name: 'SignIn',
    
    component: () => import('../views/Matches.vue')
  },
  {
    path: '/profile',
    name: 'Profile',
    
    component: () => import('../views/profile.vue')
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
