<template>
  <div class="wrapper">
    <carousel class="carousel" :items-to-show="1.5">
      <slide class="slide" v-for="slide in slides" :key="slide.id">
       
        <img class="img" :src="slide.url" alt="slide.id">
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
  name: 'slider',
  components: {
    Carousel,
    Slide,
    Pagination,
    Navigation,
  },
  data(){
    return{
      slides: [
        { id: 1, url:  "../../../assets/page_infro_images/1.jpg" },
        { id: 2, url:  "../../../assets/page_infro_images/2.jpg" },
        { id: 3, url:  "../../../assets/page_infro_images/3.jpg" },
        
      ]
    }
  }
}
</script>
<style scoped>

.slide{
  
 

  height: 343px;
 
  width: 840px;
  font-size: 20px;
  
  display: flex;
  justify-content: center;
  align-items: center;
  
}
.carousel{
  border-radius: 20px;
  background-color: #D9D9D9;
  padding: 15px;
  margin-bottom: 100px;
}


</style>