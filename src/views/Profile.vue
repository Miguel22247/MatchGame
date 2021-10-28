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
						<v-checkbox v-for="social in socials" :key="social.name" v-model="user_socials" :value="social.id">
							<template v-slot:label>
								<p justify="center">{{ social.name }}</p>
							</template>
						</v-checkbox>
						<v-btn v-on:click="submit_socials">Update</v-btn>
					</v-card-text>
			</v-col>
			<v-col align="center">
				<h3>My Games</h3>
				<v-card color="#ffffff" outlined>
					<v-card-text align="left">
						<v-checkbox v-for="game in games" :key="game.name" v-model="user_games" :value="game.id">
							<template v-slot:label>
								<p justify="center">{{ game.name }}</p>
							</template>
						</v-checkbox>
						<v-btn v-on:click="submit_games">
							Update
						</v-btn>
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
		socials: {},
		user_games: [],
		user_socials:[],
		games_response: []
    }
  },
  methods: {
	submit_socials: function (event) {
		const user_id = user.id
		const socialsurl = 'http://35.190.147.190:5000/api/socials/'
		const headers = {
    		"Access-Control-Allow-Origin": "*"
    	};
		axios.put()
	},
	submit_games: function (event) {
		const user_id = user.id
		const gamesurl = 'http://35.190.147.190:5000/api/games/'
		const headers = {
			"Access-Control-Allow-Origin": "*"
		};
		axios.put(gamesurl.concat('', user_id), { headers })
		.then(response => {
			this.games_response = response;
		})
		.catch((error) => console.log(error));
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
		  this.user_games = this.user.games]
	  })
	  .catch((error) => console.log(error));
	axios.get(gamesurl, { headers })
	  .then(response => {
		  this.games = response.data
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