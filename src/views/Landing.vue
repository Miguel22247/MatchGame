<template>
  <v-container fill-height pa-16>
    <v-row align="center" justify="center" grow>
      <h1 style="text-align: -webkit-center">Welcome to MatchGame</h1>
    </v-row>
    <v-row align="center" justify="center" grow>
      <v-img
        max-height="250"
        max-width="250"
        src="../../src/assets/GameMatch.png"
      ></v-img>
    </v-row>

    <v-row align="center" justify="center" grow>
      <v-col align="center" justify="center">
        <v-flex text-center pb-2>
          <v-btn outlined to="/register">Create an account</v-btn>
        </v-flex>
        <a href="#/login">Already have an account?</a>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  components: {},
  name: "Home",
};
</script>
<style scoped>
a {
  text-decoration: none;
}
.container {
  height: 100%;
}
</style>
