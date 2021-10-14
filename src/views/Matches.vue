<template>
	<div class="landing-page">
        <div class="on-desktop">
            <div class="desktop-table">
                <h3>Check back soon for the Desktop version!</h3>
                <img class='no-desktop' src="./../../public/icons/sad.png" alt="Sad">
            </div>
        </div>
	</div>
</template>
<script>
</script>

<style scoped>
/*for browsers*/
@media screen and (min-width:1025px){
    .landing-page {
        background-color: #292929;
        height: 100%;
        width: 100%;
    }

    .mobile-landing {
        display: none;
    }

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
}

@media screen and (max-width: 1024px) {
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
</style>