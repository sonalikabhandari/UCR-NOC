<template>
  <div class="aletheiaProcess">
  <h5 class="heading indigo--text mt-12 pt-12 mx-7">
  <b><u><i>Aletheia/Rancid Process:</i></u></b></h5>
  <v-container grid-list-xl mr-5 pr-5 ml-1 pl-1 mt-5 pt-5>

    <v-layout align-center justify start>
    <v-flex xs12 sm6 md4 lg3 class= "ml-5" v-for="process in processes" :key="process.SeqNum">
      <v-card color="#BBDEFB" flat>
      <v-card-title class="blue lighten-3 black--text">
      {{process.ProcessName}}</v-card-title>
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
  name: 'aletheiaProcess',
  components: {

  },
  data() {
    return {
      processes: [],
    };
  },
  methods: {
    getProcess() {
      axios.get('/alt/aletheia/')
        .then((res) => {
          (this.processes = res.data);
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  computed: {

  },
  created() {
    this.getProcess();
    setInterval(this.getProcess(), 30000);
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
