<template>
  <div class="location_information_theater" >
  
    <ul>
      <li>Адрес: {{info_timetable_card_theater.address}}</li>
      <li>Часы работы:{{info_timetable_card_theater.opening_hours}}</li>
      <li>Телефон: {{info_timetable_card_theater.telephone}}</li>
      <li>Дана Основаная: {{info_timetable_card_theater.date_of_foundation}}</li>
    </ul>
  
</div>
</template>

<script>
export default {
  name:'location_information_theater.vue',
  components: {
  },
  data(){
    return{
     
    }

  },
  props: {
    info_timetable_card_theater:{
      type:Object,
      default(){
        return{}
      }
    },


  },
}


</script>

<style>


.location_information_rest li{
  list-style-type:none;/*убираем точки*/
  margin-bottom:20px ;
}


</style>