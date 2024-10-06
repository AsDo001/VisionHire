<script setup>
import { logout } from "@/modules/auth";
import { getAccountInfo } from "@/modules/api";
import Footer from "@/components/Footer.vue";
import { onMounted, ref } from "vue";
import Header from "@/components/Header.vue";
import Chart from "@/components/Chart.vue";
import List from "@/components/List.vue";
import Modal from "@/components/Modal.vue";
import Filter from "@/assets/svg/Filter.vue";
import { candidates } from "@/stubs/Candidats.stubs";
import { todos } from "@/stubs/Todos.stubs";
const name = ref("");

onMounted(async () => {
  let user = await getAccountInfo();
  if (user !== null) {
    name.value = user.name;
  } else {
    logout();
  }
});

const dataDictionary = [
  { title: "Соотношение отказов к приглашениям", data: [30, 50, 60] },
  { title: "Процент заполненных вакансий", data: [100, 200, 150] },
];

const chartLabels = ref(["2024-10-07", "2024-10-08", "2024-10-09"]);
const chartData = ref([30, 50, 60]);
const chartLabel = ref("Соотношение отказов к приглашениям");

const isModalVisible = ref(false);
const startDate = ref("");
const endDate = ref("");
const selectedData = ref(dataDictionary[0].title);

const openModalFilterBar = () => {
  isModalVisible.value = true;
};
const closeModalFilterBar = () => {
  isModalVisible.value = false;
};

const applyFilter = () => {
  const start = new Date(startDate.value);
  const end = new Date(endDate.value);
  const dateArray = [];

  for (let d = start; d <= end; d.setDate(d.getDate() + 1)) {
    dateArray.push(new Date(d).toISOString().split("T")[0]); // Формат YYYY-MM-DD
  }

  const filteredData = dataDictionary.find(
    (item) => item.title === selectedData.value
  );

  chartLabels.value = dateArray; // Массив дат для графика
  chartData.value = filteredData.data; // Данные для графика
  chartLabel.value = filteredData.title; // Название графика

  console.log(chartLabels.value);
  console.log(chartData.value);

  closeModalFilterBar();
};
</script>

<template>
  <Header page="main" />
  <div class="home">
    <div class="lists">
      <List type="cand" title="Кандидаты" :list="candidates" class="cand" />
      <List type="todo" title="TODO" :list="todos" class="todo" />
    </div>

    <div class="charts">
      <div class="chart">
        <Chart :labels="chartLabels" :label="chartLabel" :data="chartData" />
        <button class="filter" @click="openModalFilterBar">
          <Filter />
        </button>
      </div>
    </div>

    <Modal
      :modelValue="isModalVisible"
      @update:modelValue="isModalVisible = $event"
    >
      <div>
        <h2>Фильтр графиков</h2>
        <label for="startDate">Начальная дата:</label>
        <input type="date" id="startDate" v-model="startDate" />

        <label for="endDate">Конечная дата:</label>
        <input type="date" id="endDate" v-model="endDate" />

        <label for="dataSelect">Выберите данные:</label>
        <select id="dataSelect" v-model="selectedData">
          <option
            v-for="item in dataDictionary"
            :key="item.title"
            :value="item.title"
          >
            {{ item.title }}
          </option>
        </select>

        <button @click="applyFilter">Применить фильтр</button>
      </div>
    </Modal>

    <img src="/api/protected/my_avatar" v-if="false" />
    <Footer />
  </div>
</template>

<style scoped lang="scss">
.home {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-content: center;
  gap: 50px;
  min-height: 100vh;
  width: 100%;

  .lists {
    display: flex;
    justify-content: space-between;

    .cand {
      width: 50%;
    }

    .todo {
      width: 40%;

    }
  }

  .charts {
    margin: 100px 0 100px;
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content: space-around;
    padding: 0 150px;
    gap: 50px;

    .chart {
      display: flex;
      position: relative;

      .filter {
        position: absolute;
        top: 0px;
        right: 0px;
        background: var(--sbg);
        color: var(--text);
        border-radius: 50px;
        padding: 0;
        width: 50px;
        height: 50px;
        display: flex;
        justify-content: center;
        align-items: center;
        cursor: pointer;
      }
    }
  }

  .title {
    font-size: 40px;
    margin-bottom: 0;
  }

  .description {
    margin-bottom: 30px;
    font-size: 16px;
    color: var(--text);
  }

  .logout-btn {
    background: var(--lavander);
    border-radius: 15px;
    border: none;
    width: 30%;
    max-width: 500;
    height: 60px;
    color: var(--hinted-text);
    font-weight: 600;
    font-size: 18px;
  }
}
</style>
