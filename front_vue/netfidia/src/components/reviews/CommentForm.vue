<template>
  <div>
    <h3>CommentForm</h3>
    <mdb-input label="내용" v-model="comment.content" />
    <mdb-btn flat size="sm" darkWaves @click.native="leaveComment">댓글 남기기</mdb-btn>
  </div>
</template>

<script>
import axios from 'axios'
import { mdbBtn, mdbInput } from 'mdbvue'
import { mapActions } from 'vuex'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'CommentForm',
  components: {
    mdbBtn,
    mdbInput
  },
  props: {
    reviewId: {
      type: Number
    }
  },
  data: function () {
    return {
      comment: {
        content: ''
      }
    }
  },
  methods: {
    ...mapActions(['setToken']),
    leaveComment: function () {
      if (this.comment.content) {
        if (localStorage.getItem('user')) {
          this.setToken().then(res => {
            axios.post(`${SERVER_URL}/reviews/comment/create/${this.reviewId}/`, this.comment, { headers: res.token })
              .then(res => {
                this.$emit('new-comment', res.data)
                this.comment.content = ''
              })
              .catch(err => console.log(err))
          })
        } else {
          this.$router.push({ name: 'Login' })
        }
      }
    }
  }
}
</script>

<style>

</style>