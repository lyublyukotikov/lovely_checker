<template>
  <div class="wrapper">
  <div class="sendtome">
    
        <div class="sendtome-inner">
            <h1 class="sendtome-title">Увеличим поток клиентов вашему заведению!</h1>
            <p>У вас нет сайта со своим заведением?</p>
            <p>Вы уверены в качестве своего продукта?</p>
            <h1 class="sendtome-title">Вам к нам!</h1>
            <button type="button" name="button" class="sendtome-btn">Оставить заявку</button>
      </div>
    </div>
  </div>




</template>


<script>
export default {
  name:'marketing_main_page',
  components: {

    
    
    
   
   
  },
}




</script>


<style>
.combine
{
  display: flex;
  align-items: center;
}
.sendtome
{
  margin-bottom: 200px;
  padding: 20px;
}

.sendtome-inner
{
  display: flex;
  flex-direction:column;
  align-items: center;
}

.sendtome-title
{
  font-family: 'Inter';
font-style: normal;
font-weight: 400;
font-size: 18px;
line-height: 22px;
}
.sendtome-inner p{

margin-top: 12px;
margin-bottom: 12px;
  font-family: 'Inter';
  font-style: normal;
  font-weight: 400;
  font-size: 16px;
  line-height: 19px;

  color: #8F8C8C;

}
.sendtome-btn{
  width: 186px;
  height: 38px;
  background: #D9D9D9;
border-radius: 20px;
font-size: 14px;
border: none;
margin-top: 15px;
cursor: pointer;
transition: background linear 0.5s;
}

.sendtome-btn:hover{
background-color: black;
color: white;
}




</style>