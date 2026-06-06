<template>
  <section>
    <AdminNav />
    <h1 class="mb-6 text-4xl font-bold text-white">Order Management</h1>

    <div class="space-y-4">
      <article v-for="order in orders" :key="order.id" class="rounded-2xl border border-slate-800 bg-slate-900/70 p-5">
        <div class="flex flex-col justify-between gap-4 md:flex-row">
          <div>
            <h2 class="text-xl font-semibold text-white">Order #{{ order.id }} - {{ order.customer_name }}</h2>
            <p class="text-sm text-slate-300">{{ order.customer_email }} | {{ order.city }} | ${{ order.total_amount.toFixed(2) }}</p>
          </div>
          <select v-model="order.status" class="rounded-lg border border-slate-700 bg-slate-950 px-3 py-2" @change="updateStatus(order)">
            <option value="pending">pending</option>
            <option value="processing">processing</option>
            <option value="shipped">shipped</option>
            <option value="delivered">delivered</option>
            <option value="cancelled">cancelled</option>
          </select>
        </div>
      </article>
    </div>
  </section>
</template>

<script setup>
import { ref } from "vue";
import AdminNav from "../../components/AdminNav.vue";
import api from "../../services/api";

const orders = ref([]);

async function fetchOrders() {
  const { data } = await api.get("/orders");
  orders.value = data;
}

async function updateStatus(order) {
  await api.put(`/orders/${order.id}/status`, { status: order.status });
}

fetchOrders();
</script>
