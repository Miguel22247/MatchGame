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
			<div>
				<input type="text" class="search" placeholder="Search">
				<router-link to="/search"><v-btn class="btn">Search</v-btn></router-link>
			</div>
			<div class="display-info">

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
<script></script>
<style scoped>
@media screen and (min-width:1025px){
    .on-desktop {
        display: none;
    }

    .landing-page {
        background-color: #292929;
        height: 100vh;
        width: 100vh;
    }

	.btn {
		position: absolute;
		top: 50%;
		left: 60%;
		color: #00A7CC;
		transform: translate(-50%, -50%);
	}

	* {
        box-sizing: border-box;
        margin: 0;
        padding: 0;
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
		width: 100vh;
		height: 40px;
		position: absolute;
		top: 95%;
	}
	.search {
		color: #00A7CC;
		border: 1px solid #00A7CC;
		border-radius: 5px;
		text-align: center;
		position: absolute;
		width: 250px;
		top: 50%;
		left: 50%;
		transform: translate(-50%, -50%);
	}
}
@media screen and (max-width: 1024px){
    .on-desktop {
        display: none;
    }

    .landing-page {
        background-color: #292929;
        height: 100vh;
        width: 100vh;
    }

	* {
        box-sizing: border-box;
        margin: 0;
        padding: 0;
    }

	.hello-user {
		position: absolute;
		top: 10%;
		left: 10%;
		color: #00A7CC;
		font-weight: bold;
		font-size: 20px;
	}

		.btn {
		position: absolute;
		top: 49%;
		left: 65%;
		color: #00A7CC;
	}

	.navbar {
		width: 100vh;
		height: 40px;
		position: absolute;
		top: 95%;
	}
	.search {
		color: #00A7CC;
		border: 1px solid #00A7CC;
		border-radius: 5px;
		text-align: center;
		position: absolute;
		width: 250px;
		top: 50%;
		left: 50%;
		transform: translate(-50%, -50%);
	}
}
</style>