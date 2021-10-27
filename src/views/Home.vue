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
				<v-card class="mx-auto my-12" max-width="374">
					<v-card-title> {{ user.username }} </v-card-title>
					<v-card-text>
						<v-row align="center" class="mx-0">
							<div class="my-4 text-subtitle-1">
								{{ user.bio }}
							</div>
						</v-row>
					</v-card-text>
					<v-divider class="mx-4"></v-divider>
					<v-card-title>Social Media</v-card-title>
					<v-card-text>
						
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
		user: {}
    }
  },
  mounted() {
	  const apiurl = 'http://35.190.147.190:5000/api/get_users/';
	  // api/get_users/<userid>  (retrieves all users that match the games of the userid)
	  // for item in response.data 
	  // show item.username 
	  const user_id = this.$store.getters.getId;
      const headers = {
        "Access-Control-Allow-Origin": "*"
      };
	  axios.get(apiurl.concat('', user_id), { headers })
	  .then(response => {
		  this.user = response.data;
	  })
	  .catch((error) => console.log(error));
  }
  
};
</script>