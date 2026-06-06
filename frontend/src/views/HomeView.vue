<template>
  <section class="space-y-10">
    <div class="grid gap-6 rounded-3xl border border-slate-800 bg-gradient-to-r from-slate-900 via-slate-900 to-brand-700/40 p-8 md:grid-cols-2 md:p-10">
      <div class="space-y-5">
        <p class="text-sm uppercase tracking-[0.25em] text-brand-200">High Performance Hardware</p>
        <h1 class="text-4xl font-bold leading-tight text-white md:text-5xl">Build Your Dream PC Setup</h1>
        <p class="text-slate-200">
          Shop gaming PCs, office workstations, and premium components with fast checkout and trusted support.
        </p>
        <router-link to="/products" class="inline-block rounded-xl bg-brand-600 px-6 py-3 font-semibold text-white hover:bg-brand-500">
          Explore Products
        </router-link>
      </div>
      <img
        src="https://images.unsplash.com/photo-1598550476439-6847785fcea6?auto=format&fit=crop&w=1300&q=80"
        alt="Gaming setup"
        class="h-full w-full rounded-2xl object-cover"
      />
    </div>

    <div>
      <div class="mb-5 flex items-center justify-between">
        <h2 class="text-3xl font-bold text-white">Featured Products</h2>
        <router-link to="/products" class="text-brand-200 hover:text-brand-100">View all</router-link>
      </div>
      <div class="grid gap-6 sm:grid-cols-2 lg:grid-cols-4">
        <ProductCard v-for="product in featuredProducts" :key="product.id" :product="product" @add="addToCart" />
      </div>
    </div>
  </section>
</template>

<script setup>
import { computed, onMounted, ref } from "vue";
import ProductCard from "../components/ProductCard.vue";
import api from "../services/api";
import { useCartStore } from "../stores/cart";

const products = ref([]);
const cart = useCartStore();
const featuredProducts = computed(() => products.value.slice(0, 4));

async function loadProducts() {
  const { data } = await api.get("/products");
  products.value = data;
}

async function addToCart(productId) {
  await cart.addToCart(productId, 1);
}

onMounted(async () => {
  await Promise.all([loadProducts(), cart.fetchCart()]);
});
</script>
