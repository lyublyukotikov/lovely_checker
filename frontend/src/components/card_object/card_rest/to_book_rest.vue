<template>
<div class="to_book_rest">
  
    <ul class="list">
        <li><button  class="button choice-button" @click="buttonClicked(1)">1</button></li>
        <li><button  class="button choice-button" @click="buttonClicked(2)">2</button></li>
        <li><button  class="button choice-button" @click="buttonClicked(3)">3</button></li>
        <li><button  class="button choice-button" @click="buttonClicked(4)">4</button></li>
        <li><button  class="button choice-button" @click="buttonClicked(5)">5</button></li>
        <li><button  class="button choice-button" @click="buttonClicked(6)">6</button></li>
        <li><button  class="button choice-button" @click="buttonClicked(7)">7</button></li>
        <li><button  class="button choice-button" @click="buttonClicked(8)">8</button></li>
        <li><button  class="button choice-button" @click="buttonClicked(9)">9</button></li>
        <li><button  class="button choice-button" @click="buttonClicked(10)">10</button></li>
        <li><button  class="button choice-button" @click="buttonClicked(11)">11</button></li>
        <li><button  class="button choice-button" @click="buttonClicked(12)">12</button></li>
        <li><button  class="button choice-button" @click="buttonClicked(13)">13</button></li>
        <li><button  class="button choice-button" @click="buttonClicked(14)">14</button></li>
        <li><button  class="button choice-button" @click="buttonClicked(15)">15</button></li>
        <li><button class="button choice-button" @click="buttonClicked(16)">16</button></li>
        <li><button  class="button choice-button" @click="buttonClicked(17)">17</button></li>
        <li><button  class="button choice-button" @click="buttonClicked(18)">18</button></li>
        <li><button  class="button choice-button" @click="buttonClicked(19)">19</button></li>
        <li><button  class="button choice-button" @click="buttonClicked(20)">20</button></li>
        <li><button  class="button choice-button" @click="buttonClicked(21)">22</button></li>
        <li><button  class="button choice-button" @click="buttonClicked(22)">22</button></li>
        <li><button  class="button choice-button" @click="buttonClicked(23)">23</button></li>
        <li><button  class="button choice-button" @click="buttonClicked(24)">24</button></li>
        <li><button  class="button choice-button" @click="buttonClicked(25)">25</button></li>
        <li><button  class="button choice-button" @click="buttonClicked(26)">26</button></li>
        <li><button  class="button choice-button" @click="buttonClicked(27)">27</button></li>
        <li><button  class="button choice-button" @click="buttonClicked(28)">28</button></li>
        <li><button  class="button choice-button" @click="buttonClicked(29)">29</button></li>
    </ul>
    <div class="list-inner">
      <h3>Забронировать столик № {{buttonValue}}</h3>
       
        <button class="button">Да</button>
    </div>

  </div>

</template>


<script>
export default {
  name: 'to_book_rest',
  components:{
  
  },
  data(){
    return{  
      buttonValue: '',
    }

  },
  methods: {
  buttonClicked(value) {
    this.buttonValue = value;
  }
}
  

}
</script>

<style scopedx>

.list button{

 
  border: none;
  color:black; 
  padding: 20px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer;
  border-radius: 50%;
  outline: none;
  position: relative;
  overflow: hidden;
  background: none;
  transition: 0.5s;
}


.list
{
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  
}




.people-input{
    border: none;
    font-size: 25px;
    width: 30px;
    font-weight:bold;
}


.list-inner{
  display: flex;
  align-items: center;
  text-align: center;
  margin-left: 150px;
 
}
.button{
  padding: 20px;
  border: none;
  margin-left: 30px;
  border-radius: 45%;
  cursor: pointer;
  transition: background linear 0.5s;
  background-color: #BCBBBB;

}
.button:hover {
  background-color:black;
  color:white;
}



</style>