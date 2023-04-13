

<template>
  <div id="app">
    <header_page/>
    
    <RouterView/>
    <footer_page/>

  <!-- <test></test> -->
  </div>
  

  
</template>



<script >

// import test from './components/test.vue';
import header_page from './components/header_footer/header_page.vue'
import footer_page from './components/header_footer/footer_page.vue'

export default {
  name:'app',
  components: {
    // test,
    header_page,
    footer_page

  
  }
}

</script>




<style>

#app {
  font-family: 'Inter', sans-serif;
  background-color:  #ECECEC;;
 
  
  
 
  
  
}


</style>
