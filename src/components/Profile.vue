<template>
	<v-container fill-height fluid mt-14>
    	<v-row align="top" justify="center">
			<h3>Miguel22247</h3>
		</v-row>
		<v-row align="center" justify="center">
			<h4>Bio</h4>
			<p>Simulation player that likes to play to Euro Truck Simulator 2, American Truck Simulator and Farming Simulator 2019</p>
		</v-row>
		<v-row justify="space-around">
			<v-col>
				<h3>Social Accounts</h3>
				<v-card color="#ffffff" outlined>
					<v-chip-group
					align="right"
					v-model="selection"
					active-class="deep-blue accent-4 white--text"
					column
					>
						<v-chip><v-icon>mdi-steam</v-icon></v-chip>
				
						<v-chip><v-icon>mdi-discord</v-icon></v-chip>
				
						<v-chip><v-icon>mdi-twitter</v-icon></v-chip>
					</v-chip-group>
				</v-card>
			</v-col>
		</v-row>
		<v-row justify="space-around">
			<v-col>
				<h3>My Games</h3>
				<v-card color="#ffffff" outlined>
					<v-chip-group
					align="right"
					v-model="selection"
					active-class="deep-blue accent-4 white--text"
					column
					>
						<v-chip><v-icon>mdi-truck</v-icon></v-chip>
				
						<v-chip><v-icon>mdi-tractor</v-icon></v-chip>
				
						<v-chip><v-icon>mdi-airplane</v-icon></v-chip>

						<v-chip><v-icon>mdi-target</v-icon></v-chip>
					</v-chip-group>
				</v-card>
			</v-col>
		</v-row>
	</v-container>
</template>

<style scoped>
a {
	text-decoration: none;
}
</style>