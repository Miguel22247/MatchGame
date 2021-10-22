import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify'
import { initializeApp } from 'firebase/app';
import VeeValidate from 'vee-validate'

Vue.use(VeeValidate)
Vue.config.productionTip = false

const firebaseConfig = {
    apiKey: "AIzaSyAB3l40bmXJPb8ApayZkRrc9jQd4RjSMFY",
    authDomain: "hbtn-final-project-mvd.firebaseapp.com",
    databaseURL: "https://hbtn-final-project-mvd-default-rtdb.firebaseio.com",
    projectId: "hbtn-final-project-mvd",
    storageBucket: "hbtn-final-project-mvd.appspot.com",
    messagingSenderId: "473058971936",
    appId: "1:473058971936:web:a374203cc6dbef52a20745",
    measurementId: "G-GQNWF2Y937"
}

initializeApp(firebaseConfig);

new Vue({
  router,
  store,
  vuetify,
  // el: "#app",
  // components: {App},
  render: h => h(App),
  mounted () {
    initializeApp(firebaseConfig);
  }
}).$mount('#app')
