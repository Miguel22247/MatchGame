<template>
  <v-app>
    <v-main>
      <router-view />
      
    </v-main>
    <Nav app></Nav>
  </v-app>
</template>

<script>
import Nav from "./components/Nav.vue";

export default {
  name: "App",
  components: { Nav },

  data: () => ({
    //
  }),
};
</script>

<style scoped>

</style>