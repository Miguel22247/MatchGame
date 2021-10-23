<template>
	<v-container fill-height fluid mt-14>
    	<v-row align="top" justify="center">
			<h3>Miguel22247</h3>
		</v-row>
		<v-row align="center" justify="center">
			<h4>Bio</h4>
			<p>Simulation player that likes to play to Euro Truck Simulator 2, American Truck Simulator and Farming Simulator 2019</p>
		</v-row>
		<v-row justify="space-around" align="center">
			<v-col align="center">
				<h3>Social Accounts</h3>
				<v-chip-group
				center-active
				v-model="selection"
				column
				>
					<v-chip active-class="indigo darken-2 accent-4 white--text"><v-icon>mdi-steam</v-icon> Steam</v-chip>

					<v-chip active-class="orange accent-4 white--text"><v-icon>mdi-origin</v-icon> Origin</v-chip>

					<v-chip active-class="blue-grey accent-4 white--text"><v-icon>mdi-ubisoft</v-icon> Ubisoft</v-chip>
			
					<v-chip active-class="blue accent-4 white--text"><v-icon>mdi-discord</v-icon> Discord</v-chip>
			
					<v-chip active-class="light-blue accent-4 white--text"><v-icon>mdi-twitter</v-icon> Twitter</v-chip>

				</v-chip-group>
			</v-col>
		</v-row>
		<v-row justify="space-around" align="center">
			<v-col align="center">
				<h3>My Games</h3>
				<v-card color="#ffffff" outlined>
					<v-chip-group
					align="right"
					v-model="selection"
					column
					>
					<v-chip active-class="red darken-2 accent-4 white--text"><v-icon>mdi-truck</v-icon>Euro Truck Simulator</v-chip>

					<v-chip active-class="green accent-4 white--text"><v-icon>mdi-tractor</v-icon> Farming Simulator</v-chip>

					<v-chip active-class="blue-grey accent-4 white--text"><v-icon>mdi-airplane</v-icon> FSX</v-chip>
			
					<v-chip active-class="blue accent-4 white--text"><v-icon>mdi-target</v-icon> CS:GO</v-chip>
			
					<v-chip active-class="light-blue accent-4 white--text"><v-icon>mdi-car</v-icon> Asseto Corsa</v-chip>
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