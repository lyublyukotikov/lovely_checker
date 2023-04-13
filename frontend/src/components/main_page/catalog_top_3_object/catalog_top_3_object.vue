<template>
  <div class="card_catalog">
    
    <div class="catalog_list">
      <item_top_3_object
      v-for="product in TOP_3_PRODUCTS"
      :key="product.id"
      :product_data="product"
      :number="product.rating"
      
      
      
      />
    </div>


  </div>



</template>

<script>












import TOP_3_PRODUCTS from 'axios'
import{mapActions,mapGetters} from 'vuex'
import item_top_3_object from './item_top_3_object.vue'


export default {

  name:'catalog_top_3_object',
  components: {
item_top_3_object
  },
  data(){
    return{

    }
  },
  computed:{
    ...mapGetters([
 'TOP_3_PRODUCTS'
    ]),
  },
  methods: {
  
    
    ...mapActions([
      'GET_PRODUCTS_FROM_API'
      ]),

  },
  mounted(){
    this.GET_PRODUCTS_FROM_API()
  }


}





</script>


<style>

.catalog_list{
  display:flex;
  flex-wrap: wrap;
  justify-content: space-between;
  align-items: center;
  
  

}





</style>