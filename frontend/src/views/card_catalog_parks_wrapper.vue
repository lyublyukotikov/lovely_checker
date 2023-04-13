<template>
  <div class="wrapper">
    <h1>Парки/Скверы</h1>
    <card_parks_catalog   />

  </div>
</template>



<script>

import card_parks_catalog from '../components/card_catalog/card_parks/card_parks_catalog.vue'
export default {
  name: 'card_catalog_parks_wrapper',
  components: {
    
    card_parks_catalog,
    
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