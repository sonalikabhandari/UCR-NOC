<template>
  <div class="homepage">
  <appBar/>
  <h3 class="heading indigo--text mt-12 pt-12 mx-10"><b>Welcome to UCR NOC Audit Page!!</b></h3>
  </div>
  </template>

<script>

import appBar from '@/components/appBar.vue';

export default {
  name: 'Home',
  components: {
    appBar,
  },
  mounted() {
    this.checkLoggedIn();
  },
  methods: {
    checkLoggedIn() {
      this.$session.start();
      if (!this.$session.has('token')) {
        this.$router.push('/');
      }
    },
  },
};
</script>
