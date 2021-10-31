<template>
  <v-container fill-height pa-12>
    <v-row fluid dense align="center" justify="center" grow>
      <v-col>
        <v-flex text-center pb-8>
          <h1>POSSIBLE MATCHES</h1>
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
      user: {},
      matches: [],
    };
  },
  mounted() {
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
