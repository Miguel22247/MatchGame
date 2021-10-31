<template>
  <v-container class="container" fluid fill-height>
    <v-row align="center" justify="center">
      <h2>Welcome to GameMatch</h2>
    </v-row>
    <v-row align="center" justify="center"> </v-row>
    <v-row align="center" justify="space-around">
      <v-btn outlined color="#00A7CC" to="/register">Sign Up</v-btn>
      <v-btn outlined color="#00A7CC" to="/login">Sign In</v-btn>
    </v-row>
  </v-container>
</template>

<script>

export default {
  components: {   },
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
