<template>
  <div class="Overview">
  <v-app id="inspire">
  <appBar/>
  <aletheia/>
  <dailyprep/>
  <dailyupdate/>
  </v-app>
  </div>
</template>

<script>

import aletheia from '@/components/Aletheia.vue';
import dailyprep from '@/components/dailyPrep.vue';
import dailyupdate from '@/components/dailyupdate.vue';
import appBar from '@/components/appBar.vue';

export default {
  name: 'Overview',
  components: {
    appBar,
    aletheia,
    dailyprep,
    dailyupdate,
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

<style scoped>

{

}


</style>
