<template>
  <div class="modal" v-if="isVisible" @click.self="close">
    <div class="modal__content">
      <slot></slot>
      <button class="modal__close-btn" @click="close"><Cancel /></button>
    </div>
  </div>
</template>

<script setup>
import { ref, defineEmits, defineProps, watch } from 'vue';
import Cancel from "@/assets/svg/Cancel.vue";
const props = defineProps({
  modelValue: {
    type: Boolean,
    default: false,
  },
});

const emit = defineEmits(['update:modelValue']);

const isVisible = ref(props.modelValue);

const close = () => {
  isVisible.value = false;
  emit('update:modelValue', isVisible.value);
};


watch(() => props.modelValue, (newValue) => {
  isVisible.value = newValue;
});
</script>

<style scoped lang="scss">
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
    padding: 12.5px 0;
    width: 50px;
    height: 50px;
    border: none;
    cursor: pointer;
  }
}
</style>
