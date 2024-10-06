<script setup>
import Copyright from "@/assets/svg/Copyright.vue";
import Logo from "@/assets/svg/Logo.vue";
</script>

<template>
  <footer>
    <div class="logo">
      <Copyright /><span>2024 · </span>
      <Logo />
    </div>
    <div class="links">
      <a>Terms of Use</a>
      <a>Privacy Policy</a>
      <a>Licensing</a>
      <a>Contact</a>
    </div>
  </footer>
</template>

<style scoped lang="scss">
footer {
  display: flex;
  border-radius: 10px 10px 0 0;
  height: 60px;
  width: 100%;
  background: var(--lavander);
  padding: 0 20px;
  justify-content: space-between;

  .logo {
    display: flex;
    color: white;
    gap: 5px;
    font-size: 20px;
    align-items: center;
  }

  .links {
    display: flex;
    gap: 20px;
    align-items: center;

    a {
      color: white;
      cursor: pointer;
    }
  }
}
</style>
