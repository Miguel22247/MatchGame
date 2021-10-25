import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify'
import { initializeApp } from 'firebase/app';
import VeeValidate from 'vee-validate'

Vue.use(VeeValidate)
Vue.config.productionTip = false

new Vue({
  router,
  store,
  vuetify,
  // el: "#app",
  // components: {App},
  render: h => h(App),
}).$mount('#app')
