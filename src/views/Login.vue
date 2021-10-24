<template>
  <v-container fill-height fluid mt-14>
	<v-row align="center" justify="center">
		<login/>
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