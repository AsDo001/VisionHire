<script setup>
import Language from "@/assets/svg/Language.vue";
import Logo from "@/assets/svg/Logo.vue";
import Sun from "@/assets/svg/Sun.vue";
import useThemeStore from "@/store/theme";

const themeStore = useThemeStore();

</script>

<template>
  <div class="header">
    <div class="logo">
      <Logo />
    </div>
    <div class="btns">
      <button class="btn green">
        <RouterLink class="link" to="/auth/login">Вход</RouterLink>
      </button>
      <button class="btn lavander">
        <RouterLink class="link" to="/auth/registration"
          >Регистрация</RouterLink
        >
      </button>
      <button class="btn red"><Language /></button>
      <button class="btn yellow" @click="themeStore.toggleTheme">
        <Sun />
      </button>
    </div>
  </div>
</template>

<style scoped lang="scss">
.header {
  display: flex;
  justify-content: space-between;
  width: calc(90vw - 10px);

  height: 80px;
  position: fixed;
  top: 2rem;
  left: calc(5vw - 2px);
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
  }
}
</style>
