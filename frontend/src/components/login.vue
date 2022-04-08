<template>
<div id="app">
<div class = "login">
    <v-content>
      <v-container fluid fill-height mt-12 pt-12>
      <v-layout align-center justify-center>
        <v-flex xs12 md4 lg5>
            <v-card color="transparent" class="elevation-12">
              <v-toolbar color="blue-grey darken-2" dark flat>
                <v-toolbar-title>Login</v-toolbar-title>
                <v-spacer></v-spacer>
            </v-toolbar>
            <v-card-text>
            <v-form>
              <v-text-field
                label="PID"
                name="PID"
                v-model="credentials.username"
                prepend-icon="mdi-account"
                type="text"
                required
                :rules="[v => !!v || 'PID is required']">
                </v-text-field>
                <v-text-field
                  id="password"
                  label="Password"
                  name="password"
                  v-model="credentials.password"
                  prepend-icon="mdi-lock"
                  type="password"
                  :rules="[v => !!v || 'password is required']"
                  required
                ></v-text-field>
              </v-form>
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="primary" :disabled="!valid" @click="login">Login</v-btn>
            </v-card-actions>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>
  </v-content>
</div>
</div>
</template>

<script>

import axios from 'axios';

export default {
  name: 'LoginForm',
  data: () => ({
    credentials: {},
    valid: true,
  }),
  methods: {
    login() {
      axios.post('/auth/', this.credentials).then((res) => {
        this.$session.start();
        this.$session.set('token', res.data.token);
        this.$router.push('/home');
      }).catch((e) => {
        this.$swal({
          type: 'warning',
          title: 'Error',
          text: 'Wrong username or password',
          showConfirmButton: false,
          showCloseButton: false,
          timer: 3000,
        });
        return e;
      });
    },
  },
};

</script>

<style>
.login {
width: 100%;
height: 100%;
position: absolute;
top: 0;
left: 0;
background: url('~@/assets/media/bg_new.jpg');
background-size: cover;
transform: scale(1.1);
}

</style>
