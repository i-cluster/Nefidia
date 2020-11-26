import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    genres: '',
    themes: '',
    movies: '',
    reviews: '',
    comments: '',
    filter_code: ''
  },
  mutations: {
    GET_DATA: function (state, res) {
      state.genres = res.genres
      state.themes = res.themes
      state.movies = res.movies_db
      state.filter_code = res.filter_code
    }
  },
  actions: {
    setToken: function () {
      return new Promise((resolve) => {
        const token = JSON.parse(localStorage.getItem('user')).token
        resolve({ token: { Authorization: `JWT ${token}` }})
      })
    },
    getUser: function () {
      return new Promise((resolve) => {
        const user = JSON.parse(localStorage.getItem('user')).username
        resolve(user)
      })
    },
    getData: function ({ commit }, res) {
      commit('GET_DATA', res)
    }
  },
  modules: {
  },
  plugins: [
    createPersistedState(),
  ]
})
