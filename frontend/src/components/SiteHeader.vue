<template>
  <header class="sticky top-0 z-30 border-b border-slate-800 bg-slate-950/90 backdrop-blur">
    <div class="mx-auto flex max-w-7xl items-center justify-between px-4 py-4 sm:px-6 lg:px-8">
      <router-link to="/" class="text-2xl font-bold tracking-wide text-white">PC Forge</router-link>
      <nav class="flex items-center gap-5 text-sm">
        <router-link class="text-slate-300 transition hover:text-white" to="/">Home</router-link>
        <router-link class="text-slate-300 transition hover:text-white" to="/products">Shop</router-link>
        <router-link class="text-slate-300 transition hover:text-white" to="/cart">
          Cart ({{ cart.totalItems }})
        </router-link>
        <router-link class="rounded-lg border border-brand-500 px-3 py-1 text-brand-100 hover:bg-brand-600/30" to="/admin/dashboard">
          Admin
        </router-link>
      </nav>
    </div>
  </header>
</template>

<script setup>
import { onMounted } from "vue";
import { useCartStore } from "../stores/cart";

const cart = useCartStore();

onMounted(async () => {
  if (!cart.items.length) {
    await cart.fetchCart();
  }
});
</script>
