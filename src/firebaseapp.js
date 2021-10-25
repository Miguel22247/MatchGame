import 'firebase/compat/auth';
import { initializeApp } from "firebase/app"


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
export default firebaseApp


