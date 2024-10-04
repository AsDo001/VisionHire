import Login from '../views/Login.vue'
import Registration from "../views/Registration.vue";
import DashBoard from "@/views/DashBoard.vue";
import Home from '../views/Home.vue';	

import {isAuthenticated, logout } from "@/modules/auth";
import { createRouter, createWebHistory } from 'vue-router';

const routes = [
	{
		path: "/",
		name: 'home',
        component: Home,
		meta: { requiresAuth: false}
	},
	{
		path: '/dashboard',
		name: 'dashboard',
		component: DashBoard,
		meta: { requiresAuth: true}
	},
	{
		path: '/auth/login',
		name: 'login',
		component: Login,
		meta: { requiresAuth: false }
	},
	{
		path: '/auth/registration',
		name: 'registration',
		component: Registration,
		meta: { requiresAuth: false }
	}
]

export const router = createRouter({
	history: createWebHistory(process.env.BASE_URL),
	routes
})

router.beforeEach(async (to, from, next) => {
	if (to.matched.some((record) => record.meta.requiresAuth)) {
	  	const isAuth = await isAuthenticated();
	  	if (!isAuth) {
			logout();
			return;
	  	}
	}
	next();
});
