<template>
  <place_info
  v-for="product in place_info_wrapper" 
  
   :key="product.id"
  :categies="product"
  :number="product.rating"
  />


</template>


<script>
import place_info from './place_info.vue'
export default {
  name: 'place_info_wrapper',
  components:{
    place_info
  },
 


   data(){
    return{
      "place_info_wrapper": [
    { id:'1',
      image:"1.jpg",
    title_place_info:"Гостиница Таганрог",
    type_of_category:"Отели",
    rating:2.5

    },
    
   
   
   
   
    
    
  ]
    }
  },
  computed:{
    ratingWidth(){
      return this.number/this.starLimit*100
    },
    ratingWidthStyle(){
      return `width: ${this.ratingWidth}%;`
    }
  }

  
}

</script>


<style>




</style>