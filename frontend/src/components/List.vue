<template>
  <div class="wrap">

    <div v-if="type === 'cand'" class="wrapper">

      <Modal v-model="isModalFilter">


      </Modal>
      
      <div class="header">
        <h1 class="header_title">{{ title }}</h1>
        <div class="header_btns">
          <div class="search">
            <input class="search_input" v-model="searchQuery" />
            <button class="search_btn">
              <Search />
            </button>
          </div>
          <button class="filter" @click="openModalFilter">
            <Filter />
          </button>
        </div>
      </div>

      <div class="list cand">
       

        <div v-for="(item, index) in filteredList" :key="item.id" v-if="isSearch">
          <div class="item" v-if="index < 5">
            <div class="img-text">
              <div class="img"></div>
              <div class="text">
                <div class="text_fio">{{ item.name }}</div>
                <div class="text_desc">{{ item.description }}</div>
              </div>
            </div>
            <div :class="`btns ${states[`${item.status}`].color}`">
              <button class="profile">
                <Profile />
              </button>
              <div class="state">
                <span class="state_text">{{ states[`${item.status}`].text }}</span>
                <button class="state_btn">
                  <ArrowDown />
                </button>
              </div>
            </div>
          </div>
        </div>

        <div v-for="(item, index) in paginatedList" :key="item.id + 1" v-else>
          <div class="item" v-if="index < 5">
            <div class="img-text">
              <div class="img"></div>
              <div class="text">
                <div class="text_fio">{{ item.name }}</div>
                <div class="text_desc">{{ item.description }}</div>
              </div>
            </div>
            <div :class="`btns ${states[`${item.status}`].color}`">
              <button class="profile">
                <Profile />
              </button>
              <div class="state">
                <span class="state_text">{{ states[`${item.status}`].text }}</span>
                <button class="state_btn">
                  <ArrowDown />
                </button>
              </div>
            </div>
          </div>
        </div>

      </div>
    </div>

    <div v-if="type === 'todo'"  class="wrapper">
      <Modal v-model="isModalVisible">
        <div :style="{ display: 'flex', flexDirection: 'column', gap: '10px' }">
          <!-- говно! не осуждать -->
          <input class="search_input" v-model="title_todo">
          <input v-model="description_todo">
          <input v-model="task_receiver" v-if="role=='admin'">
          <div>send</div @click="create_task(role, title_todo, description_todo, task_receiver)">
        </div>
      </Modal>
      <div class="header">
        <h1 class="header_title">{{ title }}</h1>
        <div class="header_btns">
          <div class="search">
            <input class="search_input" v-model="searchQueryTODO" />
            <button class="search_btn">
              <Search />
            </button>
          </div>
          <button class="filter">
            <Filter />
          </button>
          <div class="add_todo" @click="openModal">
            <Plus/>

          </div>
        </div>
      </div>



      

      <div class="list todo">

        



       
        <div class="item" v-for="(item, index) in filteredListTODO" :key="index" v-if="isSearchTODO">
          <div class="img-text">
            <div class="img"></div>
            <div class="text">
              <div class="text_fio">
                {{ item.description.length > 15 ? item.description.slice(0, 17) + "..." : item.description }}
              </div>
              <div :class="`text_desc ${item.role === 'd' && 'colored'}`">
                {{ item.author }}
              </div>
            </div>
          </div>
          <div class="btns">
            <button :class="`check ${item.status && 'active'}`" @click="item.status = !item.status">
              <Check />
            </button>
            <button class="modal_btn" @click="openModal">
              <Details />
            </button>
          </div>
          <Modal  v-model="isModalVisible">
            <h2>{{ 'фыв' }}</h2>
          </Modal>
        </div>
      

      
    
        <div class="item" v-for="(item, index) in paginatedList" :key="index+1" v-else>
          <div class="img-text">
            <div class="img"></div>
            <div class="text">
              <div class="text_fio">
                {{ item.description.length > 15 ? item.description.slice(0, 17) + "..." : item.description }}
              </div>
              <div :class="`text_desc ${item.role === 'd' && 'colored'}`">
                {{ item.author }}
              </div>
            </div>
          </div>
          <div class="btns">
            <button :class="`check ${item.status && 'active'}`" @click="item.status = !item.status">
              <Check />
            </button>
            <button class="modal_btn" @click="modalRef.openModal">
              <Details />
            </button>
          </div>
          <Modal >
            <h2>{{ 'фыв' }}</h2>
          </Modal>
        </div>
        
      










      </div>




    </div>
    <div class="pagination">
      <button class="pagination_btn pagination_prev" v-if="activePage > 1" @click="prevPage">
        &lt;
      </button>
      <button v-for="page in totalPages" :key="page" :class="`pagination_btn ${page === activePage ? 'active' : ''}`"
        @click="changePage(page)">
        {{ page }}
      </button>
      <button class="pagination_btn pagination_next" v-if="activePage < totalPages" @click="nextPage">
        &gt;
      </button>
    </div>
  </div>
</template>

<script setup>
import ArrowDown from "@/assets/svg/ArrowDown.vue";
import Check from "@/assets/svg/Check.vue";
import Details from "@/assets/svg/Details.vue";
import Filter from "@/assets/svg/Filter.vue";
import Profile from "@/assets/svg/Profile.vue";
import Search from "@/assets/svg/Search.vue";
import Plus from "@/assets/svg/Plus.vue"
import Modal from "@/components/Modal.vue";
// import 'axios' from 'axios'

// import { getAccountInfo } from "@/modules/api";

