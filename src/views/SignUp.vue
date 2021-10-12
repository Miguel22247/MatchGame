<template>
    <div class="landing-page">
        <div class="on-desktop">
            <div class="desktop-table">
                <h3>Check back soon for the Desktop version!</h3>
                <img class='no-desktop' src="./../../public/icons/sad.png" alt="Sad">
            </div>
        </div>
        <div class="mobile-landing">
            <div class="signup-text">
                <h5>Welcome to Gamematch</h5>
            </div>
            <div class="signup-forms">
                <div class="return-button">
                    <router-link to="/">
                        <v-btn color="#00A7CC">
                            <v-icon color="#ffffff">
                                mdi-arrow-left
                            </v-icon>
                        </v-btn>
                    </router-link>
                </div>
                <div class="signup-form-basic">
                    <form class="signup-form">

                        <input type="text" class="signup-email" placeholder="Email">
                        <input type="text" class="signup-username" placeholder="Username">
                        <input type="text" class="signup-password" placeholder="Password">
                        <input type="text" class="signup-confirm-password" placeholder="Confirm password">
                        <input type="text" class="signup-gametag" placeholder="Gametag (at least one)">
                    </form>
                    <router-link to="/home"><button class="button-signup-submit" type="submit">Sign Up</button></router-link>
                </div>
                <!--- Add the signup with google button here --->
            </div>
        </div>
    </div>
</template>

<style scoped>
@media screen and (min-width:1025px){
    .on-desktop {
        color: #00A7CC;
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
    }

    .on-desktop img {
        margin-top: 10px;
        position: absolute;
        left: 50%;
        transform: translate(-50%, 0%);
    }
    .mobile-landing {
        display: none;
    }

    .landing-page {
        background-color: #292929;
        height: 100%;
        width: 100%;
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
        height: 50px;
        width: 50px;
        position: absolute;
        top: 5%;
        left: 10%;
    }
    .signup-text{
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

    .signup-forms {
        width: 100%;
        height: 100%;
        position: absolute;
        left: 50%;
        top: 50%;
        transform: translate(-50%, -50%);
    }

    .signup-email {
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

        .signup-username {
        width: 211px;
        color: #00A7CC;
        border-radius: 10px;
        border: 1px solid #00A7CC;
        position: absolute;
        top: 40%;
        left: 50%;
        transform: translate(-50%, -50%);
        text-align: center;
    }

    .signup-password {
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

    .signup-confirm-password{
        width: 211px;
        color: #00A7CC;
        border-radius: 10px;
        border: 1px solid #00A7CC;
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        text-align: center;
    }

    .signup-gametag {
        width: 211px;
        color: #00A7CC;
        border-radius: 10px;
        border: 1px solid #00A7CC;
        position: absolute;
        top: 55%;
        left: 50%;
        transform: translate(-50%, -50%);
        text-align: center;
    }

    .button-signup-submit {
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
}
</style>
