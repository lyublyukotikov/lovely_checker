<template>
  <div class="card_parks_catalog">
    
    <div class="catalog_list">
      <card_parks_catalog_item
      v-for="park in PARKS"
      :key="park.id"
      :card_parks_catalog_item="park"
      :number="park.rating"
      
      
      
      />
    </div>


  </div>


</template>


<script>
import PARKS from 'axios'
import{mapActions,mapGetters} from 'vuex'
import card_parks_catalog_item from './card_parks_catalog_item.vue'
export default {
  name:'card_parks_catalog',
  components:{
    card_parks_catalog_item
  },
  data(){
    return{

    }
  },
  computed:{
    ...mapGetters([
 'PARKS'
    ]),
  },
  methods: {
  
    
    ...mapActions([
      'GET_PRODUCTS_PARK_FROM_API'
      ]),

  },
  mounted(){
    this.GET_PRODUCTS_PARK_FROM_API()
  }
 
 
}





</script>


<style >

.catalog_list{
  display:flex;
  flex-wrap: wrap;
  justify-content: space-between;
  align-items: center;
  
  

}
</style>