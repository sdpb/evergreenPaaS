<template>
  <div>
    <h1>Listado de elementos</h1>
    <ul>
      <li v-for="(elemento, index) in elementos" :key="index">
        <input type="text" v-model="elemento.nombre" ref="input{{elemento.id}}">
        <button @click="cambiarNombre(elemento)">Cambiar nombre</button>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      elementos: [],
    };
  },
  created() {
    axios.get('http://40.118.66.81/api/listar_archivos')
      .then(response => {
        this.elementos = response.data;
      })
      .catch(error => {
        console.error(error);
      });
  },
  methods: {
    cambiarNombre(elemento) {
      elemento.nombre = this.$refs['input' + elemento.id][0].value;
    },
  },
};
</script>
