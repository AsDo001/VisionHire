<template>
  <div class="wrap">
    <div class="header">
      <h1 class="header_title">{{ title }}</h1>
      <div class="header_btns">
        <div class="search">
          <input class="search_input" />
          <button class="search_btn"><Search /></button>
        </div>
        <button class="filter"><Filter /></button>
      </div>
    </div>
    <div class="list cand" v-if="type === 'cand'">
      <div v-for="(item, index) in list" :key="item.id">
        <div class="item" v-if="index < 5">
          <div class="img-text">
            <div class="img"></div>
            <div class="text">
              <div class="text_fio">{{ item.name }}</div>
              <div class="text_desc">{{ item.description }}</div>
            </div>
          </div>
          <div :class="`btns ${states[`${item.status}`].color}`">
            <button class="profile"><Profile /></button>
            <div class="state">
              <span class="state_text">{{
                states[`${item.status}`].text
              }}</span>
              <button class="state_btn"><ArrowDown /></button>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="list todo" v-if="type === 'todo'">
      <div class="item" v-for="(item, index) in list" :key="index">
        <div class="img-text">
          <div class="img"></div>
          <div class="text">
            <div class="text_fio">
              {{
                item.description.length > 15
                  ? item.description.slice(0, 17) + "..."
                  : item.description
              }}
            </div>
            <div class="text_desc">{{ item.author }}</div>
            <!-- здесь еще нужно подтягивать от кого сделана задача-->
          </div>
        </div>
        <div class="btns">
          <button class="check"></button>
          <button class="modal_btn"></button>
        </div>
      </div>
    </div>
    <div class="pagination">
      <button class="pagination_btn pagination_prev" v-if="maxPage !== 6">
        <
      </button>
      <button
        class="pagination_btn"
        v-for="(item, index) in list"
        :key="item.id"
      >
        <span v-if="index < maxPage"> </span>
        {{ index + 1 }}
      </button>
      <button
        class="pagination_btn pagination_next"
        v-if="maxPage !== list.length"
      >
        >
      </button>
    </div>
  </div>
</template>

<script setup>
import ArrowDown from "@/assets/svg/ArrowDown.vue";
import Filter from "@/assets/svg/Filter.vue";
import Profile from "@/assets/svg/Profile.vue";
import Search from "@/assets/svg/Search.vue";
import { ref } from "vue";
const states = {
  appointed: { text: "Собеседование назначено", color: "yellow" },
  accepted: { text: "Принято", color: "green" },
  rejected: { text: "Отказано", color: "red" },
  expected: { text: "Ожидание собеседования", color: "lavander" },
};
const { title, type, list } = defineProps({
  title: {},
  type: {},
  list: {},
});

const maxPage = ref(6);
</script>

<style scoped lang="scss">
.wrap {
  display: flex;
  flex-direction: column;
  gap: 20px;
  .header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 60px;
    &_title {
      font-size: 48px;
      color: var(--lavander);
    }
    &_btns {
      display: flex;
      align-items: center;
      gap: 20px;
      height: 50px;
      .search {
        height: 100%;
        position: relative;
        &_input {
          border-radius: 10px;
          border: none;
          background-color: var(--sbg);
          width: 400px;
          height: 50px;
        }
        &_btn {
          position: absolute;
          background-color: var(--sbg);
          right: 15px;
          top: 15px;
          cursor: pointer;
          padding: 0;
        }
      }
      .filter {
        background: var(--sbg);
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
  .list {
    display: flex;
    flex-direction: column;
    gap: 15px;
    .item {
      display: flex;
      justify-content: space-between;
      width: 100%;
      border-radius: 10px;
      background-color: var(--sbg);
      padding: 12px 15px;
      position: relative;
      &::before {
        content: "";
        position: absolute;
        top: -2px;
        left: -2px;
        right: -2px;
        bottom: -2px;
        border-radius: 12px;
        background-image: linear-gradient(to bottom right, #7287fd, #59595900);
        z-index: -1;
      }
      .img-text {
        display: flex;
        gap: 15px;
        align-items: center;
        .img {
          object-fit: cover;
          width: 75px;
          height: 75px;
          background-color: var(--sbg-dark);
          border-radius: 50px;
        }
        .text {
          &_fio {
            color: var(--lavander);
            font-size: 28px;
          }
          &_desc {
            color: var(--text);
            font-size: 22px;
            &.colored {
              color: var(--red);
            }
          }
        }
      }
      .btns {
        display: flex;
        gap: 15px;
      }
    }
    &.cand {
      .item {
        .btns {
          &.green {
            --bg-color: var(--green);
          }
          &.lavander {
            --bg-color: var(--lavander);
          }
          &.red {
            --bg-color: var(--red);
          }
          &.yellow {
            --bg-color: var(--yellow);
          }
          .profile {
            background: var(--bg-color);
          }
          .state {
            position: relative;
            padding: 5px 20px 5px 20px;
            background-color: var(--bg-color);
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            width: 350px;

            &_text {
              color: white;
            }
            &_btn {
              background-color: var(--bg-color);

              padding: 0;
              cursor: pointer;
            }
          }
        }
      }
    }
    &.todo {
      .item {
        .btns {
          .check {
            background: var(--sbg-dark);
            border-radius: 50px;
            padding: 15px;
            color: var(--lavander);
            &.active {
              background: var(--lavander);
              color: white;
            }
          }
          .modal_btn {
            background: var(--lavander);
          }
        }
      }
    }
  }
  .pagination {
    max-width: 0 auto;
    width: 330px;
    display: flex;
    gap: 5px;
    &_btn {
      width: 40px;
      height: 40px;
      border-radius: 10px;
      background-color: var(--sbg);
      color: var(--lavander);
      padding: 10px;
      cursor: pointer;
      &.active {
        background-color: var(--lavander);
        color: white;
      }
    }
  }
}
</style>
