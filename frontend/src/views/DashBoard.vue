<script setup>
import { logout } from "@/modules/auth";
import { getAccountInfo } from "@/modules/api";
import { onMounted, ref } from "vue";
import Header from "@/components/Header.vue";
import Modal from "@/components/Modal.vue";
import List from "@/components/List.vue";
import { candidates } from "@/stubs/Candidats.stubs";
import { todos } from "@/stubs/Todos.stubs";
const modalRef = ref(null);
const name = ref("");

onMounted(async () => {
  let user = await getAccountInfo();
  if (user !== null) {
    name.value = user.name;
  } else {
    logout();
  }
});
</script>

<template>
  <Header page="main" />
  <div class="home">
    <List type="cand" title="Кандидаты" :list="candidates" />
    <List type="todo" title="TODO" :list="todos" />
    <button @click="modalRef.openModal" v-if="false">открыть модалку</button>
    <Modal ref="modalRef">
      <h2>модалка</h2>
    </Modal>
  </div>
</template>

<style scoped lang="scss">
.home {
  padding: 0 5%;
  margin: 150px 0 300px;
  display: flex;
  justify-content: space-between;
  min-height: 100vh;
  width: 100%;

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
