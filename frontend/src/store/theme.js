import { defineStore } from 'pinia';

const useThemeStore = defineStore('theme', {
  state: () => ({
    theme: 'light',
  }),
  actions: {
    toggleTheme() {
      this.theme = this.theme === 'light' ? 'dark' : 'light';
      document.body.classList.remove(this.theme === 'light' ? 'dark' : 'light');
      document.body.classList.add(this.theme);
    },
  },
});

export default useThemeStore;
