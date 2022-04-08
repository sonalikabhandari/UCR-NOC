<template>
  <div class="dailyUpdateProcess">
    <h5 class="heading indigo--text mt-8 pt-8 mx-7">
    <b><u><i>Daily Update Process:</i></u></b></h5>
    <v-layout row wrap>
    <v-flex xs6 sm4 md3 xl6 class="lg3-custom">
    <v-container grid-list-xs mx-5 px-5 mt-0 pt-0>
    <v-layout column>
    <v-content>
    <v-card-title class="red lighten-3 black--text">RRD Data Insert</v-card-title>
     <v-card color="#FFCDD2" flat v-for="process in processesRRD" :key="process.SeqNum">
     <v-flex>
     <v-list-item three-line>
     <v-list-item-content>
     <v-list-item
     class="font-weight-medium">{{ process.ProcessName }}</v-list-item>
     <v-list-item class = "font-weight-medium font-italic" v-bind:class =
     '{ "style:bgcolor = pink lighten-3": process.ProcessStatus == "Not Started",
     "yellow lighten-3": process.ProcessStatus == "Running",
     "green lighten-3": process.ProcessStatus == "Completed"}'>
     {{process.ProcessStatus}}</v-list-item>
      <v-list-item class=" teal accent-1 font-italic">{{process.LastUpdated }}</v-list-item>
       </v-list-item-content>
      </v-list-item>
      <v-divider inset></v-divider>
  </v-flex>
  </v-card>
  </v-content>
  </v-layout>
  </v-container>
  </v-flex>

  <v-flex xs6 sm4 md3 xl6 class="lg3-custom">
  <v-container grid-list-xs mx-5 px-5 mt-0 pt-0>
  <v-layout column>
  <v-content>
  <v-card-title class="red lighten-3 black--text">Rolling P95 Calculation</v-card-title>
   <v-card color="#FFCDD2" flat v-for="process in processesRP95" :key="process.SeqNum">
   <v-flex>
   <v-list-item three-line>
   <v-list-item-content>
   <v-list-item
   class="font-weight-medium">{{ process.ProcessName }}</v-list-item>
   <v-list-item class = "font-weight-medium font-italic" v-bind:class =
   '{ "style:bgcolor = pink lighten-3": process.ProcessStatus == "Not Started",
   "yellow lighten-3": process.ProcessStatus == "Running",
   "green lighten-3": process.ProcessStatus == "Completed"}'>
   {{process.ProcessStatus}}</v-list-item>
    <v-list-item class=" teal accent-1 font-italic">{{process.LastUpdated }}</v-list-item>
     </v-list-item-content>
    </v-list-item>
    <v-divider inset></v-divider>
</v-flex>
</v-card>
</v-content>
</v-layout>
</v-container>
</v-flex>

<v-flex xs6 sm4 md3 xl6 class="lg3-custom">
<v-container grid-list-xs mx-5 px-5 mt-0 pt-0>
<v-layout column>
<v-content>
<v-card-title class="red lighten-3 black--text">WAE Merge</v-card-title>
 <v-card color="#FFCDD2" flat v-for="process in processesWAE" :key="process.SeqNum">
 <v-flex>
 <v-list-item three-line>
 <v-list-item-content>
 <v-list-item
 class="font-weight-medium">{{ process.ProcessName }}</v-list-item>
 <v-list-item class = "font-weight-medium font-italic" v-bind:class =
 '{ "style:bgcolor = pink lighten-3": process.ProcessStatus == "Not Started",
 "yellow lighten-3": process.ProcessStatus == "Running",
 "green lighten-3": process.ProcessStatus == "Completed"}'>
 {{process.ProcessStatus}}</v-list-item>
  <v-list-item class=" teal accent-1 font-italic">{{process.LastUpdated }}</v-list-item>
   </v-list-item-content>
  </v-list-item>
  <v-divider inset></v-divider>
</v-flex>
</v-card>
</v-content>
</v-layout>
</v-container>
</v-flex>

<v-flex xs6 sm4 md3 xl6 class="lg3-custom">
<v-container grid-list-xs mx-5 px-5 mt-0 pt-0>
<v-layout column>
<v-content>
<v-card-title class="red lighten-3 black--text">UCR Preparation</v-card-title>
 <v-card color="#FFCDD2" flat v-for="process in processesUCR" :key="process.SeqNum">
 <v-flex>
 <v-list-item three-line>
 <v-list-item-content>
 <v-list-item
 class="font-weight-medium">{{ process.ProcessName }}</v-list-item>
 <v-list-item class = "font-weight-medium font-italic" v-bind:class =
 '{ "style:bgcolor = pink lighten-3": process.ProcessStatus == "Not Started",
 "yellow lighten-3": process.ProcessStatus == "Running",
 "green lighten-3": process.ProcessStatus == "Completed"}'>
 {{process.ProcessStatus}}</v-list-item>
  <v-list-item class=" teal accent-1 font-italic">{{process.LastUpdated }}</v-list-item>
   </v-list-item-content>
  </v-list-item>
  <v-divider inset></v-divider>
</v-flex>
</v-card>
</v-content>
</v-layout>
</v-container>
</v-flex>

</v-layout>
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
      processesRRD: [],
      processesRP95: [],
      processesWAE: [],
      processesUCR: [],
    };
  },
  methods: {
    getProcessRRD() {
      axios.get('alt/api/DailyUpdateRRD/')
        .then((res) => {
          (this.processesRRD = res.data);
        })
        .catch((err) => {
          console.log(err);
        });
    },
    getProcessRP95() {
      axios.get('/alt/DailyUpdateRP95/')
        .then((res) => {
          (this.processesRP95 = res.data);
        })
        .catch((err) => {
          console.log(err);
        });
    },
    getProcessWAE() {
      axios.get('alt/DailyUpdateWAE/')
        .then((res) => {
          (this.processesWAE = res.data);
        })
        .catch((err) => {
          console.log(err);
        });
    },
    getProcessUCR() {
      axios.get('alt/DailyUpdateUCR/')
        .then((res) => {
          (this.processesUCR = res.data);
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  created() {
    this.getProcessRRD();
    this.getProcessRP95();
    this.getProcessWAE();
    this.getProcessUCR();
    setInterval(this.getProcessRRD(), 30000);
    setInterval(this.getProcessRP95(), 30000);
    setInterval(this.getProcessWAE(), 30000);
    setInterval(this.getProcessUCR(), 30000);
  },
};
</script>

<style>

{
@media (min-width: 1264px) and (max-width: 1903px) {
    .flex.lg3-custom {
        width: 10%;
        max-width: 10%;
        flex-basis: 10%;
    }
}
}

</style>
