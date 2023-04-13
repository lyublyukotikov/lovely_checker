<template>
  <div class="card_parks_catalog_item">
    
    <img class="img_card" src="../../assets/img_card_catalog/5.jpg" alt="img">
 
    <p class="item_1_name">{{card_parks_catalog_item.name}}</p>
    <p class="item_2_category">{{card_parks_catalog_item.categories}} </p>
    <p class="number_of_reviews">Отзывов: {{card_parks_catalog_item.number_of_reviews}}</p>

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

  </div>
</template>
<script>

export default {
  name: 'card_parks_catalog_item',
  props:{
    card_parks_catalog_item:{
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
<style scoped>
.img_card{
  width: 260px;
  height: 264px;
}
.card_parks_catalog_item{
 
  flex-basis:25%;
  background-color: black;


  border-radius:20px ;
  padding:16px ;
  margin-bottom:16px ;

}
.item_2_category{
  color:#4E4E4E ;
}
.item_1_name{
  color: white;
}
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
  background: url('../../../assets/img_star/Star_card_full.svg')center no-repeat;
}
.star--outlined{
  background: url('../../../assets/img_star/Star_card_empty.svg') center no-repeat;
}
.number_of_reviews{
  color:white;
}

</style>
