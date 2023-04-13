<!-- <template>
  <div class="wrapper">
    
    <div v-if="comments.length === 0">Комментариев пока нет</div>
    <div v-else>
      
      <div v-for="(comment, index) in comments" :key="index">
        <div class="comments">
          <div class="comments_input">
        <strong>{{comment.name}}:</strong>
        <p>{{comment.message}}</p>
      </div>
      </div>
    </div>
  </div>
</div>
  
</template>

<script>
export default {
  name:'Comments_List',
  props: ['comments'],

data(){
    return{
      "comment": [
  { id:"1",
    name:'иван'
  
  
    
  },
  
]
    }
  }




}

</script>


<style>
.comments{
 width: 960px;
height: 207px;
border-radius: 20px;
background-color:#D9D9D9;
margin-bottom: 30px;


}
.comments_input{
  width: 920px;
  height:115px ;
  border-radius: 20px;
  background-color: white;
  margin: 0 auto;
  justify-content: center;
 
  
}



</style> -->