<template>
    <div class="landing-page">
        <div class="on-desktop">
            <div class="desktop-table">
                <h3>Check back soon for the Desktop version!</h3>
                <img class='no-desktop' src="./../../public/icons/sad.png" alt="Sad">
            </div>
        </div>
        <div class="mobile-landing">
            <div class="return-button">
                <router-link to="/">
                    <v-btn
                    class="ma-2"
                    color="#00A7CC"
                    dark
                    >
                        <v-icon
                            dark
                            left
                        >
                            mdi-arrow-left
                        </v-icon>Back
                    </v-btn>
                </router-link>
            </div>
            <div class="login-text">
                <h5>Welcome Back</h5>
            </div>
        </div>
    </div>
</template>

<style scoped>
@media screen and (min-width:821px){
    .on-desktop {
        color: #00A7CC;
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
    }

    .on-desktop img {
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
@media screen and (max-width: 820px){
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
        width: 90px;
        position: absolute;
        top: 5%;
        left: 5%;
    }
    .login-text{
        font-family: Roboto;
        font-style: normal;
        font-weight: normal;
        font-size: 26px;
        line-height: 35px;
        color: #00A7CC;

        position: absolute;
        left: 5%;
        top: 17%;
    }
}
</style>