<template>
	<v-container fill-height fluid mt-14>
    	<v-row justify="left">
			<h2>Hello Miguel!</h2>
		</v-row>
		<v-row align="center" justify="center">
			<h4>Possible Matches</h4>
		</v-row>
		<v-row justify="space-around">
			<v-col>
				<v-card
					:loading="loading1"
					class="mx-auto my-12"
					max-width="374"
					>
					<template slot="progress">
						<v-progress-linear
						color="blue darken-4"
						height="10"
						indeterminate
						></v-progress-linear>
					</template>
				
				
						<v-card-title>Rielch</v-card-title>
					
						<v-card-text>
							<v-row
							align="center"
							class="mx-0"
							>					
							<div class="grey--text ms-4">
							</div>
							</v-row>
					
							<div class="my-4 text-subtitle-1">
								Simulation Player
							</div>
					
							<div>Player specialized on Euro Truck Simulator and Farming Simulator</div>
						</v-card-text>
					
						<v-divider class="mx-4"></v-divider>
					
						<v-card-title>Social Media</v-card-title>
				
						<v-card-text>
							<v-chip-group
							v-model="selection"
							column
							>
								<v-chip active-class="blue darken-4 white--text"><v-icon>mdi-steam</v-icon></v-chip>
						
								<v-chip active-class="blue accent-4 white--text"><v-icon>mdi-discord</v-icon></v-chip>
						
								<v-chip active-class="light-blue accent-4 white--text"><v-icon>mdi-twitter</v-icon></v-chip>

								<v-chip active-class="orange accent-4 white--text"><v-icon>mdi-account-circle-outline</v-icon></v-chip>

							</v-chip-group>
						</v-card-text>
				
						<v-card-actions>
							<v-btn
							color="blue darken-4"
							text
							@click="match1"
							>
							Match
							</v-btn>
						</v-card-actions>
					</v-card>
					<v-card
					:loading="loading2"
					class="mx-auto my-12"
					max-width="374"
					>
					<template slot="progress">
						<v-progress-linear
						color="blue darken-4"
						height="10"
						indeterminate
						></v-progress-linear>
					</template>
				
				
					<v-card-title>ezedksl</v-card-title>
				
					<v-card-text>
						<v-row
						align="center"
						class="mx-0"
						>
				
						<div class="grey--text ms-4">
						</div>
						</v-row>
				
						<div class="my-4 text-subtitle-1">
							First Person Shooter Player
						</div>
				
						<div>Player specialized on Counter Strike and Call of duty</div>
					</v-card-text>
				
					<v-divider class="mx-4"></v-divider>
				
					<v-card-title>Social Media</v-card-title>
				
					<v-card-text>
						<v-chip-group
						v-model="selection"
						column
						>
							<v-chip active-class="blue darken-4 white--text"><v-icon>mdi-steam</v-icon></v-chip>
					
							<v-chip active-class="blue accent-4 white--text"><v-icon>mdi-discord</v-icon></v-chip>

							<v-chip active-class="orange accent-4 white--text"><v-icon>mdi-account-circle-outline</v-icon></v-chip>
						</v-chip-group>
					</v-card-text>
				
					<v-card-actions>
						<v-btn
						color="blue darken-4"
						text
						@click="match2"
						>
						Match
						</v-btn>
					</v-card-actions>
					</v-card>
			</v-col>
		</v-row>
	</v-container>
</template>
<script>
export default {
	data: () => ({
    loading1: false,
	loading2: false,
    selection: 1,
  }),

  methods: {
    match1 () {
      this.loading1 = true

      setTimeout(() => (this.loading1 = false), 2000)
	  alert("Match successfully done!")
    },
	match2 () {
      this.loading2 = true

      setTimeout(() => (this.loading2 = false), 2000)
	  	  alert("Match successfully done!")

    },
  },
}
</script>