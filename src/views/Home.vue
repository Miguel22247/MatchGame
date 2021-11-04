<template>
  <v-container fluid dense fill-height pa-6>
    <v-row fluid dense align="center" justify="center">
      <v-col>
        <v-flex text-center pb-n16>
          <h1>Possible Matches</h1>
        </v-flex>
      </v-col>
    </v-row>
    <v-row fluid dense align="center" justify="center" class="pb-4">
      <v-col style="text-align: -webkit-center">
        <v-scale-transition mode="in" hide-on-leave="true" v-for="usr in other_users" :key="usr.username">
          <v-flex pb-4>
            <v-card
              v-show="true"
              max-width="420"
            >
              <v-card-title> {{ usr.username }} </v-card-title>
              <v-card-text> {{ usr.bio }} </v-card-text>
              <v-divider class="mx-4"></v-divider>
              <v-card-title>Games</v-card-title>
              <v-chip-group class="nowrap" justify-center column>
                <v-chip color="#ff5e00" v-for="game in usr.games" :key="game.name">
                  {{ game.name }}
                </v-chip>
              </v-chip-group>
              <v-flex text-right>
                <v-btn v-on:click="submit_like(usr.id)">Like</v-btn>
              </v-flex>
            </v-card>
          </v-flex>
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
      other_users: [],
      responsestatus: 0,
    };
  },
  methods: {
    submit_like: function (usr_id) {
      const body = { user: this.user["id"], like: usr_id };
      const likeurl = "http://35.190.147.190:5000/api/add_like/";
      const headers = {
        "Access-Control-Allow-Origin": "*",
      };
      axios.post(likeurl, body, { headers }).then((response) => {
        this.responsestatus = response.status;
        if (response.status === 201) {
          alert(
            "It's a match, check your matches to see their contact info and start to play"
          );
        }
      });
    },
  },
  mounted() {
    const userurl = "http://35.190.147.190:5000/api/user/";
    const get_users_url = "http://35.190.147.190:5000/api/get_users/";
    // api/get_users/<userid>  (retrieves all users that match the games of the userid)
    // for item in response.data
    // show item.username
    const user_id = this.$store.getters.getId;
    const headers = {
      "Access-Control-Allow-Origin": "*",
    };
    axios
      .get(userurl.concat("", user_id), { headers })
      .then((response) => {
        this.user = response.data;
      })
      .catch((error) => console.log(error));
    axios
      .get(get_users_url.concat("", user_id), { headers })
      .then((response) => {
        this.other_users = response.data;
      })
      .catch((error) => console.log(error));
  },
};
</script>
