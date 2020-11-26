<template>
  <div>
    <h3>ReviewList</h3>
    <li v-for="(review, idx) in reviews" :key="idx">
      작성자: {{ review.user.username }} |
      평점 : {{ review.vote }} |
      <span v-if="review.spoiler" @click="openSpoiler(review)">
        <span v-text="spoiler"></span> |
      </span>
      <span v-else>
        한줄평: {{ review.content }} |
      </span>
    </li>
  </div>
</template>

<script>
import { mapActions } from 'vuex'
// import { mdbBtn, mdbIcon } from 'mdbvue'

export default {
  name: 'ReviewList',
  components: {
    // mdbBtn,
    // mdbIcon
  },
  props: {
    reviews: {
      type: Array
    },
  },
  data: function () {
    return {
      spoiler: '~~ 스포일러가 있어요. ~~',
    }
  },
  methods: {
    ...mapActions(['getUser']),
    openSpoiler: function (review) {
      review.spoiler = !review.spoiler
    },
    editReview: function () {
      if (this.review.vote && this.review.content) {
      //   this.setToken().then(res => {
      //     axios.put(`${SERVER_URL}/reviews/edit/`, this.review, { headers: res.token})
      //       .then(res => this.$emit('new-review', res.data))
      //       .catch(err => console.log(err))
      //   })
      }
    }
  },
}
</script>

<style>

</style>