<template>
<div class="card_theater">
  <place_info_wrapper

  />
<card_changeable_theater/>
<app_comment/>
</div>


</template>


<script>
import place_info_wrapper from '../components/card_object/place_info_wrapper.vue'
import card_changeable_theater from '../components/card_object/card_theater/card_changeable_theatre.vue'
import app_comment from '../components/comment/app_comment.vue'
export default {
  name:'card_theater',
  components: {

    
    place_info_wrapper,
   card_changeable_theater,
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