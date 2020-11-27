<template>
  <div id="container">
    <mdb-container fluid>
      <mdb-row>
        <mdb-col col="sm">
          <div id="moviedetail-c">
            <MovieDetail :movie="movie" />
          </div>
        </mdb-col>
          
        <mdb-col col="sm">
          <div id="review-c">
            <ReviewForm
              :movieId="movie.unique_id"
              v-bind="userReview"
              @new-review="newReview"
              @edit-review="editReview"
            /><br><hr>
            <!-- {{ movie.reviews }} -->
            <ReviewList :reviews="reviews" :currentUser="currentUser" />
          </div>
        </mdb-col>
      </mdb-row>
    </mdb-container>
  </div>
</template>

<script>
import axios from 'axios'
import { mapActions } from 'vuex'
import { mdbContainer, mdbRow, mdbCol } from 'mdbvue';

const SERVER_URL = process.env.VUE_APP_SERVER_URL

import MovieDetail from '@/components/movies/MovieDetail'
import ReviewForm from '@/components/reviews/ReviewForm'
import ReviewList from '@/components/reviews/ReviewList'

export default {
  name: 'Movie',
  components: {
    MovieDetail,
    ReviewForm,
    ReviewList,
    'mdb-container': mdbContainer,
    'mdb-row': mdbRow,
    'mdb-col': mdbCol,
  },
  data: function () {
    return {
      movie: {},
      reviews: [],
      currentUser: '',
      userReview: {},
    }
  },
  props: {
    movieId: {
      type: Number,
    }
  },
  methods: {
    ...mapActions(['setToken', 'getUser']),
    newReview: function (review) {
      this.reviews.push(review)
      this.userReview = review
    },
    editReview: function (review) {
      for (const index in this.reviews) {
        if (this.reviews[index].id === review.id) {
          this.reviews.splice(index, 1, review)
        }
      }
      this.userReview = review
    }
  },
  created: function () {
    if (localStorage.getItem('user')) {
      this.setToken().then(res => {
        axios.get(`${SERVER_URL}/reviews/movie-detail`, { headers: res.token, params: { movieId: this.movieId }})
          .then(res => {
            this.movie = res.data.movie
            this.reviews = res.data.reviews
            this.userReview = res.data.user_review

            // this.getUser().then(res => {
            //   for (const review of this.reviews) {
            //     if (review.user.username === res) {
            //       this.userReview = review
            //       return
            //     }
            //   }
            // })
          })
          .catch(err => console.log(err))
      })

      this.getUser().then(res => this.currentUser = res)
    } else {
      this.$router.push({ name: 'Login' })
    }
  }
}
</script>

<style>
#moviedetail-c {
  margin: 30px;
}

#review-c {
  margin: 50px;
}

#container {
  width: 100%;
}
</style>