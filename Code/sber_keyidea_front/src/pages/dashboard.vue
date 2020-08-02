<template>
	<div>
		

		<!-- {{chartdata}} -->

		<chart :chartdata="chartdata" :options="options"></chart>
	</div>
</template>



<script>
import chart from '@/components/chart'
export default {
	data() {
		return {
			chartdata: 
			{
			  labels: ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 
			  			'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь'],
			  datasets: [
				{
					label: 'Отзывы на AppStore',
					backgroundColor: '#f87979',
					data: [40, 20, 12, 39, 10, 40, 39, 80, 40, 20, 12, 11]
				}
			  ]
			}, 
			options: {responsive: true, maintainAspectRatio: false}

		}
	},
	components: {
		chart
	}
}

</script>