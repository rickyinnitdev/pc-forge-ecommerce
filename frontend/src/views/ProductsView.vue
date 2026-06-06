<template>
  <section class="space-y-6">
    <h1 class="text-4xl font-bold text-white">All Products</h1>

    <div class="grid gap-4 rounded-2xl border border-slate-800 bg-slate-900/60 p-4 md:grid-cols-4">
      <input
        v-model="filters.search"
        type="text"
        placeholder="Search products"
        class="rounded-lg border border-slate-700 bg-slate-950 px-3 py-2 text-sm text-slate-100 focus:border-brand-500 focus:outline-none"
      />
      <select
        v-model="filters.category"
        class="rounded-lg border border-slate-700 bg-slate-950 px-3 py-2 text-sm text-slate-100 focus:border-brand-500 focus:outline-none"
      >
        <option value="">All categories</option>
        <option v-for="category in categories" :key="category" :value="category">{{ category }}</option>
      </select>
      <input
        v-model.number="filters.minPrice"
        type="number"
        min="0"
        placeholder="Min price"
        class="rounded-lg border border-slate-700 bg-slate-950 px-3 py-2 text-sm text-slate-100 focus:border-brand-500 focus:outline-none"
      />
      <input
        v-model.number="filters.maxPrice"
        type="number"
        min="0"
        placeholder="Max price"
        class="rounded-lg border border-slate-700 bg-slate-950 px-3 py-2 text-sm text-slate-100 focus:border-brand-500 focus:outline-none"
      />
    </div>

    <div class="grid gap-6 sm:grid-cols-2 lg:grid-cols-4">
      <ProductCard v-for="product in products" :key="product.id" :product="product" @add="addToCart" />
    </div>
  </section>
</template>

<script setup>
import { onMounted, reactive, ref, watch } from "vue";
import ProductCard from "../components/ProductCard.vue";
import api from "../services/api";
import { useCartStore } from "../stores/cart";

const products = ref([]);
const categories = ref([]);
const cart = useCartStore();

const filters = reactive({
  search: "",
  category: "",
  minPrice: null,
  maxPrice: null,
});

async function fetchCategories() {
  const { data } = await api.get("/products/categories");
  categories.value = data;
}

async function fetchProducts() {
  const params = {};
  if (filters.search) params.search = filters.search;
  if (filters.category) params.category = filters.category;
  if (filters.minPrice !== null) params.min_price = filters.minPrice;
  if (filters.maxPrice !== null) params.max_price = filters.maxPrice;

  const { data } = await api.get("/products", { params });
  products.value = data;
}

async function addToCart(productId) {
  await cart.addToCart(productId, 1);
}

watch(filters, fetchProducts, { deep: true });

onMounted(async () => {
  await Promise.all([fetchCategories(), fetchProducts(), cart.fetchCart()]);
});
</script>
