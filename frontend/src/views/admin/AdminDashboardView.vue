<template>
  <section>
    <AdminNav />
    <h1 class="mb-6 text-4xl font-bold text-white">Admin Dashboard</h1>

    <div class="grid gap-4 md:grid-cols-4">
      <div class="card">Total Sales<br /><span class="value">${{ metrics.total_sales?.toFixed(2) || "0.00" }}</span></div>
      <div class="card">Orders<br /><span class="value">{{ metrics.total_orders || 0 }}</span></div>
      <div class="card">Products<br /><span class="value">{{ metrics.total_products || 0 }}</span></div>
      <div class="card">Low Stock<br /><span class="value">{{ metrics.low_stock_count || 0 }}</span></div>
    </div>

    <div class="mt-8 rounded-2xl border border-slate-800 bg-slate-900/70 p-5">
      <h2 class="mb-3 text-2xl font-semibold text-white">Sales Snapshot</h2>
      <canvas ref="salesChart"></canvas>
    </div>
  </section>
</template>

<script setup>
import { Chart, BarController, BarElement, CategoryScale, LinearScale, Tooltip, Legend } from "chart.js";
import { onMounted, ref } from "vue";
import AdminNav from "../../components/AdminNav.vue";
import api from "../../services/api";

Chart.register(BarController, BarElement, CategoryScale, LinearScale, Tooltip, Legend);

const metrics = ref({});
const salesChart = ref(null);

async function loadMetrics() {
  const { data } = await api.get("/admin/dashboard");
  metrics.value = data;
}

function renderChart() {
  if (!salesChart.value) return;
  new Chart(salesChart.value, {
    type: "bar",
    data: {
      labels: ["Sales", "Orders", "Products", "Low Stock"],
      datasets: [
        {
          label: "Store Overview",
          data: [
            metrics.value.total_sales || 0,
            metrics.value.total_orders || 0,
            metrics.value.total_products || 0,
            metrics.value.low_stock_count || 0,
          ],
          backgroundColor: ["#4f46e5", "#0ea5e9", "#22c55e", "#f97316"],
        },
      ],
    },
    options: {
      responsive: true,
      plugins: {
        legend: { labels: { color: "#e2e8f0" } },
      },
      scales: {
        x: { ticks: { color: "#94a3b8" } },
        y: { ticks: { color: "#94a3b8" } },
      },
    },
  });
}

onMounted(async () => {
  await loadMetrics();
  renderChart();
});
</script>

<style scoped>
.card {
  @apply rounded-2xl border border-slate-800 bg-slate-900/70 p-4 text-slate-300;
}

.value {
  @apply text-3xl font-bold text-white;
}
</style>
