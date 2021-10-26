<template>
	<v-container fill-height fluid mt-14>
    	<v-row align="top" justify="center">
			<h3>{{ user.username }}</h3>
		</v-row>
		<v-row align="center" justify="center">
			<h4>Bio</h4>
			<p>{{ user.bio }}</p>
		</v-row>
		<v-row>
			<v-col align="center">
				<h3>Social Accounts</h3>
				<v-chip-group
				align="center"
				v-model="selection"
				column
				>
					<a target="_blank" href="https://steamcommunity.com/id/Miguel22247/"><v-chip active-class="blue darken-4 white--text"><v-icon>mdi-steam</v-icon> Steam</v-chip></a>

					<v-chip active-class="orange accent-4 white--text"><v-icon>mdi-origin</v-icon> Origin</v-chip>

					<v-chip active-class="blue-grey accent-4 white--text"><v-icon>mdi-ubisoft</v-icon> Ubisoft</v-chip>
			
					<v-chip active-class="blue accent-4 white--text"><v-icon>mdi-discord</v-icon> Discord</v-chip>
			
					<v-chip active-class="light-blue accent-4 white--text"><v-icon>mdi-twitter</v-icon> Twitter</v-chip>

				</v-chip-group>
			</v-col>
			<v-col align="center">
				<h3>My Games</h3>
				<v-card color="#ffffff" outlined>
					<v-chip-group
					align="right"
					v-model="selection"
					column
					>
					<v-chip active-class="red darken-2 accent-4 white--text"><v-icon>mdi-truck</v-icon>Euro Truck Simulator</v-chip>

					<v-chip active-class="green accent-4 white--text"><v-icon>mdi-tractor</v-icon> Farming Simulator</v-chip>

					<v-chip active-class="blue-grey accent-4 white--text"><v-icon>mdi-airplane</v-icon> FSX</v-chip>
			
					<v-chip active-class="blue accent-4 white--text"><v-icon>mdi-target</v-icon> CS:GO</v-chip>
			
					<v-chip active-class="light-blue accent-4 white--text"><v-icon>mdi-car</v-icon> Asseto Corsa</v-chip>
					</v-chip-group>
				</v-card>
			</v-col>
		</v-row>
	</v-container>
</template>
<script>
import axios from 'axios'


export default {
  data: function() {
    return {
		user: {}
    }
  },
  mounted() {
	  const apiurl = 'http://35.190.147.190:5000/api/user/10b411b5-3152-4958-a5a0-91f2711f5419';
      const headers = {
        "Access-Control-Allow-Origin": "*"
      };
	  axios.get(apiurl, { headers })
	  .then(response => {
		  this.user = response.data;
	  })
	  .catch((error) => console.log(error));
  }
};
</script>
<style scoped>
a {
	text-decoration: none;
}
</style>