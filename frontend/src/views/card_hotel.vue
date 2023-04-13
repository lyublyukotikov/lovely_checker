<template>
<div  class="card_hotel" >
<place_info_wrapper/>
<card_changeable_hotel/>
<app_comment/>
</div>


</template>


<script>
import place_info_wrapper from '../components/card_object/place_info_wrapper.vue'
import card_changeable_hotel from '../components/card_object/card_hotel/card_changeable_hotel.vue';
import app_comment from '../components/comment/app_comment.vue';
export default {
  name:'card_hotel',
  components: {

    
    place_info_wrapper,
   card_changeable_hotel,
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