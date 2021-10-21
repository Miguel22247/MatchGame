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
						<v-btn color="#00A7CC" outlined depressed small>
							<v-icon color="#ffffff">
								mdi-arrow-left
							</v-icon>
						</v-btn>
					</router-link>
				</div>
			</div>
			<div class="container">
				<div class="nickname">
					<h4> Miguel22247 </h4> <!-- Add dynamic username with login -->
				</div>
                <div class="bio">
					<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent quam libero, facilisis a posuere nec, tempor vel risus. Etiam dictum tortor erat, vel aliquam arcu aliquet vitae. In semper, magna at hendrerit pretium, ligula nisl vulputate lacus, sed varius ligula purus at orci.</p>
				</div>
				<div class="games">
					<ul>
					</ul>
				</div>
				<div class="social-accounts">
					<ul>
						<div class="social-account">
                            <p class="text-social">Social media</p>
							<v-row  align="center" justify="space-around">
                            <a target="_blank" href="https://steamcommunity.com/id/Miguel22247/">
								<v-btn color="#00A7CC" outlined depressed small>
									<v-icon color="#ffffff">
										mdi-steam
									</v-icon>
                                    Steam
								</v-btn>
                            </a>
							<a target="_blank" href="https://discord.gg/Z5K4NWmbDq">
								<v-btn color="#00A7CC" outlined depressed small>
									<v-icon color="#ffffff">
										mdi-discord
									</v-icon>
                                    Discord
								</v-btn>
                            </a>
                            <a target="_blank" href="https://discord.gg/Z5K4NWmbDq">
								<v-btn color="#00A7CC" outlined depressed small>
									<v-icon color="#ffffff">
										mdi-twitter
									</v-icon>
                                    Twitter
								</v-btn>
                            </a>
							</v-row>
						</div>
					</ul>
				</div>
                <div class="games">
                    <ul>
						<div class="game-list">
                            <p class="text-game">Games</p>
							<v-row  align="center" justify="space-around">
                            <a target="_blank" href="https://steamcommunity.com/id/Miguel22247/">
								<v-btn color="#00A7CC" outlined depressed small mx-2>
									<v-icon color="#ffffff" mx-2>
										mdi-truck
									</v-icon>
                                    ETS 2
								</v-btn>
                            </a>
							<a target="_blank" href="https://discord.gg/Z5K4NWmbDq">
								<v-btn color="#00A7CC" outlined depressed small>
									<v-icon color="#ffffff">
										mdi-tractor
									</v-icon>
                                    FS 2019
								</v-btn>
                            </a>
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

    a {
        text-decoration: none;
    }

    .my-profile-text {
        position: absolute;
        top: 6%;
        left: 60%;
        color: #00A7CC;
        font-size: 20px;
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

	.bio {
		width: 90%;
		height: 10%;
		position: absolute;
        top: 20%;
        left: 9%;
		font-size: 70%;
		color: #00A7CC;
		text-align: center;
        padding: 0px 0;
	}

	.social-accounts {
        width: 25%;
        height: 40%;
        position: absolute;
        top: 35%;
        left: 60%;
        color: #00A7CC;
        font-size: 18px;
        text-align: center;
	}

    .games {
        width: 50%;
        height: 40%;
        justify-content: space-between;
        position: absolute;
        top: 35%;
        left: 10%;
        color: #00A7CC;
        font-size: 18px;
        text-align: center;
	}

    .game-list {
    justify-content: center;
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

    a {
        text-decoration: none;
    }

    .my-profile-text {
        position: absolute;
        top: 5%;
        left: 60%;
        color: #00A7CC;
        font-size: 20px;
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

	.bio {
		width: 90%;
		height: 10%;
		position: absolute;
        top: 20%;
        left: 5%;
		font-size: 70%;
		color: #00A7CC;
		text-align: center;
        padding: 0px 0;
	}

	.social-accounts {
        width: 50%;
        height: 40%;
        position: absolute;
        top: 35%;
        left: 50%;
        color: #00A7CC;
        font-size: 18px;
        text-align: center;
	}

    .games {
        width: 50%;
        height: 40%;
        justify-content: space-between;
        position: absolute;
        top: 35%;
        left: 3%;
        color: #00A7CC;
        font-size: 18px;
        text-align: center;
	}

    .game-list {
    justify-content: center;
    }
}
</style>
