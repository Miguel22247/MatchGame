<template>
	<v-container
	fluid
	>
		<v-row
			style="background-color: #19202E"
			justify="center"
			align="center"
			back>
			<v-card
			style="background-color: #2B3750"
			elevation="6"
			height="100vh"
			width="80vw"
			>
				<v-card
				
				style="background-color: #19202E"
				class="pa-2 ma-4"
				elevation="2"
				>
					<v-card-title style="color: #00A7CC">My games</v-card-title>
					<v-chip-group
					v-model="selection"
					multiple
					max="6"
					column
				 
          >
            <v-chip
						color="#2B3750"
						v-for="game in games"
						:key="game.name"
						:value="game.id"
            >
              {{ game.name }}
            </v-chip>
          </v-chip-group>
				</v-card>
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
			selection: [],
    };
  },
  mounted() {
    const userurl = "http://35.190.147.190:5000/api/user/{{ user.id }}";
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
		axios
			.get(userurl, { headers })
      .then((response) => {
        this.user = response.data;
      })
      .catch((error) => console.log(error));
  },
};
</script>
<style scoped>
	.v-chip-group {
		color: #00A7CC;
	}
</style>
