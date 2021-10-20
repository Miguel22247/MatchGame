<template>
    <div class="landing-page">
        <div class="on-desktop">
            <div class="desktop-table">
                <h3>Check back soon for the Desktop version!</h3>
                <img class='no-desktop' src="./../../public/icons/sad.png" alt="Sad">
            </div>
        </div>
        <div class="mobile-landing">
            <div class="welcome-text">
                <h5>Welcome to Gamematch</h5>
            </div>
            <div class="sign-in-button">
                <router-link to="/signin"><button>Sign In</button></router-link>
            </div>
            <div class="sign-up-button">
                <router-link to="/signup"><button>Sign Up</button></router-link>
            </div>
        </div>
    </div>
</template>
<script>

</script>

<style scoped>
/*for browsers*/
@media screen and (min-width:1025px){

    * {
        box-sizing: border-box;
        margin: 0;
        padding: 0;
    }

    .on-desktop {
        display: none;
    }

    .mobile-landing {
        height: 100%;
    }

    .landing-page {
        background-color: #292929;
        height: 100%;
        width: 100%;
        position: fixed;
    }

    .welcome-text {
        color: #00A7CC;
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        font-family: Roboto;
        font-style: normal;
        font-weight: normal;
        font-size: 20px;
    }
    .sign-in-button {
        position: absolute;
        top: 70%;
        left: 50%;
        transform: translate(-50%, -70%);
    }
    .sign-in-button button {
        border: 1px solid #00A7CC;
        top: 50%;
        left: 50%;
        width: 211px;
        height: 70px;
        color: #00A7CC;
        border-radius: 10px;
    }

    .sign-up-button {
        position: absolute;
        top: 82%;
        left: 50%;
        transform: translate(-50%, -50%);
    }

    .sign-up-button button {
        background: #00A7CC;
        top: 50%;
        left: 50%;
        width: 211px;
        height: 70px;
        color: #ffffff;
        border-radius: 10px;
    }
}
/*for mobile devices*/
@media screen and (max-width: 1024px){

    * {
        box-sizing: border-box;
        margin: 0;
        padding: 0;
    }

    .on-desktop {
        display: none;
    }

    .mobile-landing {
        height: 100%;
    }

    .landing-page {
        background-color: #292929;
        height: 100%;
        width: 100%;
        position: fixed;
    }

    .welcome-text {
        color: #00A7CC;
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        font-family: Roboto;
        font-style: normal;
        font-weight: normal;
        font-size: 20px;
    }
    .sign-in-button {
        position: absolute;
        top: 70%;
        left: 50%;
        transform: translate(-50%, -70%);
    }
    .sign-in-button button {
        border: 1px solid #00A7CC;
        top: 50%;
        left: 50%;
        width: 211px;
        height: 70px;
        color: #00A7CC;
        border-radius: 10px;
    }

    .sign-up-button {
        position: absolute;
        top: 82%;
        left: 50%;
        transform: translate(-50%, -50%);
    }

    .sign-up-button button {
        background: #00A7CC;
        top: 50%;
        left: 50%;
        width: 211px;
        height: 70px;
        color: #ffffff;
        border-radius: 10px;
    }
}
</style>
