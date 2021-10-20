import Vue from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
import vuetify from './plugins/vuetify';
//import { initializeApp } from 'https://www.gstatic.com/firebasejs/9.1.3/firebase-app.js"';
// import firebase from 'firebase/compat/app';
// import { getAuth } from 'https://www.gstatic.com/firebasejs/9.1.3/firebase-auth.js"';

// onAuthStateChanged(auth, user => {
//   if(user != null) {
//     console.log('logged');
//   }
//   else {
//     console.log('not logged');
//   }
// });


//import firebase from 'firebase/compat/app';
import 'firebase/compat/auth';
//import { getDoc } from 'firebase/firestore'
import { onAuthStateChanged, getAuth } from "firebase/auth"
import { initializeApp } from "firebase/app"

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
};

const firebaseApp = initializeApp(firebaseConfig);

const auth = getAuth(firebaseApp);
onAuthStateChanged(auth, user => {
  store.dispatch("fetchUser", user);
});

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')

