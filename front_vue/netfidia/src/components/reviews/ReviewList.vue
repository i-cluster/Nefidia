<template>
  <div>
    <h3>ReviewList</h3>
    <hr>
    <li v-for="(review, idx) in reviews" :key="idx">
      작성자: {{ review.user.username }} |
      평점 : {{ review.vote }} |
      <span v-if="review.spoiler" @click="openSpoiler(review)">
        <span v-text="spoiler"></span> |
      </span>
      <span v-else>
        한줄평: {{ review.content }} |
      </span>
      좋아요 : {{ review.like_count }} |
      <i :class="{fas: liked, far: !liked}" :ref="review.id" class="fa-paper-plane" @click="likeReview(review.id)"></i><br><br>
      <!-- {{ review }} <br> -->
      <!-- {{ review.like_users }} | -->
      <CommentForm :reviewId="review.id" @new-comment="newComment" />
      <br>
      <CommentList :comments="review.comments" />
      <hr>
    </li>
  </div>
</template>

<script>
import axios from 'axios'
import { mapActions } from 'vuex'

import CommentForm from '@/components/reviews/CommentForm'
import CommentList from '@/components/reviews/CommentList'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'ReviewList',
  components: {
    // mdbBtn,
    CommentForm,
    CommentList
  },
  props: {
    reviews: {
      type: Array
    },
    currentUser: {
      type: String
    }
  },
  data: function () {
    return {
      spoiler: '~~ 스포일러가 있어요. ~~',
      review_like: {},
      liked: true
    }
  },
  methods: {
    ...mapActions(['getUser', 'setToken']),
    openSpoiler: function (review) {
      review.spoiler = !review.spoiler
    },
    likeReview: function (reviewId) {
      if (localStorage.getItem('user')) {
        this.setToken().then(res => {
          axios.get(`${SERVER_URL}/reviews/like`, {headers: res.token, params: { reviewId: reviewId }})
            .then(res => {
              console.log(res)
              for (const review of this.reviews) {
                if (review.id === res.data.review.id) {
                  review.like_count = res.data.review.like_count
                  review.like_users = res.data.review.like_users
                  this.$refs[review.id][0].classList.toggle('fas')
                  this.$refs[review.id][0].classList.toggle('far')
                  break
                }
              }
              
              // this.liked = !this.liked
            })
            .catch(err => console.log(err))
        })
      } else {
        this.$router.push({ name: 'Login' })
      }
    },
    newComment: function (comment) {
      for (const review of this.reviews) {
        if (review.id === comment.review) {
          review.comments.push(comment)
          break
        }
      }
    }
  },
  created: function () {
    // let review_like = {}
    // reviewFor:
    // for (const review of this.reviews) {
    //   for (const user of review.like_users) {
    //     if (user.username === this.currentUser) {
    //       review_like[[review.id]] = true
    //       continue reviewFor
    //     }
    //   }
    //   review_like[[review.id]] = false
    // }
    // this.review_like = review_like
  }
}
</script>

<style>

</style>