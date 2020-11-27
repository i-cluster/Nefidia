<template>
  <div id="reviewform">
    <h3>ReviewForm</h3>
    <div style="width: 30vw; margin: 0 auto;">
      <select class="browser-default custom-select" v-model="vote">
        <option>Your vote is</option>
        <option value="1">1</option>
        <option value="2">2</option>
        <option value="3">3</option>
        <option value="4">4</option>
        <option value="5">5</option>
      </select>
      <mdb-input type="textarea" v-model="content" id="exampleInput" label="한줄평"/>
      <div class="custom-control custom-checkbox">
        <input type="checkbox" class="custom-control-input" id="defaultUnchecked" v-model="spoiler">
        <label class="custom-control-label" for="defaultUnchecked">스포일러가 포함되어 있습니다.</label>
      </div><br>
      <mdb-btn flat size="sm" darkWaves @click.native="reviewAction">작성하기</mdb-btn><br>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { mapActions } from 'vuex'
import { mdbInput, mdbBtn } from 'mdbvue'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'ReviewForm',
  components: {
    mdbInput,
    mdbBtn
  },
  props: {
    movieId: {
      type: Number
    },
    id: Number,
    vote: Number,
    content: String,
    spoiler: Boolean
  },
  data: function () {
    return {
      // review: Vue.util.extend({}, this.userReview)
      review: {
        vote: '',
        content: '',
        spoiler: ''
      }
    }
  },
  methods: {
    ...mapActions(['setToken']),
    reviewAction: function () {
      this.review.vote = this.vote
      this.review.content = this.content
      this.review.spoiler = this.spoiler

      if (this.review.vote && this.review.content) {

        if (localStorage.getItem('user')) {

          this.setToken().then(res => {
            if (!this.id) {
              // 글 작성
              axios.post(`${SERVER_URL}/reviews/create/${this.movieId}/`, this.review, { headers: res.token })
                .then(res => this.$emit('new-review', res.data))
                .catch(err => console.log(err))
            } else {
              // 글 수정
              axios.put(`${SERVER_URL}/reviews/edit/${this.id}/`, this.review, { headers: res.token})
              .then(res => this.$emit('edit-review', res.data))
              .catch(err => console.log(err))
            }
          })

        } else {
          this.$router.push({ name: 'Login' })
        }
      } else if (!this.review.vote && !this.review.content) {
        if (!this.id) {
          // 글 삭제
          console.log(1)
        }
      }
    }
  }
}
</script>

<style>

</style>