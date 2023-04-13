<template>
  <div class="location_information_rest" >
  
    <ul>
      <li>Адрес: {{info_timetable_card_rest.address}}</li>
      <li>Часы работы:{{info_timetable_card_rest.opening_hours}}</li>
      <li>Телефон: {{info_timetable_card_rest.telephone}}</li>
      <li>цена:{{info_timetable_card_rest.  prace}}</li>
      <li>Парковка: {{info_timetable_card_rest.parking}}</li>
    </ul>
  
</div>
</template>

<script>
export default {
  name:'location_information_rest.vue',
  components: {
  },
  data(){
    return{
     
    }

  },
  props: {
    info_timetable_card_rest:{
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