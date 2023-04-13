<template>
  <div class="card_hotel_catalog">
    
    <div class="catalog_list">
      <card_hotel_catalog_item
      v-for="hotel in HOTELS"
      :key="hotel.id"
      
      :card_hotel_catalog_item="hotel"
      :number="hotel.rating"

      />
     
    </div>


  </div>


</template>


<script>
import HOTELS from 'axios'
import{mapActions,mapGetters} from 'vuex'
import card_hotel_catalog_item from './card_hotel_catalog_item.vue'
export default {
  name:'card_hotel_catalog',
  components:{
    card_hotel_catalog_item,
    

  },
  data(){
    return{
      
    
  

    }
    
  },
  
  computed:{
    ...mapGetters([
 'HOTELS'
    ]),
  },
  methods: {
  
    
    ...mapActions([
      'GET_PRODUCTS_HOTEL_FROM_API'
      ]),

  },
  mounted(){
    this.GET_PRODUCTS_HOTEL_FROM_API()
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