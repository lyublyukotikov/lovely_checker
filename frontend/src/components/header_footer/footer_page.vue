<template>

  <div class="footer">
   <div class="container">
  <div class="inner-footer">
  
  <div class="PR">
    <p class="subscribe">Подпишитесь на нашу рассылку<br>
      и узнавайте о новых местах<br> своего города  быстрее
    </p>
   <div class="form_2">
      <input class="form__input_2" type="search" placeholder="Введите свою почту">
      <button class="form__link_2">отправить</button>
    </div>
  </div>
  <div class="list">
    <ul>
      <li><a class="items" href="#">Информация</a></li> 
      <li><a class="items" href="#">О сервисе</a></li>
      <li><a class="items" href="#">Избранное</a></li>
      <li><a class="items" href="#">Акции</a></li>
      <li><a class="items" href="#">Новые места</a></li>
    </ul>
  </div>
  <div class="list">
    <ul>
      <li><a class="items" href="#">Рестораны</a></li>
      <li><a class="items" href="#">Спорт Бары</a></li>
      <li><a class="items" href="#">Школы</a></li>
      <li><a class="items" href="#">Парки</a></li>
      <li><a class="items" href="#">Больницы</a></li>
    </ul>
  </div>
  <div class="social_media">
    <a href="#"><img class="vk" src="../../assets/vk.svg" alt="#"></a>
    <a href="#"><img class="ins" src="../../assets/instagram.svg" alt="#"></a>
  </div>
</div>
</div>
</div>



</template>

<script>
export default {
  name: 'footer_page',
  props: {
   
  }
}
</script>

<style>
.inner-footer{
  width : 1000px;
   border-radius: 20px;
   padding-top: 20px;
 
   padding-right: 15px;
   padding-left: 15px;
   overflow:hidden ;
   display: flex;
   justify-content:space-around;
   align-items: center;
 margin: 0 auto;
 }
.footer{
  background-color:#D9D9D9;
}

.PR{
position: relative;
}

.subscribe{
color: #2F3035; 
padding-bottom: 10px;
}
li{
list-style-type: none;
padding-bottom: 5px;
}
.items{
text-decoration: none;
padding-top: 5px;
color: #2F3035;
list-style-type: none;
}

.form__input_2{
width: 190px;
  height: 38px;
  border-radius: 9px;
  border: none;
  outline: solid white;
}
.list{
padding-top: 30px;
}
.form__link_2{
text-decoration: none;
  color: white;
  background:#30403E;
  border-radius: 25px;
  display: inline-block;
  padding: 12px 6px ;
  position: absolute;
  right: 0;
  border: none;
}
.social_media{
padding-top: 60px;
}
</style>


