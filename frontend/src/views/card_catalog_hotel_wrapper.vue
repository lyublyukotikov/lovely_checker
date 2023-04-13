<template>
  <div class="wrapper">
    <h1>Отели</h1>
    <card_hotel_catalog   />

  </div>
</template>



<script>

import card_hotel_catalog from '../components/card_catalog/card_catalog_hotel/card_hotel_catalog.vue'
export default {
  name: 'card_catalog_hotel_wrapper',
  components: {
    
    card_hotel_catalog,
    
  },
  data(){
    return{
      
    }
  },


}

</script>


<style scoped>

 .wrapper h1{
   margin-top: 0px;
   text-align: center;
 }
</style>