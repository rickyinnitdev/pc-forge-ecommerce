<template>
  <section>
    <AdminNav />
    <h1 class="mb-6 text-4xl font-bold text-white">Inventory Tracking</h1>

    <div class="overflow-x-auto rounded-2xl border border-slate-800 bg-slate-900/70">
      <table class="min-w-full text-left text-sm text-slate-300">
        <thead class="border-b border-slate-800 text-slate-200">
          <tr>
            <th class="px-4 py-3">Product</th>
            <th class="px-4 py-3">Category</th>
            <th class="px-4 py-3">Stock</th>
            <th class="px-4 py-3">Status</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="item in inventory" :key="item.id" class="border-b border-slate-800/50">
            <td class="px-4 py-3">{{ item.name }}</td>
            <td class="px-4 py-3">{{ item.category }}</td>
            <td class="px-4 py-3">{{ item.stock_quantity }}</td>
            <td class="px-4 py-3">
              <span :class="item.stock_quantity < 10 ? 'text-amber-300' : 'text-emerald-300'">
                {{ item.stock_quantity < 10 ? "Low" : "Healthy" }}
              </span>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </section>
</template>

<script setup>
import { ref } from "vue";
import AdminNav from "../../components/AdminNav.vue";
import api from "../../services/api";

const inventory = ref([]);

async function fetchInventory() {
  const { data } = await api.get("/admin/inventory");
  inventory.value = data;
}

fetchInventory();
</script>
