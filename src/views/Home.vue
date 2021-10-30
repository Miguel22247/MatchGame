<template>
	<v-container fill-height fluid mt-14>
    	<v-row>
			<h2>Hello {{ user.username }}!</h2>
		</v-row>
		<v-row align="center" justify="center">
			<h4>Possible Matches</h4>
		</v-row>
		<v-row justify="space-around">
			<v-col>
				<v-card v-for="usr in other_users" :key="usr.username" class="mx-auto my-12" max-width="374">
					<v-card-title> {{ usr.username }} </v-card-title>
					<v-card-text>
						<v-row align="center" class="mx-0">
							<div class="my-4 text-subtitle-1">
								{{ usr.bio }}
							</div>
						</v-row>
					</v-card-text>
					<v-divider class="mx-4"></v-divider>
					<v-card-title>Games</v-card-title>
					<div v-for="game in usr.games" :key="game.name">
						{{game.name}}
					</div>
					<v-btn v-on:click="submit_like(usr.id)">
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
		other_users: [],
		responsestatus: 0
    }
  },
  methods: {
	  submit_like: function (usr_id) {
		  const body = {user_id: this.user["id"], like_id: usr_id}
		  const likeurl = 'http://35.190.147.190:5000/api/add_like/'
		  const headers = {
			"Access-Control-Allow-Origin": "*"
		};
		axios.post(likeurl, body, { headers })
		.then(response => {
			this.responsestatus = response.status
			if (responsestatus === 201) {
				alert("It's a match, check your matches to see their contact info and start to play")
			}
		})
	  }
  },
  mounted() {
	  const userurl = 'http://35.190.147.190:5000/api/user/';
	  const get_users_url = 'http://35.190.147.190:5000/api/get_users/'
	  // api/get_users/<userid>  (retrieves all users that match the games of the userid)
	  // for item in response.data 
	  // show item.username 
	  const user_id = this.$store.getters.getId;
      const headers = {
        "Access-Control-Allow-Origin": "*"
      };
	  axios.get(userurl.concat('', user_id), { headers })
	  .then(response => {
		  this.user = response.data;
	  })
	  .catch((error) => console.log(error));
	  axios.get(get_users_url.concat('', user_id), { headers })
	  .then(response => {
		  this.other_users = response.data;
	  })
	  .catch((error) => console.log(error));
  }
  
};
</script>