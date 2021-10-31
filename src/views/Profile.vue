<template>
  <v-container fill-height pa-12>
    <v-row fluid dense align="center" justify="center" grow>
      <v-col>
        <v-flex text-left pb-8>
          <h1>PROFILE</h1>
        </v-flex>
        <form ref="user" @submit.prevent="submit_bio">
          <v-text-field
            label="Username"
            v-model="user.username"
            outlined
            clearable
            append-icon="mdi-account"
          >
          </v-text-field>
          <v-text-field
            label="Bio"
            v-model="user.bio"
            outlined
            clearable
            append-icon="mdi-text-account"
          >
          </v-text-field>
          <v-flex text-right>
            <v-btn outlined type="submit_bio">Save</v-btn>
          </v-flex>
        </form>
      </v-col>
    </v-row>
    <v-row fluid>
      <v-divider dark></v-divider>
    </v-row>
    <v-row dense align="center" justify="center" grow>
      <v-col>
        <v-flex text-left pb-8>
          <h1>SOCIALS</h1>
        </v-flex>
        <form ref="user_socials" @submit.prevent="submit_socials">
          <v-flex
            v-for="social in socials"
            :key="social.name"
            :value="social.link"
            v-model="user_socials"
          >
            <v-text-field
              outlined
              :label="social.name"
              v-model="social.link"
              :append-icon="'mdi-' + social.name"
            >
            </v-text-field>
          </v-flex>

          <v-flex text-right>
            <v-btn outlined type="submit_socials">Save</v-btn>
          </v-flex>
        </form>
      </v-col>
    </v-row>

    <v-row>
      <v-divider dark></v-divider>
    </v-row>
    <v-row dense align="center" justify="center" grow>
      <v-col>
        <v-flex text-left pb-8>
          <h1>GAMES</h1>
        </v-flex>
        <v-flex>
          <v-chip-group
            active-class="primary--text"
            v-model="user_games"
            multiple
            column
          >
            <v-chip
              dark
              label
              v-for="game in games"
              :key="game.name"
              :value="game.id"
            >
              {{ game.name }}
            </v-chip>
          </v-chip-group>
        </v-flex>
        <v-flex text-right>
          <v-btn outlined type="submit_games">Save</v-btn>
        </v-flex>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from "axios";
export default {
  data: function () {
    return {
      user: [],
      games: {},
      socials: {},
      user_games: [],
      user_socials: [],
    };
  },
  methods: {
    submit_socials: function () {
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
    submit_games: function () {
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
    submit_bio: function () {
      const user_id = this.user["id"];
      const biourl = "http://35.190.147.190:5000/api/bio/";
      const headers = {
        "Access-Control-Allow-Origin": "*",
      };
      axios
        .put(biourl.concat("", user_id), this.user, { headers })
        .then((response) => {
          this.user = response.data;
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
      .get(socialurl.concat("", user_id), { headers })
      .then((response) => {
        this.socials = response.data;
      })
      .catch((error) => console.log(error));
  },
};
</script>
<style scoped>
a {
  text-decoration: none;
}
</style>
*/
