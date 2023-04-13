<!-- <template>
  
  <div class="wrapper">
  <div class="sorting_commentaries">
    <div class="top">
      <P>Комментарии <a href="#"></a></P>
    </div>
    <select id="selectID_3">
      
    
      <option value=”last”>Последнии</option>
      
      <option value=”up”>По возрастанию(оценка)</option>
      
      <option value=”down”>По убыванию(оценка)</option>
      
      </select>
    </div>


  
  <div class="comment_Form">
    <p class="leave_review" >Оставить отзыв</p>

  <form @submit.prevent="submitComment" class="form_user">
    <div class="user_data_button">
      <div class="bottom">
        <div class="user"></div>
        <div class="name_login_user">
        <p class="name_user" >Артем Новиков</p>
        <p class="login_user">krutoyChel228322</p>
      </div>
        
      </div>
    
    
  </div>
    <textarea  v-model="message" placeholder="Ваш комментарий" class="users_message"></textarea>
    <div class="to_sent">
    <button><img src="" alt=""></button>
  </div>
  </form>
</div>
</div>

</template>

<script>
export default {
  name:'Comment_Form',
  data() {
    return {
      name: '',
      email: '',
      message: ''
    }
  },
  methods: {
    submitComment() {
      const comment = {
        name: this.name,
        email: this.email,
        message: this.message
      }
      this.$emit('comment-added', comment)
    }
  }
}
</script>

<style scoped>
.wrapper{
  width: 1000px;
  margin: 0 auto;
  padding-top: 20px;
  padding-right: 15px;
  padding-left: 15px;
  overflow: hidden;
  background-color: white;
}
.bottom{
  border-radius: 20px;
  background: #D9D9D9;
  width: 920px;
 
  display: flex;
 
  gap: 30px;
 
}

.user{
  width:46.36px;
height: 45px;
background: black;
border-radius: 45%;

}
.leave_review{
 padding: 20px 0px 0px 20px;


color: #000000;
}
.sorting_commentaries{
  display: flex;
  text-align: center;
    align-items: center;
    gap: 20px;
    margin-left: 30px;
}
.comment_Form{
  width: 960px;
  height: 410px;
  border-radius: 20px;
background-color: #D9D9D9;

margin: 0 auto;

}
.user_data_button{
display: flex,


}
.top{
  display: flex;
  text-align: center;
  
  
}

.top a{
  text-decoration: none;
  color: rgba(102, 102, 102, 1);
}

#selectID_3{
  
  border-radius:20px;
  border: 1px solid black;
  outline: none;
  
 
  width: 205px;
  height: 32px;
  
}
.user_email{
  margin-left: 30px;
  border-radius: 5px;
  padding: 5px;
}
.user_name{
  border-radius: 5px;
  padding: 5px;
  margin-left: 10px;
}

.users_message{
  width: 920px;
  height: 203px;
  border-radius: 20px;
  background-color: white;
  display: flex;
  justify-content: center;
  margin: 0 auto;
}
.to_sent{
display: flex;
justify-content: end;
}
.form_user button{
width: 100px;
height: 42px;
background-color: black;
border-radius: 20px;

}

</style> -->