<template>
	<v-container fill-height fluid mt-14>
    	<v-row>
			<v-form ref="user" @submit.prevent="submit_bio">
				<v-text-field label="Username" v-model="user.username">
				</v-text-field>
				<v-textarea label="Bio" v-model="user.bio">
				</v-textarea>
			</v-form>
			<p>{{ user }}</p>
			<v-btn v-on:click="submit_bio">
				Submit
			</v-btn>
		</v-row>
		<v-row>
			<v-col align="center">
				<h3>Social Accounts</h3>
					<v-card-text align="left">
						<v-form ref="user_socials" @submit.prevent="submit_socials">
							<v-container v-for="social in socials" :key="social.name" :value="social.link" v-model="user_socials">
								<v-text-field rounded outlined color="#00A7CC" :label="social.name" v-model="social.link">
								</v-text-field>
							</v-container>
						</v-form>
						<p>{{ socials }}</p>
						<v-btn rounded outlined color="#00A7CC" v-on:click="submit_socials">
							Update
						</v-btn>
					</v-card-text>
			</v-col>
			<v-col align="center">
				<h3>My Games</h3>
					<v-card-text align="left">
						<v-checkbox color="#00A7CC" v-for="game in games" :key="game.name" v-model="user_games" :value="game.id">
							<template v-slot:label>
								<p>{{ game.name }}</p>
							</template>
						</v-checkbox>
						<p>{{ user_games }}</p>
						<v-btn rounded outlined color="#00A7CC" v-on:click="submit_games">
							Update
						</v-btn>
					</v-card-text>
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
		user_socials: []
    }
  },
  methods: {
	submit_socials: function () {
		const user_id = this.user["id"]
		const socialsurl = 'http://35.190.147.190:5000/api/socials/'
		const headers = {
    		"Access-Control-Allow-Origin": "*"
    	};
		axios.put(socialsurl.concat('', user_id), this.socials, { headers })
		.then(response => {
			this.user_socials = response.data;
		})
		.catch((error) => console.log(error));
	},
	submit_games: function () {
		const user_id = this.user["id"]
		const gamesurl = 'http://35.190.147.190:5000/api/games/'
		const headers = {
			"Access-Control-Allow-Origin": "*"
		};
		axios.put(gamesurl.concat('', user_id), this.user_games, { headers })
		.then(response => {
			this.user_games = response.data;
		})
		.catch((error) => console.log(error));
	},
	submit_bio: function () {
		const user_id = this.user["id"]
		const biourl = 'http://35.190.147.190:5000/api/bio/'
		const headers = {
			"Access-Control-Allow-Origin": "*"
		};
		axios.put(biourl.concat('', user_id), this.user, { headers })
		.then(response => {
			this.user = response.data;
		})
		.catch((error) => console.log(error));
	}
  },
  mounted() {
	  const userurl = 'http://35.190.147.190:5000/api/user/';
	  const gamesurl = 'http://35.190.147.190:5000/api/games/';
	  const socialurl = 'http://35.190.147.190:5000/api/socials/';
	  const user_id = this.$store.getters.getId;
      const headers = {
        "Access-Control-Allow-Origin": "*"
      };
	axios.get(userurl.concat('', user_id), { headers })
	  .then(response => {
		  this.user = response.data;
		  this.user_games = this.user["games"]
	  })
	  .catch((error) => console.log(error));
	axios.get(gamesurl, { headers })
	  .then(response => {
		  this.games = response.data
	  })
	  .catch((error) => console.log(error));
	axios.get(socialurl.concat('', user_id), { headers })
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