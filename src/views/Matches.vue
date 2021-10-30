<template>
	<v-container fill-height fluid mt-14>
		<v-row align="center" justify="center">
			<h4>Last Matches</h4>
		</v-row>
		<v-row justify="space-around">
			<v-col>
				<v-card v-for="match in matches" :key="match.username" class="mx-auto my-12" max-width="374">
					<v-card-title> {{ match.username }} </v-card-title>
					<v-card-text>
						<v-row align="center" class="mx-0">
							<div class="my-4 text-subtitle-1">
								{{ match.bio }}
							</div>
						</v-row>
					</v-card-text>
					<v-divider class="mx-4"></v-divider>
					<v-card-title>Social Accounts</v-card-title>
					<v-card-text>
						<div v-for="social in match.social" :key="social.name">
							{{ social.name }}: {{ social.link }}
						</div>
					</v-card-text>
					<v-card-title>Games</v-card-title>
					<v-card-text>
						<div v-for="game in match.games" :key="game.name">
							{{ game.name }}
						</div>
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
		matches: []
    }
  },
  mounted() {
	  const apiurl = 'http://35.190.147.190:5000/api/user/';
	  const userid = this.$store.getters.getId;
	  const headers = {
        "Access-Control-Allow-Origin": "*"
      };
	  axios.get(apiurl.concat('', userid), { headers })
	  .then(response => {
		  this.user = response.data;
	  })
	  .catch((error) => console.log(error));
  }
};
</script>