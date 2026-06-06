<template>
  <div class="mb-6 flex flex-wrap items-center gap-3 rounded-2xl border border-slate-800 bg-slate-900/70 p-4">
    <router-link class="nav-link" to="/admin/dashboard">Dashboard</router-link>
    <router-link class="nav-link" to="/admin/products">Products</router-link>
    <router-link class="nav-link" to="/admin/orders">Orders</router-link>
    <router-link class="nav-link" to="/admin/inventory">Inventory</router-link>
    <button class="ml-auto rounded-lg border border-rose-500 px-3 py-2 text-sm text-rose-300" @click="handleLogout">Logout</button>
  </div>
</template>

<script setup>
import { useRouter } from "vue-router";
import { useAdminStore } from "../stores/admin";

const router = useRouter();
const admin = useAdminStore();

function handleLogout() {
  admin.logout();
  router.push("/admin/login");
}
</script>

<style scoped>
.nav-link {
  @apply rounded-lg border border-slate-700 px-3 py-2 text-sm text-slate-200 hover:border-brand-500;
}
</style>
