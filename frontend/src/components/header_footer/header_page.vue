<template>
  <!-- Header_first -->
  <div class="header-wrapper_header_first">
    <div class="container">
 
    <div class="header-first">
     
      <H3> <Router-link to="/">Lovely Checker</Router-link></H3>
      <div class="form">
      <input class="form__input" type="search" placeholder="Искать на Lovely Checker">
      <button class="form__link"><img  src="../../assets/search_header.svg" alt="#"></button>
       </div>
       
      <select id="selectID_2">
  
        <option value=”last”>Таганрог</option>
        
        <option value=”up”>Ростов-на-дону</option>
        
        <option value=”down”>Астрахань</option>
        
        </select>
     
      <div class="profile">
        <div class="profile-img"></div>
        
      <select id="selectID">
  
        <option value=”GR”>вход/регистрация</option>
        
        <option value=”YE”>Избранное</option>
        
        <option value=”BL”>добавить заведение</option>
        <option value=”BL”>о сервесе</option>
        
        </select>
      </div>
    </div>
  </div>
</div>
 
  <!-- header second -->
  
  <div class="header-wrapper_header_second">
    <div class="container">

    <div class="header-second">
   
      <ul>
        <li><div class="header_second_li"> <router-link to="/card_catalog_theater_wrapper">Театры/Кино</router-link></div></li>
          <li><div class="header_second_li"><router-link to="">Музеи/Галереи</router-link></div></li>
          <li><div class="header_second_li"><router-link to="/card_catalog_parks_wrapper">Парки/Скверы</router-link></div> </li>
          <li><div class="header_second_li"><router-link to="/card_catalog_rest_wrapper">Кафе/Рестораны</router-link></div></li>
          <li><div class="header_second_li"><router-link to="/card_catalog_hotel_wrapper">Отели</router-link></div></li>
          <li><div class="header_second_li"><router-link to="">Другое</router-link></div></li>
        </ul> 
      </div>
    </div>
  </div>
  

</template>

<script>
export default {
  name: 'header_page',
  props: {
   
  }
}



</script>



<style>
.container
{
  width:100%;
  max-width: 1200px;
  margin: 0 auto;
}


.header-wrapper_header_first{
  width:1354px;
 background-color: #D9D9D9;
  overflow: hidden;
  margin: 0 auto;
  border-radius: 20px;
}

.header-wrapper_header_second{
  width:1354px ;
  background-color: #BCBBBB;
  overflow: hidden;
  margin: 0 auto;
  border-radius: 20px;
}

.header-first{
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin: 0 auto;
  max-width:1000px ;
  max-height: 74px;
}

.header-second{
  background-color: #BCBBBB;
  max-width: 1000px;
  margin: 0 auto;
 max-height:64px ;
}

.header_second_li  a { 
  width: 157px;
  height:  29px;
 border-radius: 20px;
  background-color: #BCBBBB ;
  text-align: center;
  padding: 10px;
  cursor: pointer;
  transition: background linear 0.5s;
}

.header_second_li a:hover {
  background-color:black;
  color:white;
}

.header-second ul{
  display: flex;
  text-align: center;
  margin-left:35px ;
  margin-right: 35px;
  justify-content: space-between;
  list-style-type:none;/*убираем точки*/
}

.header-second a{
  text-decoration: none;
  color: #000000;
}

.form{
  position: relative;
  display: flex;
  align-items: center;
}

.form__input{
  outline:none;
  border:none;
  width: 300px;
  height: 30px;
  border-radius: 20px;
  padding-left: 30px;
}
.form__link{
  background-color:transparent ;
 border: none;
 height: 30px;
  background-repeat: no-repeat;
  right: 0px;
  position: absolute;
}

#selectID_2{
  background-color: #D9D9D9;
  outline:none;
  border-color:black;
 
  height: 30px;
  border-radius: 20px;
}

.profile{
  display: flex;
  align-items: center;
  background-color: #B7B7B7;
  width: 95px;
  height: 44px;
  border-radius: 35px;
  
}

#selectID{
  width: 15px;
  height: 13.42px;
  border-radius: 20px;
  border: none;
  
  background-color: #B7B7B7;
  outline:none;
}

.profile-img{
  width: 30px; 
height: 30px;
background: rgba(102, 102, 102, 1);
border-radius: 50%;
margin-right: 5px;
margin:0px 22px 0px 10px;
}




</style>