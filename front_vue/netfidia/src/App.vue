<template>
  <div id="app">
    <div id="nav">
      <mdb-navbar expand="large" dark color="transparent">
        <mdb-navbar-brand href="#">
          <router-link :to="{ name: 'Home' }"><img 
          src="./assets/NETFIDIA logo.png" height="60" alt=""></router-link>
        </mdb-navbar-brand>
        <mdb-navbar-toggler>
          <mdb-navbar-nav right>
            <mdb-nav-item href="#" active><router-link :to="{ name: 'Home' }">Home</router-link></mdb-nav-item>
            <mdb-nav-item href="#"><router-link :to="{ name: 'About' }">About</router-link></mdb-nav-item>
            <mdb-nav-item href="#"><router-link :to="{ name: 'Logout' }">Logout</router-link></mdb-nav-item>
            <mdb-nav-item href="#"><router-link :to="{ name: 'Profile' }">Profile</router-link></mdb-nav-item>
            
            
              <mdb-dropdown tag="li" class="nav-item" dark color="transparent">
                <mdb-dropdown-toggle tag="a" navLink color="transparent" slot="toggle" waves-fixed><img 
            src="./assets/bellicon.png" height="40" alt=""></mdb-dropdown-toggle>
                <mdb-dropdown-menu color="transparent">
                  <mdb-dropdown-item color="transparent"><img 
          src="./assets/follow icon.png" height="40" alt="">Follow</mdb-dropdown-item>
                  <mdb-dropdown-item color="transparent"><img 
          src="./assets/like icon.png" height="40" alt="">Like</mdb-dropdown-item>
                  <mdb-dropdown-item color="transparent"><img 
          src="./assets/movie icon.png" height="40" alt="">For You</mdb-dropdown-item>
                </mdb-dropdown-menu>
              </mdb-dropdown>
            

          </mdb-navbar-nav>
        </mdb-navbar-toggler>
      </mdb-navbar>
    </div>

    <div v-if='login'>
      <router-link :to="{ name: 'Home' }">Home</router-link> | 
      <router-link :to="{ name: 'About' }">About</router-link> |
      <router-link :to="{ name: 'Profile' }">Profile</router-link> |
      <router-link @click.native="logout" to="#">Logout</router-link>
    </div>
    <div v-else>
      <router-link :to="{ name: 'Signup' }">Signup</router-link> |
      <router-link :to="{ name: 'Login' }">Login</router-link> 
    </div>
    <router-view @login="login = true"/>
  </div>
</template>

<script>
// import axios from 'axios'

import { mdbDropdown, mdbDropdownToggle, mdbDropdownMenu, mdbDropdownItem, mdbNavbar, mdbNavbarBrand, mdbNavbarToggler, mdbNavbarNav, mdbNavItem } from 'mdbvue';

// const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'App',
  components: {
    mdbNavbar,
    mdbNavbarBrand,
    mdbNavbarToggler,
    mdbNavbarNav,
    mdbNavItem,
    mdbDropdown,
    mdbDropdownToggle,
    mdbDropdownMenu,
    mdbDropdownItem
  },
  data: function () {
    return {
      login: false,
    }
  },
  methods: {
    logout: function () {
      localStorage.removeItem('user')
      this.login = false
      this.$router.push({ name: 'Login' })
    }
  },
  created: function () {
    if (localStorage.getItem('user')) {
      // const token = JSON.parse(localStorage.getItem('user')).token
      this.login = true
    }
    // axios.get(`${SERVER_URL}/reviews/movie-register`)
    //   .then(res => {
    //     console.log(res.data)
    //     this.$store.dispatch('getData', res.data)
    //   })
    //   .catch()
  },
}
</script>


<style>
@import url('https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap');

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
  background-color: transparent;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
  background-color: transparent;
}

#nav a.router-link-exact-active {
  color: #42b983;
  background-color: transparent;
}

#beforelogin {
  color: white
}
</style>
