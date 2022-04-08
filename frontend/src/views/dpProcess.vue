<template>
  <div class="dailyPrepProcess">
  <appBar/>
  <dailyPrep/>

</div>
</template>


<script>
// @ is an alias to /src
import dailyPrep from '@/components/dailyPrep.vue';
import appBar from '@/components/appBar.vue';

export default {
  name: 'logout',
  components: {
    appBar,
    dailyPrep,
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
