<template>
  <v-container class="container" fluid fill-height>
	<v-row align="center" justify="center">
		<login/>
	</v-row>
  </v-container>
</template>

<script>
import Login from '../components/Login.vue'

export default {
  components: {Login },
  name: 'Home'
}
</script>
<style scoped>
.container {
  height: 100%;
}
</style>