<template>
<div class="register">
  <div class="date_of_register_wrapper">
    <p>зарегистрироваться</p>
  <datepicker class="check_in_hotel"
      v-model="selectedDate_check_in_hotel" 
      format="dd.MM.yyyy" 
      language="ru">
    </datepicker>
  </div>
  <div class="exit_hotel_wrapper">
    <p>Выезд</p>
    <datepicker class="exit_hotel"
    v-model="selectedDate_exit_hotel" 
    format="dd.MM.yyyy" 
    language="ru">
  </datepicker>
 </div>
 <div class="number_of_persons_wrapper">
  <p>Количество персон</p>
  <div class="number_of_persons">
    
    <img class="person" src="../../../assets/card_changeable/person.svg" alt="">
    <input class  v-model="count" />
    
    <button class="arrow_left" @click="decrement"><img  src="../../../assets/card_changeable/arrow_left.svg" alt=""></button>
    <button class="arrow_right" @click="increment" ><img  src="../../../assets/card_changeable/arrow_right.svg" alt=""></button>
  
  </div>
</div>
<div class="button_take_off_wrapper">
  <button class="button_take_off">
    забронировать
  </button>
</div>
   

</div>


</template>

<script>
import Datepicker from 'vue3-datepicker'
export default {
  name: 'register',
  components:{
    Datepicker
  },
  data(){
    return{  
      selectedDate_check_in_hotel: null,
      selectedDate_exit_hotel:null,
      count: 0
    }

  },
 
  methods: {
    increment() {
      this.count++
    },
    decrement() {
      this.count--
    }
  },

  

}
</script>


<style>
.register{
  display: grid;
  row-gap: 20px;
  margin:0 auto

}

.check_in_hotel{
  width: 149px;
  height: 46px;
  border-radius: 20px;
  border: 1px solid black;
  padding-left: 30px;


}
.exit_hotel{
  width: 149px;
  height: 46px;
  border-radius: 20px;
  border: 1px solid black;
  padding-left: 30px;
}
.number_of_persons input{
  width: 149px;
  height: 46px;
  border-radius: 20px;
  border: 1px solid black;
  padding-left: 30px;
  outline: none;
}
.number_of_persons{
  position: relative;
  display: flex;
  align-items: center;
}
.person{
  background-color: transparent;
    border: none;
    height: 30px;
    background-repeat: no-repeat;
    left: 4px;
    position: absolute;
}
.arrow_left{
  background-color: transparent;
    border: none;
    height: 30px;
    background-repeat: no-repeat;
    right: 26px;
    position: absolute;
    
}
.arrow_right{
  background-color: transparent;
    border: none;
    height: 30px;
    background-repeat: no-repeat;
    right: 0px;
    position: absolute;
}
.button_take_off {
  background: white;
    border-radius: 20px;
    border: none;
    width: 140px;
    height: 60px;
    cursor: pointer;
    transition: background linear 0.5s;
}
.button_take_off:hover{
  background-color:black;
  color:white;
}

.button_arrow{
  position: absolute;
}
.date_of_register_wrapper{
  display: flex;
 gap: 20px;
 align-items: center;
}
.exit_hotel_wrapper{
  display: flex;
  gap: 20px;
  align-items: center;
}
.number_of_persons_wrapper{
  display: flex;
  gap: 20px;
  align-items: center;
}
.button_take_off_wrapper{
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>