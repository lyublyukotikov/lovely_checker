<template>
<div class="card_rest">
  <place_info_wrapper
  
  
  />
<card_changeable_rest/>
<app_comment/>


</div>


</template>


<script>
import place_info_wrapper from '../components/card_object/place_info_wrapper.vue'
import card_changeable_rest from '../components/card_object/card_rest/card_changeable_rest.vue';
import app_comment from '../components/comment/app_comment.vue'
export default {
  name:'card_rest',
  components: {

    
    place_info_wrapper,
   card_changeable_rest,
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