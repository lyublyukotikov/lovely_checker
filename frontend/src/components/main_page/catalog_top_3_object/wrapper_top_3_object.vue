<template>
  <div class="wrapper">
   
    <h3>Топ 3 просматривыемых места</h3>
   <catalog_top_3_object/>
  
  </div>







</template>


<script>

import catalog_top_3_object from './catalog_top_3_object.vue'
export default {
  name:'wrapper_top_3_object',
  components: {

catalog_top_3_object
    
    
    
   
   
  },
}





</script>


<style scoped>

 
 .wrapper h3{
   margin-top: 0px;
   text-align: center;
 }

</style>