<template>
<div class="main_page">

<slider/>
<wrapper_top_3_object></wrapper_top_3_object>
<marketing_main_page></marketing_main_page>

</div>




</template>

<script>
import slider  from '../components/main_page/slider/slider.vue'
import marketing_main_page from "../components/main_page/marketing_static/marketing_main_page.vue";

import wrapper_top_3_object from "../components/main_page/catalog_top_3_object/wrapper_top_3_object.vue";
export default {
  name:'main_page',
  components: {
  slider,
   wrapper_top_3_object,
   marketing_main_page
    
    
    
   
   
  },
}






</script>


<style>








</style>