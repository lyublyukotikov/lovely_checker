<template>
  
<div class="wrapper">
  <div class="section_3">
    <div class="section_3_left">
    <button class="button-info" @click="button_info"  >
   общая информация
  </button>
  
  <button class="button-map " @click="button_map"   >
     на карте
  </button>
  </div>
 <location_information 
 v-if="is_open_info"
 v-for=" product in card_changeable_parks"

 :key="product.id"
 :info_timetable_card_parks="product"
 
 />
  <card_location
  v-if="is_open_card_location"
  
  />
</div>
  </div>



</template>

<script>

import card_location from'../card_location.vue'

 import location_information from './location_information.vue'
 export default {
  name: 'card_changeable_parks',
  components:{
   location_information,
   card_location
  },
  data(){
    return{
      is_open_info:false,
      is_open_card_location:false,
    
     
      

  "card_changeable_parks": [
    { 
      address:'aadadada',
      opening_hours:'fsfsfsfs',
      telephone:'dsdsdsdsdsds',
      date_of_foundation:'fsfsfsfsfs',
      availability_of_playgrounds:'fsfsfsfsfsfs',
      availability_of_spordgrounds:'fsfsfsfsfsfs'


    },

    
    
  ]
  
      
    }

  },
 
    methods:{
      button_map(){
      this.is_open_card_location=!this.is_open_card_location;
      
    },
    button_info(){
      this.is_open_info=!this.is_open_info;
    },
  },
}
 




</script>


<style scoped>

.wrapper{
  width : 1000px;
   margin: 0 auto;
   padding-top: 20px;
   padding-top: 20px;
   padding-right: 15px;
   padding-left: 15px;
   overflow:hidden ;
   background-color: white;
 }
.section_3{
  width: 920px;
 height: 356px;
 border-radius: 20px;
 border:1px solid black;
 display: flex;
 margin: 0 auto;
}
.section_3_left{
  display: flex;
flex-direction: column
}



.button-info{
  background:white;
  border-radius: 20px;
  border: none;
  width: 256px;
  height: 178px;
  cursor: pointer;
  transition: background linear 0.5s;
}
.button-map{
  background: white;
  border-radius: 20px;
  border: none;
  width: 256px;
  height: 178px;
  cursor: pointer;
  transition: background linear 0.5s;
}


.button-info:hover {
  background-color:black;
  color:white;
}

.button-map:hover{
  background-color:black;
  color:white;
}




</style>