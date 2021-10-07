<template>
    <div class="landing-page">
        <div class="on-desktop">
            <div>&nbsp;</div>
            <div>&nbsp;</div>
            <div>&nbsp;</div>
            <div class="desktop-table">
                <h3>Check back soon for the Desktop version!</h3>
                <img class='no-desktop' src="./../../public/icons/sad.png" alt="Sad">
            </div>
        </div>
        <div class="mobile-landing">
        </div>
    </div>
</template>
<script>
</script>
<style scoped>
/*for browsers*/
@media screen and (min-width:821px){
    .on-desktop {
        color: #00A7CC;
        text-align: center;
        vertical-align: center;
    }
}
/*for mobile devices*/
@media screen and (max-width: 820px){

    .on-desktop {
        display: none;
    }
    * {
        box-sizing: border-box;
        margin: 0;
        padding: 0;
    }

}
</style>