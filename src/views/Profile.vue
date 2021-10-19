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
@media screen and (min-width:1025px) {
	.landing-page {
		background-color: #292929;
		height: 100%;
		width: 100%;
	}

	.desktop-table {
		display: none;
	}
}

@media screen and (max-width:1024px) {
	.landing-page {
		background-color: #292929;
		height: 100%;
		width: 100%;
	}

}
</style>