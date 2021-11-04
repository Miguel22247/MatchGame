import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from "vuex-persistedstate";

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    id: ""
  },

  // Vuex mutations each have a string type and a handler function
  // The handler function is where we alter or change the state, 
  // and it will receive the state as the first argument.

  // this.$store.commit('set_id', user_id)
  // this.$store.commit (commits a mutation)
  mutations: {
    set_id (state, user_id) {
      state.id = user_id
    }
  },
  // actions are triggered thorough 'dispatch' method 
  // this.$store.dispatch
  actions: {
  },
  modules: {
  },
  plugins: [createPersistedState({
    storage: window.sessionStorage,
  })],
  getters: {
    getId: state => {
      return state.id
    }
  }
})
