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
      this.saveThemeToCookies();
    },
    saveThemeToCookies() {
      document.cookie = `theme=${this.theme}; path=/; max-age=31536000`; 
    },
    loadThemeFromCookies() {
      const themeCookie = document.cookie.split('; ').find(row => row.startsWith('theme='));
      if (themeCookie) {
        this.theme = themeCookie.split('=')[1];
        document.body.classList.add(this.theme);
      }
    },
  },
});


export default useThemeStore;
