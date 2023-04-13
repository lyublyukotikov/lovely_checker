<template>
  <div class="card_rest_catalog">
    
    <div class="catalog_list">
      <card_rest_catalog_item
      v-for="rest in RESTS"
      :key="rest.id"
      :card_rest_catalog_item="rest"
      :number="rest.rating"
      
      
      
      />
    </div>


  </div>


</template>


<script>
import RESTS from 'axios'
import{mapActions,mapGetters} from 'vuex'
import card_rest_catalog_item from './card_rest_catalog_item.vue'
export default {
  name:'card_rest_catalog',
  components:{
    card_rest_catalog_item
  },
  data(){
    return{

    }
  },
  computed:{
    ...mapGetters([
 'RESTS'
    ]),
  },
  methods: {
  
    
    ...mapActions([
      'GET_PRODUCTS_REST_FROM_API'
      ]),

  },
  mounted(){
    this.GET_PRODUCTS_REST_FROM_API()
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