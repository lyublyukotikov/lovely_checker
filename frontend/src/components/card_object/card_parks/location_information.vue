<template>
  <div class="location_information_parks" >
  
    <ul>
      <li>Адрес: {{info_timetable_card_parks.address}}</li>
      <li>Часы работы:{{info_timetable_card_parks.opening_hours}}</li>
      <li>Телефон: {{info_timetable_card_parks.telephone}}</li>
      <li>Дата основания:{{info_timetable_card_parks.date_of_foundation}}</li>
      <li>Наличие детских площадок:{{info_timetable_card_parks. availability_of_playgrounds}}</li>
      <li>Наличие спортивных площадок: {{info_timetable_card_parks.availability_of_spordgrounds}}</li>
    </ul>
  
</div>
</template>

<script>
export default {
  name:'location_information',
  components: {
  },
  data(){
    return{
     
    }

  },
  props: {
    info_timetable_card_parks:{
      type:Object,
      default(){
        return{}
      }
    },


  },
}


</script>

<style>


.location_information_parks li{
  list-style-type:none;/*убираем точки*/
  margin-bottom:20px ;
}


</style>