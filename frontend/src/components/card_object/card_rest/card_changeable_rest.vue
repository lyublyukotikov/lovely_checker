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
    <button class="button-menu" @click="button_menu">
     меню
    </button>
    <button class="button-to_book" @click="button_to_book">
      забронировать столик
    </button>
    </div>
   <location_information_rest
   v-if="is_open_info"
   v-for=" product in card_changeable_rest"
  
   :key="product.id"
   :info_timetable_card_rest="product"
   
   />
    <card_location
    v-if="is_open_card_location"
    
    />
    
  <menu_rest
  v-if="is_open_menu"
    />
    <to_book_rest
    v-if="is_open_to_book"
    />
  
  </div>
  </div>
  

</template>

<script>
import card_location from'../card_location.vue'
 import location_information_rest from './location_information_rest.vue'
 import menu_rest from './menu_rest.vue'
 import to_book_rest from './to_book_rest.vue'

 export default {
  name: 'card_changeable_rest',
  components:{
   location_information_rest,
   card_location,
   menu_rest,
   to_book_rest
  },
  data(){
    return{
      is_open_info:false,
      is_open_card_location:false,
      is_open_event:false,
      is_open_menu:false,
      is_open_to_book:false,
    
     
      

  "card_changeable_rest": [
    { id:'1',
      address:'Петровская ул., 42',
      opening_hours: '9.00-18.00',
      telephone:'+7 (989) 507-79-47',
      prace:'низкий',
      parking:' не имеется',
      image:'1.png'


    },
    { id:'1',
      address:'Тургеневский,23',
      opening_hours: '9.00-18.00',
      telephone:'+7 (919)889-99-72',
      prace:'высокий',
      parking:'имеется',
    
      image:'2.png'


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
    button_menu(){
      this.is_open_menu=!this.is_open_menu
    },
    button_to_book(){
      this.is_open_to_book=!this.is_open_to_book
    }

  },
}


</script>


<style>
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
  max-width: 920px;
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
  width: 240px;
  height: 90px;
  cursor: pointer;
  transition: background linear 0.5s;
}
.button-map{
  background: white;
  border-radius: 20px;
  border: none;
  width: 240px;
  height: 90px;
  cursor: pointer;
  transition: background linear 0.5s;
}
.button-menu{
  background: white;
  border-radius: 20px;
  border: none;
  width: 240px;
  height: 90px;
  cursor: pointer;
  transition: background linear 0.5s;
}
.button-to_book{
  background: white;
  border-radius: 20px;
  border: none;
  width: 240px;
  height: 90px;
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
.button-menu:hover{
  background-color: black;
  color:white;
}
.button-to_book:hover{
  background-color: black;
  color:white;
}



</style>