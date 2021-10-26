<template>
  <v-container class="container" fluid fill-height>
    <v-row align="top" justify="center">
			<h3>Welcome!</h3>
		</v-row>
    <v-layout row>
      <v-flex xs12 sm6 offset-sm3>
        <v-card color="#ffffff" outlined>
          <v-card-text>
            <v-container>
              <form v-on:submit.prevent="onSubmit">
                <v-layout row>
                  <v-flex xs12>
                    <v-text-field
                      outlined
                      rounded
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
                      outlined
                      rounded
                      color="#00A7CC"
                      name="username"
                      label="Username"
                      id="username"
                      v-model="username"
                      type="text"
                      required></v-text-field>
                  </v-flex>
                </v-layout>
                <v-layout row>
                  <v-flex xs12>
                    <v-text-field
                      outlined
                      rounded
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
                    <v-btn outlined rounded color="#00A7CC" type="submit">Sign up</v-btn>
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
      username: '',
      email: '',
      password: '',
    }
  },
  // async created() {
  //   try {
      
  //     const req = await axios.post(apiurl, this.userData);

  //   } catch (e) {
  //     console.error(e);
  //   }
  // },

  methods: {
    onSubmit: function(){
       const datos = { 'username': this.username, 'email': this.email, 'password': this.password };
       const headers = {
         "Access-Control-Allow-Origin": "*"
       };
       axios.post('http://35.190.147.190:5000/api/user', datos, { headers });
        // .then((res) => {
        //     //Perform Success Action
        //     axios.post(url, )
        // })
        // .catch((error) => {
        //     // error.response.status Check status code
        // });
        // .finally(() => {
        //     //Perform action in always
        // });
    }
  },
}
</script>
