<template>
  <div id="app">
    <mainmenu></mainmenu>
    <!-- <img src="./assets/logo.png"> -->
    <div class="container my-5">
      
      <router-view/>
    </div>
  </div>
</template>

<script>

import mainmenu from './components/mainmenu'

export default {
  name: 'App',
  components: {
    mainmenu
  }
}
</script>

<style>

  html, body, #app { min-height: 100%; background: #f8f9fa!important;  }
/*#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}*/
</style>
