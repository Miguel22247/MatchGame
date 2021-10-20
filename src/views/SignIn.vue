<template>
    <div class="landing-page">
        <div class="on-desktop">
            <div class="desktop-table">
                <h3>Check back soon for the Desktop version!</h3>
                <img class='no-desktop' src="./../../public/icons/sad.png" alt="Sad">
            </div>
        </div>
        <div class="mobile-landing">
            <div class="login-text">
                <h5>Welcome Back</h5>
            </div>
            <div class="login-forms">
                <div class="return-button">
                    <router-link to="/">
                        <v-btn color="#00A7CC" small>
                            <v-icon color="#ffffff">
                                mdi-arrow-left
                            </v-icon>
                        </v-btn>
                    </router-link>
                </div>
                <div class="login-form-basic">
                    <form class="login-form">
                        <input type="text" class="login-email" name="email" placeholder="Email">
                        <input type="password" class="login-password" name="password" placeholder="Password">
                    </form>
                    <router-link to="/home"><button class="button-login-submit" type="submit">Sign In</button></router-link>
                    <p class="signup-message"> if you don't have an account you can create it <a href="/signup">here</a></p>	
                </div>
                <!--- Add the login button here --->
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'signIn',
        data() {
            return {
                email: '',
                password: '',
            }
        },
        methods: {}
    }
</script>

<style scoped>
@media screen and (min-width:1025px){
    .on-desktop {
        display: none;
    }

    .landing-page {
        background-color: #292929;
        height: 100%;
        width: 100%;
    }
    * {
        box-sizing: border-box;
        margin: 0;
        padding: 0;
    }

    .return-button button {
        position: absolute;
        top: 5%;
        left: 10%;
    }
    .login-text{
        font-family: Roboto;
        font-style: normal;
        font-weight: normal;
        font-size: 26px;
        line-height: 35px;
        color: #00A7CC;

        position: absolute;
        left: 10%;
        top: 15%;
    }

    .login-forms {
        width: 100%;
        height: 100%;
        position: absolute;
        left: 50%;
        top: 50%;
        transform: translate(-50%, -50%);
    }

    .login-email {
        width: 211px;
        color: #00A7CC;
        border-radius: 10px;
        border: 1px solid #00A7CC;
        position: absolute;
        top: 35%;
        left: 50%;
        transform: translate(-50%, -50%);
        text-align: center;
    }

    .login-password {
        width: 211px;
        color: #00A7CC;
        border-radius: 10px;
        border: 1px solid #00A7CC;
        position: absolute;
        top: 45%;
        left: 50%;
        transform: translate(-50%, -50%);
        text-align: center;
    }

    .button-login-submit {
        width: 211px;
        height: 70px;
        color: #FFFFFF;
        background-color: #00A7CC;
        border-radius: 10px;
        position: absolute;
        top: 60%;
        left: 50%;
        transform: translate(-50%, 0%);
    }

    .signup-message {
        color: #FFFFFF;
        position: absolute;
        left: 50%;
        top: 80%;
        transform: translate(-50%, 0);
        text-decoration: none;
        text-align: center;
        font-size: 14px;
    }
}

/*for mobile devices*/
@media screen and (max-width: 1024px){
    .on-desktop {
        display: none;
    }

    .landing-page {
        background-color: #292929;
        height: 100%;
        width: 100%;
    }
    * {
        box-sizing: border-box;
        margin: 0;
        padding: 0;
    }

    .return-button button {
        position: absolute;
        top: 5%;
        left: 10%;
    }
    .login-text{
        font-family: Roboto;
        font-style: normal;
        font-weight: normal;
        font-size: 26px;
        line-height: 35px;
        color: #00A7CC;

        position: absolute;
        left: 10%;
        top: 15%;
    }

    .login-forms {
        width: 100%;
        height: 100%;
        position: absolute;
        left: 50%;
        top: 50%;
        transform: translate(-50%, -50%);
    }

    .login-email {
        width: 211px;
        color: #00A7CC;
        border-radius: 10px;
        border: 1px solid #00A7CC;
        position: absolute;
        top: 35%;
        left: 50%;
        transform: translate(-50%, -50%);
        text-align: center;
    }

    .login-password {
        width: 211px;
        color: #00A7CC;
        border-radius: 10px;
        border: 1px solid #00A7CC;
        position: absolute;
        top: 45%;
        left: 50%;
        transform: translate(-50%, -50%);
        text-align: center;
    }

    .button-login-submit {
        width: 211px;
        height: 70px;
        color: #FFFFFF;
        background-color: #00A7CC;
        border-radius: 10px;
        position: absolute;
        top: 60%;
        left: 50%;
        transform: translate(-50%, 0%);
    }

    .signup-message {
        color: #FFFFFF;
        position: absolute;
        left: 50%;
        top: 80%;
        transform: translate(-50%, 0);
        text-decoration: none;
        text-align: center;
        font-size: 9px;
    }

}
</style>