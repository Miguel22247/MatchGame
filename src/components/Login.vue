<template>
  <v-container class="container" fluid fill-height>
    <v-row align="top" justify="center">
			<h3>Welcome Back!</h3>
		</v-row>
    <v-layout row>
      <v-flex xs12 sm6 offset-sm3>
        <v-card color="#ffffff" outlined>
          <v-card-text>
            <v-container>
              <form @submit.prevent="onSignup">
                <v-layout row>
                  <v-flex xs12>
                    <v-text-field
                      rounded
                      outlined
                      color="#00A7CC"
                      name="email"
                      label="Mail"
                      id="email"
                      v-model="email"
                      type="email"
                      required></v-text-field>
                  </v-flex>
                </v-layout>
                <v-layout row>
                  <v-flex xs12>
                    <v-text-field
                      rounded
                      outlined
                      color="#00A7CC"
                      name="password"
                      label="Password"
                      id="password"
                      v-model="password"
                      type="password"
                      required></v-text-field>
                  </v-flex>
                </v-layout>
                <v-layout row>
                  <v-flex xs12>
                    <v-btn color="#00A7CC" rounded outlined type="submit">Log in</v-btn>
                  </v-flex>
                </v-layout>
              </form>
            </v-container>
          </v-card-text>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>
<script>
import axios from 'axios'

export default {
  data: function() {
    return {
      email: '',
      password: '',
    }
  },

  methods: {
    onSubmit: function(){
       const datos = {'email': this.email, 'password': this.password };
       const headers = {
         "Access-Control-Allow-Origin": "*"
       };
       axios.post('http://35.190.147.190:5000/validate_user', datos, { headers });
  }
  }
}
</script>
<style scoped>
.container {
  height: 100%;
}
</style>

