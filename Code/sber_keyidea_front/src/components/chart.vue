<script>

import { Line } from 'vue-chartjs'

export default {
  extends: Line,
  props: ['chartdata', 'options'],
  mounted () {
    this.renderChart(this.chartdata, this.options)
  }
}


// import VueChartJs from 'VueChartJs'

// export default {
//  extends: VueChartJs.Line,
//  	mounted () {
//     this.renderChart({
//       labels: ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь'],
//       datasets: [
//         {
//           label: 'Коммиты на GitHub',
//           backgroundColor: '#f87979',
//           data: [40, 20, 12, 39, 10, 40, 39, 80, 40, 20, 12, 11]
//         }
//       ]
//     }, {responsive: true, maintainAspectRatio: false})
//   }
// }

</script>