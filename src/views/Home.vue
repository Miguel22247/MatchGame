<template>
	<v-container fill-height fluid mt-14>
    	<v-row justify="left">
			<h2>Hello Miguel!</h2>
		</v-row>
		<v-row align="center" justify="center">
			<h4>Possible Matches</h4>
		</v-row>
		<v-row justify="space-around">
			<v-col>
				<v-card class="mx-auto my-12" max-width="374">
					<v-card-title> {{ user.username }} </v-card-title>
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