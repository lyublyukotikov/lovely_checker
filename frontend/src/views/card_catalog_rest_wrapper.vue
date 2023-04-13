<template>
  <div class="wrapper">
    <h1>Кафе/Рестораны</h1>
    <card_rest_catalog   />

  </div>
</template>



<script>

import card_rest_catalog from '../components/card_catalog/card_catalog_rest/card_rest_catalog.vue'
export default {
  name: 'card_catalog_rest_wrapper',
  components: {
    
    card_rest_catalog,
    
  },
  data(){
    return{
     
    }
  }

}

</script>


<style scoped>

 .wrapper h1{
   margin-top: 0px;
   text-align: center;
 }
</style>