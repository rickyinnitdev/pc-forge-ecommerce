import { defineStore } from "pinia";
import api from "../services/api";

export const useAdminStore = defineStore("admin", {
  state: () => ({
    token: localStorage.getItem("admin_token") || null,
  }),
  getters: {
    isAuthenticated: (state) => Boolean(state.token),
  },
  actions: {
    async login(email, password) {
      const { data } = await api.post("/auth/login", { email, password });
      this.token = data.access_token;
      localStorage.setItem("admin_token", data.access_token);
    },
    logout() {
      this.token = null;
      localStorage.removeItem("admin_token");
    },
  },
});
