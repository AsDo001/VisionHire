<!-- Modal.vue -->
<template>
  <div class="modal" v-if="visible" @click.self="closeModal">
    <div class="modal__content">
      <slot></slot>
      <button class="modal__close-btn" @click="closeModal"><Cancel /></button>
    </div>
  </div>
</template>

<script setup>
import Cancel from "@/assets/svg/Cancel.vue";
import { ref } from "vue";
const emit = defineEmits(["close"]);
const visible = ref(false);

const openModal = () => {
  visible.value = true;
};

const closeModal = () => {
  visible.value = false;
  emit("close");
};

defineExpose({
  openModal,
});
</script>

<style lang="scss">
.modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;

  &__content {
    background-color: white;
    padding: 2rem;
    border-radius: 5px;
    position: relative;
  }

  &__close-btn {
    position: absolute;
    top: 0.5rem;
    right: 0.5rem;
    background-color: var(--sbg);
    color: var(--contrast);
    display: flex;
    justify-content: center;
    align-content: center;
    border-radius: 100px;
    padding: 12px 0;
    width: 50px;
    height: 50px;
    border: none;
    cursor: pointer;
  }
}
</style>
