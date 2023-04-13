<template>
  <div class="location_information_hotel" >
  
    <ul>
      <li>Адрес: {{info_timetable_card_hotel.address}}</li>
      <li>Часы работы:{{info_timetable_card_hotel.opening_hours}}</li>
      <li>Телефон: {{info_timetable_card_hotel.telephone}}</li>
      
    </ul>
  
</div>
</template>

<script>
export default {
  name:'location_information_hotel',
  components: {
  },
  data(){
    return{
     
    }

  },
  props: {
    info_timetable_card_hotel:{
      type:Object,
      default(){
        return{}
      }
    },


  },
}


</script>

<style>


.location_information_hotel li{
  list-style-type:none;/*убираем точки*/
  margin-bottom:20px ;
}


</style>