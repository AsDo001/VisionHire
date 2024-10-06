<template>
	<div :class="themeStore.theme">
		<router-view />
	</div>
</template>
<script setup>
import useThemeStore from "@/store/theme";

const themeStore = useThemeStore();
themeStore.loadThemeFromCookies();
</script>
<style lang="scss">
@import "./styles/light-theme.scss";
@import "./styles/dark-theme.scss";

.light {
	@include light-theme;
}

.dark {
	@include dark-theme;
}

:root {
	--lavander: #7287fd;
	--green: #39e9a7;
	--gradient: linear-gradient(to bottom right, #39e9a7, #7287fd);
	--red: #ff86aa;
	--yellow: #ffe872;

	text-rendering: optimizeLegibility;
	-webkit-font-smoothing: antialiased;
	-webkit-text-size-adjust: 100%;
	font-family: "Noto", sans-serif;
	font-weight: 700;
	scroll-behavior: smooth;
}

* {
	box-sizing: border-box;
	transition: all 0.1s ease;
}

body.light {
	@include light-theme;
}

body.dark {
	@include dark-theme;
}

body {
	background: var(--bg);
	color: var(--text);
	margin: 0;
	padding: 30px 5vw 0;
}

button {
	padding: 6px 25px;
	border-radius: 10px;
	color: white;
	outline: none;
	border: none;
	font-size: 20px;
	font-family: "Noto", sans-serif;
	font-weight: 700;
}

h1 {
	margin: 0;
}

p {
	margin: 0;
}
</style>
