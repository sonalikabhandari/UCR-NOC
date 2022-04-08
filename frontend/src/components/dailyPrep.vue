<template>
  <div class="dailyPrepProcess">
    <h5 class="heading indigo--text mt-8 pt-8 mx-7">
    <b><u><i>Daily Preparartion Process:</i></u></b></h5>
    <v-container grid-list-xl mr-5 pr-5 ml-3 pl-3 mt-5 pt-5>
    <v-layout row wrap >
     <v-flex xs3 sm6 md4 lg3 v-for="process in processes" :key="process.name">
      <v-card color="#D7CCC8" flat>
      <v-card-title class="brown lighten-3 black--text">{{process.ProcessName}}</v-card-title>
        <v-list-item two-line>
        <v-list-item-content>
        <v-list-item class = "font-weight-medium font-italic" v-bind:class =
        '{ "style:bgcolor = pink lighten-3": process.ProcessStatus == "Not Started",
        "yellow lighten-3": process.ProcessStatus == "Running",
        "green lighten-3": process.ProcessStatus == "Completed"}'>
        {{process.ProcessStatus}}</v-list-item>
        <v-list-item class=" teal accent-1 font-weight-medium font-italic">
        {{process.LastUpdated }}</v-list-item>
      </v-list-item-content>
     </v-list-item>
    </v-card>
   </v-flex>
  </v-layout>
</v-container>
</div>
</template>


<script>
// @ is an alias to /src
import axios from 'axios';

export default {
  name: 'logout',
  components: {
  },
  data() {
    return {
      processes: [],
    };
  },
  methods: {
    getProcess() {
      axios.get('/alt/DailyPrep/')
        .then((res) => {
          (this.processes = res.data);
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },

  created() {
    this.getProcess();
    setInterval(this.getProcess(), 30000);
  },
};
</script>

<style scoped>

{
h5 {
  background-color: blue-grey lighten-3;
}
}

</style>
