<template>
  <div>
    <h1>Login</h1><br>
    <div class="loginForm">
      <label for="username">아이디</label>
      <mdb-input label="아이디" id="username" v-model="credentials.username" /><br>

      <label for="password">비밀번호</label>
      <mdb-input label="password" id="password" type="password" v-model="credentials.password" @keypress.enter.native="login"/><br><br>
      <mdb-btn flat size="md" darkWaves @click.native="login">로그인</mdb-btn>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { mdbBtn, mdbInput } from 'mdbvue'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'LoginForm',
  components: {
      mdbBtn,
      mdbInput
  },
  data: function () {
    return {
      credentials: {
        username: '',
        password: '',
      },
    }
  },
  methods: {
    login: function () {
      axios.post(`${SERVER_URL}/accounts/api-token-auth/`, this.credentials)
        .then(res => {
          console.log(res.data)
          console.log()
          console.log()
          localStorage.setItem('user', JSON.stringify(res.data))
          this.$emit('login')
          this.$router.push({ name: 'Home' })
        })
        .catch(err => {
          console.log(err)
        })
    }
  }
}
</script>

<style scoped>
.loginForm {
  justify-content: center;
  width: 40vw;
  margin: 0 auto;
}
</style>