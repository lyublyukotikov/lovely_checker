<template>
  <div class="card_pars">
    <place_info_wrapper/>
    <card_changeable_parks/>
   <app_comment/>
   
</div>



</template>


<script>

import place_info_wrapper from '../components/card_object/place_info_wrapper.vue'

import card_changeable_parks from '../components/card_object/card_parks/card_changeable_parks.vue'


import app_comment from '../components/comment/app_comment.vue'



export default {
  name:'card_parks',
  components: {

    
    place_info_wrapper,
   card_changeable_parks,
    app_comment,
  
    
   
   
  },
  data(){
    return{
 
  
      
    }

  },
  
}





</script>


<style>



</style>