<template>
  <div class="wrapper">
    <h1>Театры/Кино</h1>
    <card_catalog   />

  </div>
</template>



<script>

import card_catalog from '../components/card_catalog/card_theater/card_theater_catalog.vue'
export default {
  name: 'card_catalog_theater_wrapper',
  components: {
    
    card_catalog,
    
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