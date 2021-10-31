<template>
  <v-app-bar fixed height="auto" bottom color="black" dark>
    <v-bottom-navigation
      app
      v-model="value"
      :background-color="color"
      dark
      shift
      grow
    >
      <v-btn to="/profile">
        <span>Profile</span>

        <v-icon>mdi-account-circle</v-icon>
      </v-btn>

      <v-btn to="/home">
        <span>Find</span>

        <v-icon color="">mdi-crosshairs</v-icon>
      </v-btn>

      <v-btn to="/matches">
        <span>Matches</span>

        <v-icon>mdi-heart-multiple</v-icon>
      </v-btn>
      <v-btn to="/">
        <span>Logout</span>

        <v-icon>mdi-logout</v-icon>
      </v-btn>
    </v-bottom-navigation>
  </v-app-bar>
</template>

<script>
export default {
  data: () => ({ value: 1 }),

  computed: {
    color() {
      switch (this.value) {
        case 0:
          return "gray";
        case 1:
          return "blue";
        case 2:
          return "pink";
        case 3:
          return "red";
        default:
          return "blue-grey";
      }
    },
  },
};
</script>

<style scoped>
.v-btn {
  background-color: white;
}
</style>
