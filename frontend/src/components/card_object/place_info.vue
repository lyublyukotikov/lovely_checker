<template>
  
  <div class="wrapper">
    <h1>{{categies. title_place_info}}</h1>
  <div class="section_1">
    <div class="star-rating"  >
     
      <span class="star star--outlined" v-for="index in starLimit"
      :key="index" 
      ></span>
      <div class="star-rating __colored" :style="ratingWidthStyle">
        <span class="star star--colored" v-for="index in starLimit"
        :key="index"  
        ></span> 
      </div>
     </div>
  
    <div class="rating">
        <a href="">4.4 <a href="#app_comment">(5 отзывов) </a> </a>
  </div>
    <div class="namber_categori">
      Представитель категории: {{categies.type_of_category}}
    </div>
    <div class="favorite">
       <a href="#">Добавить в избранное<img src="../../assets/heart.svg" alt="#"></a>  
    </div>
  </div>
  
 
  <div class="section_2">
    
  </div>
</div>





</template>

<script>


export default {
  name: 'place_info',
  components:{
    
  },
 

  props: {
    categies:{
      type:Object,
      default(){
        return{}
      }
    },
    number:{
      type:Number,
      default:0
    },
    starLimit:{
      type:Number,
      default:5
    }


  },
   data(){
    return{}
  },
  computed:{
    ratingWidth(){
      return this.number/this.starLimit*100
    },
    ratingWidthStyle(){
      return `width: ${this.ratingWidth}%;`
    }
  }

  
}


</script>



<style>

/* Star */
.star-rating{
  position: relative;
  display: inline-flex;
}
.__colored{
  display: inline-flex;
  position: absolute;
  width: 0;
  height: 100%;
  top: 0;
  left: 0;
  overflow: hidden;
}
.star{
  color: white;
  display: inline-block;
  width: 16px;
  height: 16px;
  margin: 0 3px;
  flex-shrink: 0;
  
    
}
.star--colored{
  background: url('../../assets/img_star_car_object/star_full.svg')center no-repeat;
}
.star--outlined{
  background: url('../../assets/img_star_car_object/star_empty.svg') center no-repeat;
}
/* Section_1 */
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

h1{
  margin-top: 71px;
}

.section_1{
  margin-bottom: 20px;
display: flex;
 align-items: center;
 justify-content: space-between;
}

.rating a{
  text-decoration: none;
  color: rgba(102, 102, 102, 1);
  
}

.favorite a{
  text-decoration: none;
  color:black ;
}

/* Section_2 */
.section_2{
  margin: 0 auto;
  height: 491px;
  width: 920px;
  border-radius: 20px;
  border: 1px solid black;
  background: url('../../assets/page_infro_images/1.jpg') center no-repeat;

  
 
   
    
}
.section_2 img{
  width: 100%;
  height: 100%;
  object-fit: contain;
}
/* section_3 */


/* Selection_4 */
.selection_4{
  width: 920px;
  height: 336px;
  border-radius: 20px;
  background: #D9D9D9;
  margin: 0 auto;
}
.section_4 user{
  display:flex;
}


.wrapper-input{
  width: 920px;
  height: 230px;
  border-radius: 20px;
  background-color: white;
  display: flex;
  margin-top: 110px;
  display: inline-block;
}

.wrapper-input input{
  width: 860px;
  height: 128px;
}






</style>