import { ref, computed } from "vue";


const isModalVisible = ref(false);
const isModalFilter = ref(false)


function openModal(){
  isModalVisible.value = true;
  console.log(1)
};



function openModalFilter(){
  isModalFilter.value = true;
  console.log(1)
};



// const role = ref()
// const title_todo = ref()
// const description_todo = ref()
// const task_receiver = ref()

// onMounted(async () => {
// 	let user = await getAccountInfo()
// 	if (user !== null) {
// 		role.value = user.role
//     console.log(role.value)

   
  
// })

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
const activePage = ref(1);
const modalRef = ref(null);


const ITEMS_PER_PAGE = 5;
const reactiveList = ref(list.map(item => ({ ...item, status: ref(item.status) })));
//фильтровать реактив и передовать в пагинайшен
const paginatedList = computed(() => {
  const start = (activePage.value - 1) * ITEMS_PER_PAGE;
  const end = start + ITEMS_PER_PAGE;
  return reactiveList.value.slice(start, end);
});


const totalPages = computed(() => Math.ceil(list.length / ITEMS_PER_PAGE));

const changePage = (page) => {
  activePage.value = page;
};

const prevPage = () => {
  if (activePage.value > 1) {
    activePage.value--;
  }
};

const nextPage = () => {
  if (activePage.value < totalPages.value) {
    activePage.value++;
  }
};


const searchQuery = ref('')
const isSearch = computed(() => searchQuery.value.length > 0);

const filteredList = computed(() => {
  if (!isSearch.value) return [];

  return reactiveList.value.filter(item =>
    item.name.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
    item.description.toLowerCase().includes(searchQuery.value.toLowerCase())
  );
});

const searchQueryTODO = ref('');
const isSearchTODO = computed(() => searchQueryTODO.value.length > 0);

const filteredListTODO = computed(() => {
    if (!isSearchTODO.value) return [];

    const filteredItems = reactiveList.value.filter(item =>
        item.description.toLowerCase().includes(searchQueryTODO.value.toLowerCase()) ||
        item.author.toLowerCase().includes(searchQueryTODO.value.toLowerCase())
    );

  
    return filteredItems.slice(0, 4);
});

// async function create_task(role, title_todo, description_todo, task_receiver) {
//     if (role === "admin") {
//         try {
//             const taskData = {
//                 title: title_todo,
//                 description: description_todo,
//                 task_receiver: task_receiver,
//             };

//             let response = await axios.post("/api/protected/create_tasks", taskData);
//             console.log("Task created successfully:", response.data);
//         } catch (error) {
//             console.error("Error creating task:", error.response ? error.response.data : error.message);
//             alert("Ошибка при создании задачи: " + (error.response ? error.response.data.detail : error.message));
//         }
//     } else if (role === "recruiter") {
//         try {
//             const taskData = {
//                 title: title_todo,
//                 description: description_todo,
             
//             };

//             let response = await axios.post("/api/protected/create_tasks", taskData);
//             console.log("Task created successfully:", response.data);
//         } catch (error) {
//             console.error("Error creating task:", error.response ? error.response.data : error.message);
//             alert("Ошибка при создании задачи: " + (error.response ? error.response.data.detail : error.message));
//         }
//     } else {
//         alert("Недостаточно прав");
//     }
// }

</script>

<style scoped lang="scss">
.wrap {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100%;
  .wrapper{
    width: 100%;
  }
  .header {
    display: flex;
    gap: 60px;
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
      flex-grow: 1;

      .search {
        height: 100%;
        position: relative;
        display: flex;
        flex-grow: 1;

        &_input {
          border-radius: 10px;
          border: none;
          background-color: var(--sbg);
          flex-grow: 1;
          height: 50px;
          outline-color: var(--lavander);
        }

        &_btn {
          position: absolute;
          background-color: var(--sbg);
          color: var(--text);
          right: 15px;
          top: 12.5px;
          cursor: pointer;
          padding: 0;
        }
      }

      .filter, .add_todo {
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

  .list {
    display: flex;
    flex-direction: column;
    gap: 15px;
    margin: 20px 0 20px;
    width: 100%;
    .item {
      display: flex;
      justify-content: space-between;
      width: 100%;
      border-radius: 10px;
      background-color: var(--sbg);
      padding: 12px 15px;
      position: relative;



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
        align-items: center;
        gap: 15px;
      }
    }

    &.cand {
      width: 100%;

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
            display: flex;
            justify-content: center;
            align-items: center;
            height: 60px;
            width: 60px;
            padding: 0;
          }

          .state {
            position: relative;
            padding: 0 20px;
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
              display: flex;
              align-items: center;
              justify-content: center;
              height: 60px;
              padding: 0;
              cursor: pointer;
            }
          }
        }
      }
    }

    &.todo {
      width: 100%;

      .item {

        .btns {
          .check {
            background: var(--sbg-dark);
            border-radius: 50px;
            display: flex;
            align-items: center;
            justify-content: center;
            width: 50px;
            height: 50px;
            padding: 0;
            color: var(--lavander);
            cursor: pointer;

            &.active {
              background: var(--lavander);
              color: white;
            }
          }

          .modal_btn {
            display: flex;
            align-items: center;
            justify-content: center;
            width: 60px;
            height: 60px;
            padding: 0;
            background: var(--lavander);
            cursor: pointer;
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
      display: flex;
      justify-content: center;
      align-items: center;
      cursor: pointer;

      &.active {
        background-color: var(--lavander);
        color: white;
      }
    }
  }
}
</style>
