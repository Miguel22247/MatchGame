<template>
	<v-container
	fluid
	>
		<v-row
			style="background-color: #EDE7F6"
			justify="center"
			align="center"
			back>
			<v-card
			height="100vh"
			width="80vw"
			>
				hello
				asd
				asd
				asd
				asd

			</v-card>
		</v-row>
	</v-container>
</template>

<script>
import axios from "axios";

export default {
  data: function() {
    return {
      user: {},
      games: [],
    };
  },
  mounted() {
    const userurl =
      "http://35.190.147.190:5000/api/user/10b411b5-3152-4958-a5a0-91f2711f5419";
    const gamesurl = "http://35.190.147.190:5000/api/games";
    const headers = {
      "Access-Control-Allow-Origin": "*",
    };
    axios
      .get(gamesurl, { headers })
      .then((response) => {
        this.games = response.data;
      })
      .catch((error) => console.log(error));
  },
};
</script>
<style scoped>
</style>
