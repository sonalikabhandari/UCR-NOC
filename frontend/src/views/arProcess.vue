<template>
  <div class="aletheiaProcess">
  <appBar/>
  <Aletheia/>
</div>
</template>


<script>
// @ is an alias to /src
import Aletheia from '@/components/Aletheia.vue';
import appBar from '@/components/appBar.vue';

export default {
  name: 'aletheiaProcess',
  components: {
    appBar,
    Aletheia,
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
