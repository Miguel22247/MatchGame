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
					:loading="loading"
					class="mx-auto my-12"
					max-width="374"
					>
					<template slot="progress">
						<v-progress-linear
						color="deep-blue"
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
							<v-rating
								:value="4.5"
								color="amber"
								dense
								half-increments
								readonly
								size="14"
							></v-rating>
					
							<div class="grey--text ms-4">
								4.5 (413)
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
							active-class="blue accent-4 white--text"
							column
							>
								<v-chip><v-icon>mdi-steam</v-icon></v-chip>
						
								<v-chip><v-icon>mdi-discord</v-icon></v-chip>
						
								<v-chip><v-icon>mdi-twitter</v-icon></v-chip>
							</v-chip-group>
						</v-card-text>
				
						<v-card-actions>
							<v-btn
							color="deep-blue lighten-2"
							text
							@click="reserve"
							>
							Match
							</v-btn>
						</v-card-actions>
					</v-card>
					<v-card
					:loading="loading"
					class="mx-auto my-12"
					max-width="374"
					>
					<template slot="progress">
						<v-progress-linear
						color="deep-purple"
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
						<v-rating
							:value="3.0"
							color="amber"
							dense
							half-increments
							readonly
							size="14"
						></v-rating>
				
						<div class="grey--text ms-4">
							3.0 (200)
						</div>
						</v-row>
				
						<div class="my-4 text-subtitle-1">
							First Person Shooter Player
						</div>
				
						<div>Small plates, salads & sandwiches - an intimate setting with 12 indoor seats plus patio seating.</div>
					</v-card-text>
				
					<v-divider class="mx-4"></v-divider>
				
					<v-card-title>Social Media</v-card-title>
				
					<v-card-text>
						<v-chip-group
						v-model="selection"
						active-class="red accent-4 white--text"
						column
						>
							<v-chip><v-icon>mdi-steam</v-icon></v-chip>
					
							<v-chip><v-icon>mdi-discord</v-icon></v-chip>
						</v-chip-group>
					</v-card-text>
				
					<v-card-actions>
						<v-btn
						color="deep-blue lighten-2"
						text
						@click="reserve"
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