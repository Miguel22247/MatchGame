<template
style="overflow: hidden;">
	<v-container
  style="overflow-y: hidden;"
  app
	fluid
	>
		<v-row
    style="overflow: hidden;"
			justify="center"
			align="center"
			back>
			<v-card
      color="primary"
			elevation="6"
			height="100vh"
			width="80vw"
      align="center"
			>
        <v-card
				flat
        color="secondary"
				class="pa-2 ma-4"
				elevation="2"
        outlined>
          <v-card-title class="justify-center"
          >Welcome</v-card-title>
        </v-card>

        <v-card
        flat
        class="pa-2 ma-4"
        color="secondary"
        elevation="2"
        align="center">
          <v-img
            max-height="250"
            max-width="250"
            src="../../public/icons/GameMatch.png"
          ></v-img>
            
        </v-card>
        <v-btn outlined color="accent" to="/register">Sign Up</v-btn>
        <v-btn outlined color="accent" to="/login">Sign In</v-btn>
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
  .scrollbar-hidden::-webkit-scrollbar {
    display: none;
  }
  a {
    text-decoration: none;
  }

  .container {
    height: 100%;
  }
</style>