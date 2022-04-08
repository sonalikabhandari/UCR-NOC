<template>
  <div class ="appBar">

    <v-app-bar
        dark
        color="#37474F" clipped-left app>
        <v-app-bar-nav-icon @click="drawer = !drawer">
        </v-app-bar-nav-icon>

        <v-toolbar-title>UCR NOC</v-toolbar-title>

        <v-spacer></v-spacer>

        <v-btn flat color="#37474F" @click="logout">
        <span>Logout</span>
        <v-icon>exit_to_app</v-icon>
      </v-btn>

    </v-app-bar>
    <v-navigation-drawer clipped app
     v-model="drawer" class="blue-grey lighten-4" :width="325" >
        <v-list v-for="link in links" :key="link.text">
         <v-list-item :href="link.path" >
          <v-list-item-action>
            <v-icon>{{link.icon}}</v-icon>
          </v-list-item-action>
          <v-list-item-content>
           <v-list-item-title class="black--text">{{link.text}}</v-list-item-title>
          </v-list-item-content>
         </v-list-item>
        </v-list>
    </v-navigation-drawer>

    </div>
</template>

<script>
export default {
  data() {
    return {
      drawer: false,
      links: [
        { icon: 'home', text: 'Home', path: '/home' },
        { icon: 'view_compact', text: 'Overview', path: '/Overview' },
        { icon: 'dashboard', text: 'Aletheia/Rancid Process', path: '/arProcess' },
        { icon: 'dashboard', text: 'Daily Preparation Process', path: '/dpProcess' },
        { icon: 'dashboard', text: 'Daily Update Process', path: '/duProcess' },

      ],
    };
  },
  methods: {
    logout() {
      this.$session.destroy();
      this.$router.push('/');
    },
  },
};
</script>
