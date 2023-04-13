<template>
  <div class="menu_rest">
   
      <carousel class="carousel" :items-to-show="1.5">
        <slide class="slide" v-for="slide in 10" :key="slide">
          {{ slide }}
        </slide>
    
        <template #addons>
          <navigation />
          <pagination />
        </template>
      </carousel>
    </div>
 


</template>

<script>
import 'vue3-carousel/dist/carousel.css'
import { Carousel, Slide, Pagination, Navigation } from 'vue3-carousel'
export default {
  name: 'menu_rest',
  components: {
    Carousel,
    Slide,
    Pagination,
    Navigation,
  },
  data(){
    return{  

    }

  },
  props: {
    info_timetable_card_rest:{
      type:Object,
      default(){
        return{}
      }
    },


  },

}
</script>

<style scoped>
.menu_rest{
  margin: auto;
 
  width: 800px;
  box-sizing: border-box;
}
.carousel{
  width: 680px;
  

}


</style>