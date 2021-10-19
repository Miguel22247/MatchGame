<template>
    <div class="landing-page">
        <div class="on-desktop">
            <div class="desktop-table">
                <h3>Check back soon for the Desktop version!</h3>
                <img class='no-desktop' src="./../../public/icons/sad.png" alt="Sad">
            </div>
        </div>
        <div class="mobile-landing">
            <div class="header">			
				<div class="my-profile-text">
					<h5>My Profile</h5>
				</div>
				<div class="return-button">
					<router-link to="/home">
						<v-btn color="#00A7CC" small>
							<v-icon color="#ffffff">
								mdi-arrow-left
							</v-icon>
						</v-btn>
					</router-link>
				</div>
			</div>
			<div class="container">
				<div class="nickname">
					<p> Miguel22247 </p> <!-- Add dynamic username with login -->
				</div>
				<div class="bio">
				</div>
				<div class="games">
					<ul>
						<li v-for="game in games" :key="game.name">
						{{ game.name }}
						</li>
					</ul>
				</div>
				<div class="social-accounts">
					<ul>
						<li v-for="social in socials" :key="social.name">
							{{ social.name }}
						</li>
						<div class="social-account"> 
							<v-row  align="center" justify="space-around">
								<v-btn color="#00A7CC" small>
									<v-icon color="#ffffff">
										mdi-steam
									</v-icon>
								</v-btn>
								<v-btn color="#00A7CC" small>
									<v-icon color="#ffffff">
										mdi-discord
									</v-icon>
								</v-btn>
							</v-row>
						</div>
					</ul>
				</div>
			</div>
        </div>
	</div>
</template>
<script>
</script>

<style scoped>
@media screen and (min-width:1025px) {
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

    .my-profile-text {
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

@media screen and (max-width:1024px) {
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

    .my-profile-text {
        position: absolute;
        top: 6.5%;
        left: 60%;
        color: #00A7CC;
    }

    .return-button button {
        position: absolute;
        top: 5%;
        left: 10%;
    }

	.nickname {
		color: #00A7CC;
		text-align: right;
		position: absolute;
		top: 15%;
		left: 10%;
	}

	.social-accounts {
	}
}
</style>