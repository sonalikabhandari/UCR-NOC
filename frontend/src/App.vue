<template>
  <div id="app">
  <v-app  v-bind:style="{ background: activeColor}">
    <router-view/>
  </v-app>
  </div>
</template>

<script>

export default {
  computed: {
  },
  data() {
    return {
      activeColor: '#ECEFF1',
    };
  },
};
</script>

<style>
 .app {
 background: yellow;
 }

</style>
