<template>
  <div class="card_theater_catalog">
    
    <div class="catalog_list">
      <card_catalog_item
      v-for="theater in THEATERS"
      :key="theater.id"
      :card_theater_catalog_item="theater"
      :number="theater.rating"
      
      
      
      />
    </div>


  </div>


</template>


<script>
import THEATERS from 'axios'
import{mapActions,mapGetters} from 'vuex'
import card_catalog_item from './card_theater_catalog_item.vue'
export default {
  name:'card_catalog_theater',
  components:{
    card_catalog_item
  },
  data(){
    return{

    }
  },
  computed:{
    ...mapGetters([
 'THEATERS'
    ]),
  },
  methods: {
  
    
    ...mapActions([
      'GET_PRODUCTS_THEATER_FROM_API'
      ]),

  },
  mounted(){
    this.GET_PRODUCTS_THEATER_FROM_API()
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