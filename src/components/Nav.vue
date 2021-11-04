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
      <v-btn to="/profile" v-if="isDisabled">
        <span>Profile</span>

        <v-icon>mdi-account-circle</v-icon>
      </v-btn>

      <v-btn to="/home" v-if='isDisabled'>
        <span>Find</span>

        <v-icon color="">mdi-magnify</v-icon>
      </v-btn>

      <v-btn to="/matches" v-if='isDisabled'>
        <span>Matches</span>

        <v-icon>mdi-heart-multiple</v-icon>
      </v-btn>

      <v-btn to="/" v-if='!isDisabled'>
        <span>Authenticate</span>

        <v-icon>mdi-home-account</v-icon>
      </v-btn>
      
    </v-bottom-navigation>
  </v-app-bar>
</template>

<script>
export default {
  data: () => ({ value: 1 }),

  computed: {

    isDisabled: function(){
      if (!this.$store.getters.getId) {
        return false
      } else {
        return true
      }
    },

    color() {
      switch (this.value) {
        case 0:
          return "#007ACC";
        case 1:
          return "#ff5e00";
        case 2:
          return "#A300FF";
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
