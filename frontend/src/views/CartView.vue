<template>
  <section class="space-y-6">
    <h1 class="text-4xl font-bold text-white">Shopping Cart</h1>

    <div v-if="!cart.items.length" class="rounded-2xl border border-slate-800 bg-slate-900/60 p-8 text-slate-300">
      Your cart is empty.
    </div>

    <div v-else class="space-y-4">
      <article
        v-for="item in cart.items"
        :key="item.id"
        class="flex flex-col gap-4 rounded-2xl border border-slate-800 bg-slate-900/60 p-4 md:flex-row md:items-center"
      >
        <img :src="item.product.image_url" :alt="item.product.name" class="h-24 w-24 rounded-lg object-cover" />
        <div class="flex-1">
          <h2 class="text-lg font-semibold text-white">{{ item.product.name }}</h2>
          <p class="text-sm text-slate-300">${{ item.product.price.toFixed(2) }}</p>
        </div>
        <input
          type="number"
          min="1"
          :value="item.quantity"
          class="w-20 rounded-lg border border-slate-700 bg-slate-950 px-2 py-1"
          @change="updateQty(item.id, $event)"
        />
        <button class="rounded-lg border border-rose-500 px-3 py-2 text-rose-300 hover:bg-rose-500/20" @click="cart.removeItem(item.id)">
          Remove
        </button>
      </article>

      <div class="rounded-2xl border border-slate-800 bg-slate-900/70 p-6">
        <p class="text-lg text-slate-200">Subtotal: <span class="font-semibold text-white">${{ cart.subtotal.toFixed(2) }}</span></p>
        <router-link
          to="/checkout"
          class="mt-4 inline-block rounded-xl bg-brand-600 px-5 py-3 font-semibold text-white hover:bg-brand-500"
        >
          Proceed to Checkout
        </router-link>
      </div>
    </div>
  </section>
</template>

<script setup>
import { onMounted } from "vue";
import { useCartStore } from "../stores/cart";

const cart = useCartStore();

function updateQty(id, event) {
  const quantity = Number(event.target.value);
  if (quantity > 0) {
    cart.updateQuantity(id, quantity);
  }
}

onMounted(cart.fetchCart);
</script>
