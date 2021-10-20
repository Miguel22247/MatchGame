<template>
    <div class="landing-page">
        <div class="on-desktop">
            <div class="desktop-table">
                <h3>Check back soon for the Desktop version!</h3>
                <img class='no-desktop' src="./../../public/icons/sad.png" alt="Sad">
            </div>
        </div>
        <div class="mobile-landing">
            <div class="my-matches-text">
                <h5>My Matches</h5>
            </div>
            <div class="return-button">
                <router-link to="/home">
                    <v-btn color="#00A7CC" outlined depressed>
                        <v-icon color="#00A7CC" outlined depressed>
                            mdi-arrow-left
                        </v-icon>
                    </v-btn>
                </router-link>
            </div>
            <div class="navbar">
                <v-row
                align="center"
                justify="space-around"
                >
                    <v-btn color="#00A7CC" outlined depressed>
                        <v-icon color="#ffffff">mdi-account-multiple-minus</v-icon>
                    </v-btn>
                </v-row>
            </div>
        </div>
    </div>
</template>
<script>
</script>

<style scoped>
/*for browsers*/
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
}
/*for mobile*/
@media screen and (max-width: 1024px) {
    .on-desktop {
        display: none;
    }

    .landing-page {
        background-color: #292929;
        height: 100%;
        width: 100%;
        position: fixed;
    }

    * {
        box-sizing: border-box;
        margin: 0;
        padding: 0;
    }

    .my-matches-text {
        position: absolute;
        top: 15%;
        left: 10%;
        color: #00A7CC;
    }

    .return-button button {
        position: absolute;
        top: 5%;
        left: 10%;
        font-weight: bold;
        font-size: 20px;
    }

    .navbar {
        width: 100%;
        height: 40px;
        position: absolute;
        top: 90%;
    }

}
</style>
