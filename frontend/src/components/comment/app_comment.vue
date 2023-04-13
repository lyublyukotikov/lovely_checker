<!-- <template>
  <div id="app_comment">
    <Comment_Form @comment-added="addComment"/>
    <Comments_List :comments="comments"/>
   
  </div>
</template>

<script>
import Comment_Form from '../comment/Comment_Form.vue'
import Comments_List from '../comment/Comments_List.vue'

export default {
  components: {
    Comment_Form,
    Comments_List
  },
  data() {
    return {
      comments: []
    }
  },
  methods: {
    addComment(comment) {
      this.comments.push(comment)
    }
  }
}
</script>

<style>



</style> -->

<template>
  <div class="wrapper">
    <h1>Отправить отзыв</h1>
    <div class="comments">
    <div class="name">
      <label>Имя:</label>
      <div>{{ review.firstName }}</div>
    </div>
    <div class="sername">
      <label>Фамилия:</label>
      <div>{{ review.lastName }}</div>
    </div>
    <div class="email">
      <label>Электронная почта:</label>
      <div>{{ review.email }}</div>
    </div>
    <div class="photo">
      <label>Фото:</label>
      <input type="file" ref="fileInput" @change="handleFileUpload()" accept="image/*">
    </div>
    <div class="rating">
      <label>Оценка:</label>
      <div>{{ review.rating }}</div>
    </div>
    <div class="user_comm">
      <label>Комментарий:</label>
      <textarea v-model="review.comment"></textarea>
    </div>
  
    <div class="btn_comm">
      <button @click.prevent="submitReview()">Отправить</button>
    </div>
  </div>
    <div v-if="reviews.length">
      <h2>Отзывы:</h2>
      <div v-for="review in reviews" :key="review.id">
        <div>{{ review.firstName }} {{ review.lastName }}</div>
        <div>{{ review.email }}</div>
        <div v-if="review.photo">
          <img :src="review.photo" alt="Отзыв"/>
        </div>
        <div>Оценка: {{ review.rating }}</div>
        <div>Комментарий: {{ review.comment }}</div>
        <hr>
      </div>
    </div>
  </div>
</template>

<script>


export default {
  components: {
    
  },
  data() {
    return {
      review: {
        firstName: '',
        lastName: '',
        email: '',
        photo: null,
        rating: 0,
        comment: ''
      },
      reviews: []
    }
  },
  mounted() {
    this.loadUserReview();
    this.loadReviews();
  },
  methods: {
    loadUserReview() {
      // Получить данные пользователя из JSON файла
      // и обновить review объект
    },
    handleFileUpload() {
  const file = this.$refs.fileInput.files[0];
  const reader = new FileReader();
  reader.readAsDataURL(file);
  reader.onload = () => {
    this.review.photo = reader.result;
  };
},
   
    submitReview() {
  // Отправка отзыва на сервер
  // Обновить review объект
  // Добавить отправленный отзыв в список отзывов
  this.reviews.push(this.review);
  // Сбросить поле выбора файла и объекта review.photo
  this.$refs.fileInput.value = '';
  this.review.photo = null;
  // Очистить review объект
  this.review = {
    firstName: '',
    lastName: '',
    email: '',
    rating: 0,
    comment: ''
  };
},
    loadReviews() {
      // Получить список отзывов
      // и обновить reviews массив
    }
  }
}
</script>

<style>
.user_comm{
 padding-right: 30px;
}



.wrapper {
  max-width: 960px;
  margin: 0 auto;
  padding: 20px;
  font-family: Arial, sans-serif;
  color: #333;
}

h1 {
  font-size: 32px;
  margin-bottom: 20px;
}

.comments {
  
  
  background-color: #D9D9D9;
  display: flex;
  flex-wrap: wrap;
height: 336px;
margin: 0 auto;
border-radius: 10px;
padding: 30px;
}

.comments > div {
  margin-bottom: 10px;
  flex-basis: 50%;
}

.comments label {
  display: inline-block;
  width: 120px;
  margin-right: 10px;
  font-weight: bold;
}

.comments input[type="file"] {
  margin-top: 10px;
}

.comments textarea {
  height: 137px;
  width: 900px;
  padding: 10px;
  resize: vertical;
  border-radius: 20px;
}

.comments button {
  background-color: #008CBA;
  color: #fff;
  border: none;
  padding: 10px 20px;
  border-radius: 5px;
  cursor: pointer;
}

.comments button:hover {
  background-color: #006B8E;
}

h2 {
  font-size: 24px;
  margin-top: 40px;
  margin-bottom: 20px;
}

img {
  max-width: 100%;
  height: auto;
  border-radius: 5px;
  margin-top: 10px;
}

hr {
  border: none;
  border-top: 1px solid #ddd;
  margin-top: 20px;
}


</style>