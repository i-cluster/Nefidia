<template>
  <div>
    <h3><b>Movie Detail</b></h3>
    
    <div id="short overview">
    <mdb-container fluid>
      <mdb-row>
        <mdb-col col="sm">
          <div id="onlyposter">
            <img :src="posterUrl(movie.poster_path)" alt="">
          </div>
          <br><br>
          <div id="rating">
            <h5>평점</h5>
            {{ movie.vote_average }}
          </div>
        </mdb-col>

        <mdb-col col="sm">
        [title director actress rating column]
          <div id="title">
            <h5><b> {{ movie.title }} </b></h5>
          </div>

          <div id="director">
            <div class="directorbox">
              <p>
              감독: ~
              출연: ~
              개봉일: {{ movie.release_date }}
              러닝타임: ~
              </p>
            </div>
          </div>
          
          <div id="genrelist">
            <div class="genrebox">
              <p>장르</p>
              <span v-for="(genre, idx) in movie.movie_genres" :key="idx">{{ genre.name }} </span><br>
            </div>
          </div>

          <!-- <div id="hashtaglist">
            <div class="tagbox">
              <p>태그</p>
              
            </div>
          </div> -->
        </mdb-col>
      </mdb-row>
    </mdb-container>
      
      <!-- 전체 배경화면을 흐릿하게 포스터로 넣을까나 -->
   
    </div>   
    <div id="overview">
      <h4>Overview</h4>
      <div class="overviewbox">
        <h5>{{ movie.overview }}</h5>
      </div>
    </div>
      
    <div id="videos">
      <h4>크레딧영상</h4>
      <!-- https://antoniandre.github.io/vueper-slides/ -->
      <vueper-slides
        class="no-shadow"
        :visible-slides="2"
        slide-multiple
        :gap="2"
        :slide-ratio="1 / 2"
        :dragging-distance="200"
        :breakpoints="{ 800: { visibleSlides: 2, slideMultiple: 2 } }">
        <vueper-slide v-for="i in 10" :key="i" :title="i.toString()" />
      </vueper-slides>      
    </div>
  </div>
</template>

<script>
import { VueperSlides, VueperSlide } from 'vueperslides'
import { mdbContainer, mdbRow, mdbCol } from 'mdbvue';

export default {
  name: 'MovieDetail',
  components: {
    'mdb-container': mdbContainer,
    'mdb-row': mdbRow,
    'mdb-col': mdbCol,
    'vueper-slide': VueperSlide,
    'vueper-slides': VueperSlides,
  },
  props: {
    movie: {
      type: Object
    }
  },
  computed: {
    posterUrl: function () {
      return (poster_path) => {
        return `https://image.tmdb.org/t/p/w200${poster_path}`
      }
    }
  }
}
</script>

<style>
#title {
  text-align: left;
}

.directorbox {
  border-radius: 10px;
  /* height: ;
  width: ; */
  font-size: 10pt;
  text-align: left;
  color:  #fff;
  background: transparent;
  box-sizing: border-box;
  padding: auto;
  border: auto;
  margin: 10px;
  margin-top: 30px;
  margin-bottom: 30px;
}

.genrebox {
  border: 1px solid rgb(50, 53, 243);
  border-radius: 10px;
  /* height: ;
  width: ; */
  font-size: 10pt;
  text-align: left;
  color: #fff;
  background: rgba(54, 53, 2, 0.582);
  box-sizing: border-box;
  padding: 20px;
  margin: 10px;
  margin-top: 30px;
  margin-bottom: 30px;  
}

.overviewbox {
  border: 1px solid rgb(50, 53, 243);
  border-radius: 10px;
  /* height: ;
  width: ; */
  font-size: 10pt;
  text-align: left;
  color: #fff;
  background: rgba(54, 53, 2, 0.582);
  box-sizing: border-box;
  padding: 20px;
  margin: 10px;
  margin-top: 30px;
  margin-bottom: 30px; 
}

#genrelist {
  text-align: left;
}

#rating {
  text-align: left;
}

#overview {
  text-align: left;
}

#videos {
  text-align: left;
}
</style>