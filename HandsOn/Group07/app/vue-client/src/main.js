import Vue from "vue";
import VueI18n from "vue-i18n";

Vue.use(VueI18n);

// Cargando vue-notification
import Notifications from "vue-notification";
Vue.use(Notifications);

import App from "./App.vue";
import router from "./router";
import vuetify from "./plugins/vuetify";

import BootstrapVue from "bootstrap-vue";
Vue.use(BootstrapVue);

import "bootstrap/dist/css/bootstrap.css";
import "bootstrap-vue/dist/bootstrap-vue.css";
import "./App.scss";

Vue.config.productionTip = false;

new Vue({
  router,
  vuetify,
  render: h => h(App)
}).$mount("#app");
