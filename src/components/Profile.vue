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
					<v-card-text align="left">
						<li v-for="social in socials" :key="social.name">
							{{ social.name }}
						</li>
					</v-card-text>
			</v-col>
			<v-col align="center">
				<h3>My Games</h3>
				<v-card color="#ffffff" outlined>
					<v-card-text align="left">
						<li v-for="game in games" :key="game.name">
							{{ game.name }}
						</li>
					</v-card-text>
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
		user: {},
		games: {},
		socials: {}
    }
  },
  mounted() {
	  const userurl = 'http://35.190.147.190:5000/api/user/10b411b5-3152-4958-a5a0-91f2711f5419';
	  const gamesurl = 'http://35.190.147.190:5000/api/games/'
	  const socialurl = 'http://35.190.147.190:5000/api/socials/'
      const headers = {
        "Access-Control-Allow-Origin": "*"
      };
	axios.get(userurl, { headers })
	  .then(response => {
		  this.user = response.data;
	  })
	  .catch((error) => console.log(error));
	axios.get(gamesurl, { headers })
	  .then(response => {
		  this.games = response.data;
	  })
	  .catch((error) => console.log(error));
	axios.get(socialurl, { headers })
	  .then(response => {
		  this.socials = response.data;
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