import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/views/movies/Home'
import About from '@/views/movies/About'
import Movie from '@/views/movies/Movie'
import Login from '@/views/accounts/Login'
import Profile from '@/views/accounts/Profile'
import Signup from '@/views/accounts/Signup'


Vue.use(VueRouter)

const routes = [
  {
    path: '/about',
    name: 'About',
    component: About
  },
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/movie/:movieId',
    name: 'Movie',
    component: Movie,
    props: true
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/profile',
    name: 'Profile',
    component: Profile,
  },
  {
    path: '/signup',
    name: 'Signup',
    component: Signup
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
