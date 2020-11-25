import Vue from "vue";
import Router from "vue-router";
import { NotFound } from "./components";

Vue.use(Router);

const routes = [
  {
    path: "/",
    name: "Home",
    component: () => import("./components/Home.vue"),
    meta: { public: true }
  },
  {
    path: "/about",
    name: "About",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "./components/About.vue"),
    meta: { public: true }
  },
  {
    path: "/organizations",
    name: "Organization",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "./components/Organization.vue"),
    meta: { public: true }
  },
  {
    path: "/researchers",
    name: "Researcher",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "./components/Researcher.vue"),
    meta: { public: true }
  },
  { path: "*", component: NotFound, meta: { public: true } }
];

// A las rutas definidas en este fichero les añadimos rutas importadas
const router = new Router({
  routes: routes.concat()
});

export default router;
