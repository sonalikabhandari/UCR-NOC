import Vue from 'vue';
import VueRouter from 'vue-router';
// import About from '../views/About.vue';
import AletheiaProcess from '../views/arProcess.vue';
import DailyPrepProcess from '../views/dpProcess.vue';
import DailyUpdateProcess from '../views/duProcess.vue';
import Homepage from '../views/homepage.vue';
import Overview from '../views/overview.vue';
import Login from '../views/loginPage.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'login',
    component: Login,
  },
  {
    path: '/home',
    name: 'homepage',
    component: Homepage,

  },
  {
    path: '/Overview',
    name: 'Overview',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: Overview,

  },

  {
    path: '/arProcess',
    name: 'aletheiaProcess',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: AletheiaProcess,

  },
  {
    path: '/dpProcess',
    name: 'dailyPrepProcess',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: DailyPrepProcess,

  },
  {
    path: '/duProcess',
    name: 'dailyUpdateProcess',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: DailyUpdateProcess,

  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

/*  router.beforEach((to, from, next) => {
  const reqSession = to.matched.some((route) => (route.meta.requiresSession));
  if (!reqSession) next();

  if (router.app.$session.exists()) {
    next();
  } else {
    next('/');
  }
}); */

export default router;
