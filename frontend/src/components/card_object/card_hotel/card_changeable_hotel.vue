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
    <button class="button-register" @click="button_register">
      зарегистрироваться
    </button>
    
    
    </div>
   <location_information_hotel 
   v-if="is_open_info"
   v-for=" hotel in hotels"
  
   :key="hotel.id"
   :info_timetable_card_hotel="hotel"
   
   />
    <card_location
    v-if="is_open_card_location"
    
    />
    
  <register
  v-if="is_open_card_register"
  
  />
    
  
  </div>
  </div>


</template>


<script>
import card_location from'../card_location.vue'
 import location_information_hotel from './location_information_hotel.vue'
import register from './register.vue'

 export default {
  name: 'card_changeable_hotel',
  components:{
   location_information_hotel,
   card_location,
  register,
  },
  data(){
    return{
      is_open_info:false,
      is_open_card_location:false,
      is_open_event:false,
      is_open_menu:false,
      is_open_to_book:false,
      is_open_card_register:false,
    
     
      

  "hotels": [
    { id:"1",
      address:'Греческая,58',
      opening_hours:'11.30-18.00',
      telephone:'888534567',
      

     



    },
    { id:"2",
      address:'Ломакина,74',
      opening_hours:'12.30-20.00',
      telephone:'89198899972',
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
    button_register(){
      this.is_open_card_register=!this.is_open_card_register;
    }

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
.button-register{
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
.button-register:hover{
  background-color:black;
  color:white;
}



</style>