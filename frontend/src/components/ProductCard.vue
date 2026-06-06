<template>
  <article class="group overflow-hidden rounded-2xl border border-slate-800 bg-slate-900/70 shadow-lg transition hover:-translate-y-1 hover:border-brand-500/50 hover:shadow-glow">
    <img :src="product.image_url" :alt="product.name" class="h-48 w-full object-cover" />
    <div class="space-y-2 p-4">
      <p class="text-xs uppercase tracking-wider text-brand-200">{{ product.category }}</p>
      <h3 class="line-clamp-2 text-lg font-semibold text-white">{{ product.name }}</h3>
      <p class="text-sm text-slate-300">${{ product.price.toFixed(2) }}</p>
      <div class="flex gap-2 pt-2">
        <router-link
          :to="`/products/${product.id}`"
          class="flex-1 rounded-lg border border-slate-700 px-3 py-2 text-center text-sm text-slate-200 hover:border-slate-500"
        >
          View
        </router-link>
        <button
          class="flex-1 rounded-lg bg-brand-600 px-3 py-2 text-sm font-semibold text-white hover:bg-brand-500"
          @click="$emit('add', product.id)"
        >
          Add
        </button>
      </div>
    </div>
  </article>
</template>

<script setup>
defineProps({
  product: {
    type: Object,
    required: true,
  },
});

defineEmits(["add"]);
</script>
