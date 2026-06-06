<template>
  <section v-if="product" class="grid gap-8 md:grid-cols-2">
    <div class="space-y-3">
      <img :src="selectedImage" :alt="product.name" class="h-96 w-full rounded-2xl object-cover" />
      <div class="grid grid-cols-3 gap-2">
        <button
          v-for="(image, index) in gallery"
          :key="index"
          class="overflow-hidden rounded-xl border"
          :class="selectedImage === image ? 'border-brand-500' : 'border-slate-700'"
          @click="selectedImage = image"
        >
          <img :src="image" :alt="`Gallery ${index}`" class="h-20 w-full object-cover" />
        </button>
      </div>
    </div>

    <div class="space-y-5">
      <p class="text-sm uppercase tracking-[0.2em] text-brand-200">{{ product.category }}</p>
      <h1 class="text-4xl font-bold text-white">{{ product.name }}</h1>
      <p class="text-xl font-semibold text-brand-100">${{ product.price.toFixed(2) }}</p>
      <p class="text-slate-300">{{ product.description }}</p>
      <p class="text-sm text-slate-400">Stock: {{ product.stock_quantity }} available</p>

      <div class="flex w-full max-w-xs items-center gap-3">
        <input
          v-model.number="quantity"
          type="number"
          min="1"
          :max="product.stock_quantity"
          class="w-20 rounded-lg border border-slate-700 bg-slate-900 px-3 py-2"
        />
        <button
          class="flex-1 rounded-xl bg-brand-600 px-4 py-3 font-semibold text-white hover:bg-brand-500"
          @click="addToCart"
        >
          Add to Cart
        </button>
      </div>
    </div>
  </section>
</template>

<script setup>
import { computed, onMounted, ref } from "vue";
import { useRoute } from "vue-router";
import api from "../services/api";
import { useCartStore } from "../stores/cart";

const route = useRoute();
const cart = useCartStore();

const product = ref(null);
const selectedImage = ref("");
const quantity = ref(1);

const gallery = computed(() => {
  if (!product.value) return [];
  const base = product.value.image_url;
  return [base, `${base}&sat=-40`, `${base}&hue=20`];
});

async function fetchProduct() {
  const { data } = await api.get(`/products/${route.params.id}`);
  product.value = data;
  selectedImage.value = data.image_url;
}

async function addToCart() {
  await cart.addToCart(product.value.id, quantity.value);
}

onMounted(fetchProduct);
</script>
