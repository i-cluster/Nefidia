<template>
  <div>
    <h1>Signup</h1><br>
    <div class="signupForm">
      <label for="username">아이디</label>
      <mdb-input label="아이디" id="username" v-model="credentials.username" /><br>

      <label for="password">비밀번호</label>
      <mdb-input label="password" id="password" type="password" v-model="credentials.password" /><br>

      <label for="passwordConfirmation">비밀번호 확인</label>
      <mdb-input label="passwordConfirmation" id="passwordConfirmation" v-model="credentials.passwordConfirmation" type="password" /><br>

      <label for="first_name">이름</label>
      <mdb-input label="first_name" id="first_name" v-model="credentials.first_name" /><br>

      <label for="genres">좋아하는 장르</label><br>
      <mdb-btn-group>
        <mdb-btn v-for="(genre, idx) in genres" :key="idx" color="mdb-color" @click.native="toggleGenre(genre.unique_id)" :active="credentials.user_genres[genre.unique_id]">
          {{ genre.name }}
        </mdb-btn>
      </mdb-btn-group><br><br>

      <label for="themes">관심있는 테마</label><br>
      <mdb-btn-group>
        <mdb-btn v-for="(theme, idx) in themes" :key="idx" color="mdb-color" @click.native="toggleTheme(theme.name)" :active="credentials.user_themes[theme.name]">
          {{ theme.name }}
        </mdb-btn>
      </mdb-btn-group><br><br>
      <mdb-btn flat size="md" darkWaves @click.native="signup">가입하기</mdb-btn>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { mapState } from 'vuex'
import { mdbBtn, mdbBtnGroup, mdbInput } from 'mdbvue'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'SignupForm',
  components: {
      mdbBtn,
      mdbBtnGroup,
      mdbInput
  },
  data: function () {
    return {
      credentials: {
        username: '',
        password: '',
        passwordConfirmation: '',
        first_name: '',
        user_genres: {},
        user_themes: {}
      },
    }
  },
  computed: {
    ...mapState(['genres', 'themes']),
  },
  methods: {
    toggleGenre(unique_id) {
      const user_genres = this.credentials.user_genres
      this.$set(user_genres, unique_id, !user_genres[unique_id])
    },
    toggleTheme(name) {
      const user_themes = this.credentials.user_themes
      this.$set(user_themes, name, !user_themes[name])
    },
    signup() {
      axios.post(`${SERVER_URL}/accounts/signup/`, this.credentials)
        .then(() => {
          this.$router.push({ name: 'Login' })
        })
        .catch(err => {
          console.log(err)
        })
    }
  },
  created: function () {
    // for (const genre of this.genres) {
    //   this.credentials.user_genres[genre.uniq_id] = false 
    // }
    // for (const theme of this.themes) {
    //   this.credentials.user_themes[theme.name] = false 
    // }
  }
}
</script>

<style scoped>
.signupForm {
  justify-content: center;
  width: 40vw;
  margin: 0 auto;
}
</style>