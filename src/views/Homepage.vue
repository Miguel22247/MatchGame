<template>
    <div class="landing-page">
        <div class="on-desktop">
            <div class="desktop-table">
                <h3>Check back soon for the Desktop version!</h3>
                <img class='no-desktop' src="./../../public/icons/sad.png" alt="Sad">
            </div>
        </div>
        <div class="mobile-landing">
			<div class="hello-user">
					<h5>Hello Miguel!</h5> <!--- Add the ability to recognize the user ---->
			</div>
			<div class="display-info">
				<p class='nickname'>Rielch</p>
				<div class="bio">
					<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent quam libero, facilisis a posuere nec, tempor vel risus. Etiam dictum tortor erat, vel aliquam arcu aliquet vitae. In semper, magna at hendrerit pretium, ligula nisl vulputate lacus, sed varius ligula purus at orci.</p>
				</div>
				<div class="games">
					<ul>
						<li v-for="game in games" :key="game.message">
							{{ game.message }}
						</li>
					</ul>
				</div>
			</div>
			<div class="navbar">
				<v-row
				align="center"
				justify="space-around"
				>
					<router-link to="/matches">
						<v-btn color="#00A7CC">
							<v-icon color="#ffffff">mdi-account-multiple-plus</v-icon>
						</v-btn>
					</router-link>
					<router-link to="/profile">
						<v-btn color="#00A7CC">
							<v-icon color="#ffffff">mdi-face-man-profile</v-icon>
						</v-btn>
					</router-link>
				</v-row>
			</div>
		</div>
	</div>
</template>
<script>
</script>
<style scoped>
@media screen and (min-width:1025px){
    .on-desktop {
        display: none;
    }

    .landing-page {
		position: fixed;
        background-color: #292929;
        height: 100%;
        width: 100%;
    }

	* {
        box-sizing: border-box;
        margin: 0;
        padding: 0;
    }

    a {
        text-decoration: none;
    }

	.hello-user {
		position: absolute;
		top: 10%;
		left: 10%;
		color: #00A7CC;
		font-weight: bold;
		font-size: 20px;
	}

	.navbar {
		width: 100%;
		height: 40px;
		position: absolute;
		top: 90%;
	}

	.display-info {
		border: 1px solid blue;
		width: 70%;
		height: 65%;
		position: fixed;
		top: 15%;
		left: 15%;
		margin: 1%;
	}

	.nickname {
		color: #00A7CC;
	}

	.bio {
		width: 100%;
		height: 40%;
		font-size: 100%;
		color: #00A7CC;
		text-align: left;
	}

	.games {
		border: 1px solid red;
		width: 100%;
		height: 49%;
	}
}
@media screen and (max-width: 1024px){
    .on-desktop {
        display: none;
    }

    .landing-page {
		position: fixed;
        background-color: #292929;
        height: 100%;
        width: 100%;
    }

	* {
        box-sizing: border-box;
        margin: 0;
        padding: 0;
    }

    a {
        text-decoration: none;
    }

	.hello-user {
		position: absolute;
		top: 10%;
		left: 10%;
		color: #00A7CC;
		font-weight: bold;
		font-size: 20px;
	}

	.navbar {
		width: 100%;
		height: 40px;
		position: absolute;
		top: 90%;
	}

	.display-info {
		border: 1px solid blue;
		width: 70%;
		height: 65%;
		position: fixed;
		top: 15%;
		left: 15%;
		margin: 1%;
	}

	.nickname {
		color: #00A7CC;
	}

	.bio {
		width: 100%;
		height: 40%;
		position: relative;
		font-size: 70%;
		color: #00A7CC;
		text-align: left;
		border: 1px solid green;
	}

	.games {
		border: 1px solid red;
		width: 100%;
		height: 49%;
	}
}
</style>