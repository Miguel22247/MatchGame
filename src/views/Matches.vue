<template>
  <v-container fill-height pa-12>
    <v-row fluid dense align="center" justify="center" grow>
      <v-col>
        <v-flex text-center pb-8>
          <h1>MATCHES</h1>
        </v-flex>
        <v-scale-transition mode="in" hide-on-leave="true">
          <v-card
            max-width="420"
            v-show="true"
            v-for="match in matches"
            :key="match.username"
            class="mx-auto my-12"
          >
            <v-card-title class="justify-center" style="color: #b83aff">
              <h2>{{ match.username }}</h2>
            </v-card-title>
            <v-divider class="mx-2"></v-divider>
            <v-card-text>
              <v-row align="center" class="mx-0">
                <div class="my-2 text-subtitle-1">
                  {{ match.bio }}
                </div>
              </v-row>
            </v-card-text>
            <v-card-text>
              <div
                class="text-subtitle-1"
                v-for="match_social in match.socials"
                :key="match_social.name"
              >
                <div class="d-inline-flex">{{ match_social.name }}: &nbsp;</div>
                <div class="d-inline-flex" style="color: rgb(163, 0, 255)">
                  {{ match_social.link }}
                </div>
              </div>
            </v-card-text>
            <v-divider class="mx-4"></v-divider>

            <v-card-title class="justify-center">Games</v-card-title>
            <v-chip-group class="nowrap" justify-center column>
              <v-flex text-center pb-4>
              <v-chip
                dense
                label
                color="#b83aff"
                v-for="game in match.games"
                :key="game.name"
              >
                {{ game.name }}
              </v-chip>
              </v-flex>
            </v-chip-group>
          </v-card>
        </v-scale-transition>
      </v-col>
    </v-row>
  </v-container>
</template>
<script>
import axios from "axios";
export default {
  data: function () {
    return {
      user: {},
      matches: [],
    };
  },
  async mounted() {
    const userurl = "http://35.190.147.190:5000/api/user/";
    const matchurl = "http://35.190.147.190:5000/api/get_matches/";
    const userid = this.$store.getters.getId;
    const headers = {
      "Access-Control-Allow-Origin": "*",
    };
    axios
      .get(userurl.concat("", userid), { headers })
      .then((response) => {
        this.user = response.data;
      })
      .catch((error) => console.log(error));
    axios
      .get(matchurl.concat("", userid), { headers })
      .then((response) => {
        this.matches = response.data;
      })
      .catch((error) => console.log(error));
  },
};
</script>
