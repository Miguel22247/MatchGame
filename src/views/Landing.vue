<template>
	<v-container
	fluid
	>
		<v-row
			style="background-color: #19202E"
			justify="center"
			align="center"
			back>
			<v-card
      style="background-color: #2B3750"
			elevation="6"
			height="100vh"
			width="80vw"
      align="center"
			>
        <v-card
				flat
				style="background-color: #19202E"
				class="pa-2 ma-4"
				elevation="2">
          <v-card-title class="justify-center"
          style="color: #00A7CC">Welcome</v-card-title>
        </v-card>


        <v-card
        flat
          style="background-color: #19202E"
          class="pa-2 ma-4"
          elevation="2"
          align="center">
            <v-img
              max-height="250"
              max-width="250"
              src="../../public/icons/GameMatch.png"
            ></v-img>
            
        </v-card>
        <v-btn outlined color="#00A7CC" to="/register">Sign Up</v-btn>
        <v-btn outlined color="#00A7CC" to="/login">Sign In</v-btn>
      </v-card>
    </v-row>
  </v-container>
</template>

<script>
import Register from './Register.vue'
import Login from './Login.vue'
import About from './About.vue'

export default {
  components: { Register, Login, About },
  name: 'Home'
}
</script>
<style scoped>
  a {
    text-decoration: none;
  }

  .container {
    height: 100%;
  }

</style>