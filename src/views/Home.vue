<template>
  <v-container fill-height fluid mt-14>
    <v-row align="center" justify="center">
  		<h2>Welcome to GameMatch</h2>
	</v-row>
    <v-row align="center" justify="space-around">
		<router-link to="/register"><v-btn outlined color="#00A7CC">Sign Up</v-btn></router-link>
		<router-link to="/login"><v-btn outlined color="#00A7CC">Sign In</v-btn></router-link>
	</v-row>
  </v-container>
</template>

<script>
import Register from '../components/Register.vue'
import Login from '../components/Login.vue'

export default {
  components: { Register, Login },
  name: 'Home'
}
</script>