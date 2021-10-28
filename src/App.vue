<template>
  <v-app
  id="app"
  style="overflow-y: hidden;">
    <v-app-bar
      app
      color="#00A7CC"
      dark
    >
      <v-app-bar-nav-icon @click.stop="drawer = !drawer">
        <v-icon color="black">mdi-menu</v-icon>
      </v-app-bar-nav-icon>
      <v-spacer></v-spacer>
      <v-toolbar-title class="pr-10" style="color: black">
        {{ $route.name }}
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <!-- <v-btn icon>
        <v-icon>mdi-magnify</v-icon>
      </v-btn>

      <v-btn icon>
        <v-icon>mdi-filter</v-icon>
      </v-btn>

      <v-btn icon>
        <v-icon>mdi-dots-vertical</v-icon>
      </v-btn> -->
    </v-app-bar>

    <v-navigation-drawer
      v-model="drawer"
      absolute
      bottom
      temporary
      color="#00A7CC"
    >
      <v-list
        nav
        dense
      >
        <v-list-item-group
          v-model="group"
          active-class="deep-blue--text text--accent-4"
        >
          <v-list-item
          v-for="item in items"
          :key="item.title"
          :to="item.to"
          link
          >
            <v-list-item-icon>
              <v-icon>{{ item.icon }}</v-icon>
            </v-list-item-icon>

            <v-list-item-content>
              <v-list-item-title>{{ item.title }}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>

    <v-main>
      <!-- If using vue-router -->
      <router-view></router-view>
    </v-main>
  </v-app>
</template>

<script>
  export default {
    data: () => ({ 
      drawer: false,
      group: null,
      items: [
        { title: 'Home', icon: 'mdi-home', to: '/home' },
        { title: 'Profile', icon: 'mdi-account-circle-outline', to: '/profile' },
        { title: 'Matches', icon: 'mdi-account-group', to: '/matches' },
        { title: 'Settings', icon: 'mdi-cog', to: '/settings'},
        { title: 'Log Out', icon: 'mdi-logout', to: '/'}
      ],
    }),

    watch: {
      group () {
        this.drawer = false
      },
    },
  }
</script>

<style scoped>
  .scrollbar-hidden::-webkit-scrollbar {
    display: none;
  }
</style>