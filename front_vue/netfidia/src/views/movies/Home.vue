<template>
  <div class="home">
    <div id="billboard">
      <h1>Today's Top recommendation just for you</h1>
        <!-- Youtube 링크? 영화  -->

      <!-- <vueper-slides
        ref="myVueperSlides"
        :parallax="parallax"
        :parallax-fixed-content="parallaxFixedContent">
        <vueper-slide
          v-for="(slide, i) in slides"
          :key="i"
          :image="slide.image"/>
      </vueper-slides> -->
    </div>
   
    <div id="slider">
      <span v-for="(code, idx) in filter_code" :key="idx">
        <div class="movie-list">
        <h3>{{ code }}</h3>
          <vueper-slides
            class="no-shadow"
            :visible-slides="8"
            slide-multiple
            :gap="1"
            :slide-ratio="1 / 6"
            :dragging-distance="200"
            :breakpoints="{ 800: { visibleSlides: 2, slideMultiple: 2 } }">
            <vueper-slide
              v-for="(movie, idx) in movies[code]"
              :key="idx"
              :image="posterUrl(movie.poster_path)"
              @click.native="movieLink(movie.id)"
            />
          </vueper-slides>
        </div>
      </span>
    </div>
    
  </div>
</template>

<script>
import { mapState } from 'vuex'
import { VueperSlides, VueperSlide } from 'vueperslides'
import 'vueperslides/dist/vueperslides.css'

export default {
  name: 'Home',
  components: {
    'vueper-slide': VueperSlide,
    'vueper-slides': VueperSlides,
  },
  data: function () {
    return {
      parallax: 1,
      parallaxFixedContent: false
    }
  },
  computed: {
    ...mapState(['movies', 'filter_code']),
    posterUrl: function () {
      return (poster_path) => {
        return `https://image.tmdb.org/t/p/w200${poster_path}`
      }
    }
  },
  methods: {
    movieLink: function (movieId) {
      this.$router.push({ name: 'Movie', params: { movieId: movieId } })
    }
  }
}
</script>

<style>
#billboard {
  margin-bottom: 20px;
}

#slider {
  margin-top: 100px;
  margin-bottom: 300px;
}

.movie-list {
  margin-top: 200px;
  margin-bottom: 200px;
}

#recommendedlist {
  margin-top: 200px;
  margin-bottom: 200px;
}

#popularlist {
  margin-top: 200px;
  margin-bottom: 200px;
}

#boxofficelist {
  margin-top: 200px;
  margin-bottom: 200px;
}
</style>