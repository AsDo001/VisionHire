<script setup>
import { Bar, Doughnut, Line } from "vue-chartjs";
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  BarElement,
  ArcElement,
  LineElement,
  CategoryScale,
  LinearScale,
} from "chart.js";
import { defineProps, computed, toRef, ref, onMounted, watch } from "vue";

const getColor = (color) =>
  getComputedStyle(document.documentElement.children[1])
    .getPropertyValue(color)
    .trim();

ChartJS.register(
  Title,
  Tooltip,
  Legend,
  BarElement,
  ArcElement,
  LineElement,
  CategoryScale,
  LinearScale
);

const props = defineProps({
  type: {
    type: String,
    default: "bar",
  },
  labels: {
    type: Array,
    default: () => ["January", "February", "March"],
  },
  label: {
    type: String,
    default: "Sales",
  },
  data: {
    type: Array,
    default: () => [40, 20, 12],
  },
});
const refProps = toRef(props);

const chartData = {
  labels: refProps.value.labels,
  datasets: [
    {
      label: refProps.value.label,
      backgroundColor: [
        getColor("--green"),
        getColor("--red"),
        getColor("--lavander"),
      ],
      data: refProps.value.data,
      borderWidth: 0,
    },
  ],
};

const chartOptions = {
  responsive: true,
  maintainAspectRatio: false,
  plugins: {
    title: {
      display: true,
      text: refProps.value.label,
      font: {
        size: 20,
        weight: "bold",
        family: "Arial",
      },
      color: getColor("--text"),
    },
    legend: {
      display: true,
      labels: {
        color: getColor("--text"),
        font: {
          size: 14,
        },
      },
    },
    tooltip: {
      enabled: false,
    },
  },
};

const myChart = ref(null);
let chartInstance = null;
onMounted(() => {
  const ctx = myChart.value.getContext("2d");
  chartInstance = new ChartJS(ctx, {
    type: "bar", // тип графика
    data: chartData,
    options: chartOptions,
  });
});

watch(
  () => props,
  (n) => {
    chartInstance.destroy();
    const chartData = {
      labels: refProps.value.labels,
      datasets: [
        {
          label: refProps.value.label,
          backgroundColor: [
            getColor("--green"),
            getColor("--red"),
            getColor("--lavander"),
          ],
          data: refProps.value.data,
          borderWidth: 0,
        },
      ],
    };

    const chartOptions = {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        title: {
          display: true,
          text: refProps.value.label,
          font: {
            size: 20,
            weight: "bold",
            family: "Arial",
          },
          color: getColor("--text"),
        },
        legend: {
          display: true,
          labels: {
            color: getColor("--text"),
            font: {
              size: 14,
            },
          },
        },
        tooltip: {
          enabled: false,
        },
      },
    };
    const ctx = myChart.value.getContext("2d");
    chartInstance = new ChartJS(ctx, {
      type: "bar", 
      data: chartData,
      options: chartOptions,
    });
  },
  { deep: true }
);
</script>

<template>
  <div class="chart">
    <canvas ref="myChart"></canvas>
    <Bar
      :data="chartData"
      :options="chartOptions"
      v-if="type === 'bar' && false"
    />
    <Doughnut :data="chartData" :options="chartOptions" v-if="type === 'pie'" />
    <Line :data="chartData" :options="chartOptions" v-if="type === 'line'" />
  </div>
</template>

<style scoped>
.chart {
  min-width: 45%;
  height: 400px;
}
</style>
