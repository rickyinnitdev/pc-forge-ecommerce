<template>
  <section class="mx-auto max-w-3xl space-y-6">
    <h1 class="text-4xl font-bold text-white">Checkout</h1>

    <form class="space-y-4 rounded-2xl border border-slate-800 bg-slate-900/70 p-6" @submit.prevent="submitOrder">
      <div class="grid gap-4 md:grid-cols-2">
        <input v-model="form.customer_name" required placeholder="Full Name" class="input" />
        <input v-model="form.customer_email" required type="email" placeholder="Email" class="input" />
      </div>
      <input v-model="form.address" required placeholder="Address" class="input" />
      <div class="grid gap-4 md:grid-cols-2">
        <input v-model="form.city" required placeholder="City" class="input" />
        <input v-model="form.zip_code" required placeholder="ZIP Code" class="input" />
      </div>
      <p class="text-slate-300">Order Total: <span class="font-semibold text-white">${{ cart.subtotal.toFixed(2) }}</span></p>
      <button class="w-full rounded-xl bg-brand-600 px-4 py-3 font-semibold text-white hover:bg-brand-500" type="submit">
        Place Order
      </button>
    </form>
  </section>
</template>

<script setup>
import { reactive } from "vue";
import { useRouter } from "vue-router";
import api from "../services/api";
import { useCartStore } from "../stores/cart";

const router = useRouter();
const cart = useCartStore();

const form = reactive({
  customer_name: "",
  customer_email: "",
  address: "",
  city: "",
  zip_code: "",
});

async function submitOrder() {
  const payload = {
    ...form,
    session_id: cart.sessionId,
  };
  const { data } = await api.post("/orders/checkout", payload);
  await cart.clearAfterCheckout();
  await router.push(`/order-confirmation/${data.id}`);
}
</script>

<style scoped>
.input {
  @apply w-full rounded-lg border border-slate-700 bg-slate-950 px-3 py-2 text-slate-100 focus:border-brand-500 focus:outline-none;
}
</style>
