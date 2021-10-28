<template>
	<v-container
	fluid
	>
		<v-row
			class="primary"
			justify="center"
			align="center"
			back>
			<v-card
			class="secondary"
			elevation="6"
			height="100vh"
			width="80vw"
			>
				<v-card
				class="primary pa-2 ma-4"
				elevation="2"
				>
					<v-card-title class="accent--text">My games</v-card-title>
					<v-chip-group
					v-model="selection"
					multiple
					max="6"
					column
				 
          >
            <v-chip
						style="color: white"
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
