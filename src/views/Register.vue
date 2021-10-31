<template>
  <v-container fill-height pa-16>
    <v-row align="center" justify="center" grow>
      <v-form @submit.prevent="submit">
        <v-alert
          v-if="errorMessage == 404"
          dense
          type="error"
          >User not found.</v-alert
        >
        <v-alert
          v-if="errorMessage == 400"
          dense
          type="error"
          >Wrong password.</v-alert
        >
        <v-col fill-height>
          <v-text-field
            label="E-mail"
            v-model="email"
            outlined
            clearable
            append-icon="mdi-email"
            :rules="emailRules"
          ></v-text-field>

          <v-text-field
            v-model="password"
            label="Password"
            outlined
            clearable
            append-icon="mdi-key"
            type="password"
            :rules="passwordRules"
          >
          </v-text-field>

          <v-flex text-center>
            <v-btn outlined type="submit">Log in</v-btn>
          </v-flex>
        </v-col>
      </v-form>
    </v-row>
  </v-container>
</template>

<script>
import axios from "axios";
export default {
  data: function () {
    return {
      username: "",
      email: "",
      password: "",
    };
  },
  methods: {
    onSubmit: function () {
      const url = "http://35.190.147.190:5000/api/user";
      const datos = {
        username: this.username,
        email: this.email,
        password: this.password,
      };
      const headers = {
        "Access-Control-Allow-Origin": "*",
      };
      axios
        .post(url, datos, { headers })
        .then(() => {
          this.$router.push("/home");
        })
        .catch(function (error) {
          console.log(error.response);
          alert(error.response.data);
        });
      // .finally(() => {
      //     //Perform action in always
      // });
    },
  },
};
</script>
