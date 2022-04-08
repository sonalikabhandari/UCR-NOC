import Vue from 'vue';
import BootstrapVue from 'bootstrap-vue';
import VueSession from 'vue-session';
import Vuetify from 'vuetify';
import App from './App.vue';
import vuetify from './plugins/vuetify';
import VueSweetalert2 from 'vue-sweetalert2';
import router from './router';

import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';
import 'sweetalert2/dist/sweetalert2.min.css';

import Default from './layouts/default.vue';


Vue.component('defaultlayout', Default);

Vue.use(Vuetify);
Vue.use(VueSession);
Vue.use(VueSweetalert2);
// require('./assets/css/style.css');

Vue.config.productionTip = false;
Vue.use(BootstrapVue);

new Vue({
  router,
  vuetify,
  render: (h) => h(App),
}).$mount('#app');
