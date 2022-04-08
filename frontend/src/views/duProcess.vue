<template>
  <div class="dailyUpdateProcess">
  <appBar/>
  <dailyupdate/>
  </div>
  </template>


<script>
// @ is an alias to /src
import dailyupdate from '@/components/dailyupdate.vue';
import appBar from '@/components/appBar.vue';


export default {
  name: 'dailyUpdateProcess',
  components: {
    appBar,
    dailyupdate,

  },
  mounted() {
    this.checkLoggedIn();
  },
  data() {
    return {
      activeColor: '#EEEEEE',
    };
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

<style scoped>

{
.theme--light .v-card {
  border-left: 5px solid red !important;
}

}


</style>
