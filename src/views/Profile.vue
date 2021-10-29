<template>
  <v-container fluid>
    <v-row class="primary" justify="center" align="center" back>
      <v-card class="secondary" elevation="6" height="100vh" width="70vw">
        <v-card class="accent pa-2 ma-4" elevation="2">
          <v-card-title class="primary--text justify-center"
            >{{ user.username }}
          </v-card-title>
          <v-card-text class="secondary--text ">{{ user.bio }}</v-card-text>
        </v-card>

        <v-card class="primary pa-2 ma-4" elevation="2">
          <v-card-title class="accent--text">My games</v-card-title>
          <v-chip-group v-model="user_games" multiple max="6" column>
            <v-chip
              label
              color="secondary accent--text"
              active-class="accent"
              v-for="game in games"
              :key="game.name"
              :value="game.id"
            >
              {{ game.name }}
            </v-chip>
            <p>{{ user_games }}</p>
          </v-chip-group>
          <v-card-actions class="justify-end">
            <v-btn color="accent primary--text" v-on:click="submit_games">
              Update
            </v-btn>
          </v-card-actions>
        </v-card>
        <v-card class="primary pa-2 ma-4" elevation="2">
          <v-card-title class="accent--text">My Social Accounts</v-card-title>
          <v-chip-group v-model="user_games" multiple max="6" column>
            <v-chip
              label
              color="secondary accent--text"
              active-class="accent"
              v-for="social in socials"
              :key="social.name"
            >
              {{ social.name }}
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
      games: {},
      socials: {},
      user_games: {},
      user_socials: {},
    };
  },
  methods: {
    submit_socials: function(event) {
      const user_id = this.user["id"];
      const socialsurl = "http://35.190.147.190:5000/api/socials/";
      const headers = {
        "Access-Control-Allow-Origin": "*",
      };
      axios
        .put(socialsurl.concat("", user_id), this.socials, { headers })
        .then((response) => {
          this.user_socials = response.data;
        })
        .catch((error) => console.log(error));
    },
    submit_games: function(event) {
      const user_id = this.user["id"];
      const gamesurl = "http://35.190.147.190:5000/api/games/";
      const headers = {
        "Access-Control-Allow-Origin": "*",
      };
      axios
        .put(gamesurl.concat("", user_id), this.user_games, { headers })
        .then((response) => {
          this.user_games = response.data;
        })
        .catch((error) => console.log(error));
    },
  },
  mounted() {
    const userurl = "http://35.190.147.190:5000/api/user/";
    const gamesurl = "http://35.190.147.190:5000/api/games/";
    const socialurl = "http://35.190.147.190:5000/api/socials/";
    const user_id = this.$store.getters.getId;
    const headers = {
      "Access-Control-Allow-Origin": "*",
    };
    axios
      .get(userurl.concat("", user_id), { headers })
      .then((response) => {
        this.user = response.data;
        this.user_games = this.user["games"];
      })
      .catch((error) => console.log(error));
    axios
      .get(gamesurl, { headers })
      .then((response) => {
        this.games = response.data;
      })
      .catch((error) => console.log(error));
    axios
      .get(socialurl, { headers })
      .then((response) => {
        this.socials = response.data;
      })
      .catch((error) => console.log(error));
  },
};
</script>

<style scoped>
.v-chip--active >>> .v-chip__content {
  color: black;
}
</style>
