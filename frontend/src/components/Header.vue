<script setup>
import Language from "@/assets/svg/Language.vue";
import Logo from "@/assets/svg/Logo.vue";
import Sun from "@/assets/svg/Sun.vue";
import useThemeStore from "@/store/theme";
import { useRouter } from "vue-router";
import { ref, onMounted } from "vue";
import Modal from "@/components/Modal.vue";
import { isAuthenticated, logout } from "@/modules/auth";
import LogoutIcon from "@/assets/svg/LogoutIcon.vue";
import Moon from "@/assets/svg/Moon.vue";

const router = useRouter();
const themeStore = useThemeStore();

const { page } = defineProps({
  page: {
    type: String,
    default: "land",
  },
});

const isModalVisible = ref(false);
const isauth = ref(false);

const openModal = () => {
  isModalVisible.value = true;
};

onMounted(async () => {
  const a = await isAuthenticated();
  if (a) {
    isauth.value = true;
  }
});
</script>

<template>
  <div class="header">
    <div class="logo" @click="router.push('/')">
      <Logo />
    </div>
    <div class="btns">
      <button
        class="btn green"
        v-if="!isauth"
        @click="router.push('/auth/login')"
      >
        Вход
      </button>
      <button
        class="btn lavander"
        v-if="!isauth"
        @click="router.push('/auth/registration')"
      >
        Регистрация
      </button>
      <button class="btn lavander" v-if="isauth" @click="openModal">
        Профиль
      </button>
      <button class="btn green logout-btn" v-if="isauth" @click="logout">
        <LogoutIcon />
      </button>
      <button class="btn red">
        <Language />
      </button>
      <button :class="`btn ${themeStore.theme==='light'?'yellow': 'moon'}`" @click="themeStore.toggleTheme">
        <Sun v-if="themeStore.theme==='light'"/>
        <Moon v-else/>
      </button>
    </div>
  </div>
  <Modal v-model="isModalVisible">
    <h2>модалка</h2>
  </Modal>
</template>

<style scoped lang="scss">
.header {
  display: flex;
  justify-content: space-between;
  width: 100%;
  margin: 0 0 70px;
  height: 80px;

  padding: 15px 20px;
  border-radius: 10px;
  background: var(--sbg);

  z-index: 3;

  .logo {
    display: flex;
    justify-content: center;
    align-items: center;
    background: var(--gradient);
    border-radius: 10px;
    color: white;
    padding: 16px 32px;
    gap: 10px;
    cursor: pointer;

    &_stick {
      width: 3px;
      height: 35px;
      background-color: white;
      border-radius: 5px;
    }

    &_text {
      font-size: 15px;
      line-height: 17px;
      width: 60px;
    }
  }

  .btns {
    display: flex;
    gap: 25px;

    .link {
      color: white;
      text-decoration: none;
    }

    .btn {
      cursor: pointer;
    }

    .btn.logout-btn {
      padding: 0;
      width: 50px;
      height: 50px;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    .btn.green {
      background-color: var(--green);
    }

    .btn.lavander {
      background-color: var(--lavander);
    }

    .btn.red {
      background-color: var(--red);
      padding: 10px;
    }

    .btn.yellow {
      background-color: var(--yellow);
      padding: 12px;
    }

    .btn.moon {
      background-color: var(--sbg-dark);
      padding: 12px;
    }
    
  }
}
</style>
