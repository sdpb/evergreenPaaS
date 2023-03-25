<template>
  <div id="app">
    <img alt="Analytics logo" src="https://www.irisidea.com/wp-content/uploads/2017/11/datapump_3.png">
    <Ingestion msg="Analytics data ingestion"/>
  </div>
</template>

<script>
import Ingestion from './components/Ingestion.vue'

export default {
  name: 'App',
  components: {
    Ingestion
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 30px;
}
</style>
