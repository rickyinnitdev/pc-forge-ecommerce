<template>
  <section class="mx-auto max-w-2xl rounded-2xl border border-emerald-600/40 bg-emerald-500/10 p-8 text-center">
    <h1 class="text-4xl font-bold text-white">Order Confirmed</h1>
    <p class="mt-3 text-lg text-emerald-200">Thank you! Your order #{{ route.params.id }} has been placed successfully.</p>
    <router-link to="/products" class="mt-6 inline-block rounded-xl bg-brand-600 px-5 py-3 font-semibold text-white hover:bg-brand-500">
      Continue Shopping
    </router-link>
  </section>
</template>

<script setup>
import { useRoute } from "vue-router";

const route = useRoute();
</script>
