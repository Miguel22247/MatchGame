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
      email: "",
      password: "",
      emailRules: [
        (v) => !!v || "E-mail is required",
        (v) =>
          /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(v) ||
          "E-mail must be valid",
        (v) => v.length <= 30 || "Max 30 characters",
      ],
      passwordRules: [
        (v) => !!v || "Password is required",
        (v) => v.length >= 8 || "Min 8 characters",
        (v) => v.length <= 30 || "Max 30 characters",
      ],
      errorMessage: "",
    };
  },

  methods: {
    async submit() {
      const url = "http://35.190.147.190:5000/api/validate_user";
      const datos = { email: this.email, password: this.password };
      const headers = {
        "Access-Control-Allow-Origin": "*",
      };

      axios
        .post(url, datos, { headers })
        .then((response) => {
          this.$store.commit("set_id", response.data.id);
          this.$router.push("/home");
        })
        .catch((error) => {
          console.log(error.response);
          console.log(error.response.status);
          this.errorMessage = error.response.status;
        });
    },
  },
};
</script>

<style scoped></style>
