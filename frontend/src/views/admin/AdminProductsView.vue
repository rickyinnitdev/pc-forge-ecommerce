<template>
  <section>
    <AdminNav />
    <div class="mb-6 flex items-center justify-between">
      <h1 class="text-4xl font-bold text-white">Product Management</h1>
      <button class="rounded-xl bg-brand-600 px-4 py-2 text-white" @click="openCreate">Add Product</button>
    </div>

    <div class="overflow-x-auto rounded-2xl border border-slate-800 bg-slate-900/70">
      <table class="min-w-full text-left text-sm text-slate-300">
        <thead class="border-b border-slate-800 text-slate-200">
          <tr>
            <th class="px-4 py-3">Name</th>
            <th class="px-4 py-3">Category</th>
            <th class="px-4 py-3">Price</th>
            <th class="px-4 py-3">Stock</th>
            <th class="px-4 py-3">Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="product in products" :key="product.id" class="border-b border-slate-800/50">
            <td class="px-4 py-3">{{ product.name }}</td>
            <td class="px-4 py-3">{{ product.category }}</td>
            <td class="px-4 py-3">${{ product.price.toFixed(2) }}</td>
            <td class="px-4 py-3">{{ product.stock_quantity }}</td>
            <td class="px-4 py-3">
              <button class="mr-2 rounded border border-brand-500 px-3 py-1" @click="openEdit(product)">Edit</button>
              <button class="rounded border border-rose-500 px-3 py-1 text-rose-300" @click="removeProduct(product.id)">Delete</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <div v-if="showForm" class="mt-6 rounded-2xl border border-slate-800 bg-slate-900/70 p-5">
      <h2 class="mb-4 text-2xl font-semibold text-white">{{ editingId ? "Edit Product" : "Add Product" }}</h2>
      <form class="grid gap-3 md:grid-cols-2" @submit.prevent="submitForm">
        <input v-model="form.name" required placeholder="Product Name" class="input" />
        <input v-model="form.category" required placeholder="Category" class="input" />
        <input v-model.number="form.price" required type="number" step="0.01" placeholder="Price" class="input" />
        <input v-model.number="form.stock_quantity" required type="number" min="0" placeholder="Stock" class="input" />
        <input v-model="form.image_url" required placeholder="Unsplash image URL" class="input md:col-span-2" />
        <textarea v-model="form.description" required rows="3" placeholder="Description" class="input md:col-span-2"></textarea>
        <div class="md:col-span-2">
          <button class="rounded-xl bg-brand-600 px-4 py-2 text-white" type="submit">Save</button>
          <button class="ml-2 rounded-xl border border-slate-600 px-4 py-2 text-slate-300" type="button" @click="cancel">Cancel</button>
        </div>
      </form>
    </div>
  </section>
</template>

<script setup>
import { reactive, ref } from "vue";
import AdminNav from "../../components/AdminNav.vue";
import api from "../../services/api";

const products = ref([]);
const showForm = ref(false);
const editingId = ref(null);

const emptyForm = () => ({
  name: "",
  category: "",
  price: 0,
  description: "",
  image_url: "",
  stock_quantity: 0,
});

const form = reactive(emptyForm());

async function fetchProducts() {
  const { data } = await api.get("/products");
  products.value = data;
}

function openCreate() {
  Object.assign(form, emptyForm());
  editingId.value = null;
  showForm.value = true;
}

function openEdit(product) {
  Object.assign(form, product);
  editingId.value = product.id;
  showForm.value = true;
}

async function submitForm() {
  if (editingId.value) {
    await api.put(`/products/${editingId.value}`, form);
  } else {
    await api.post("/products", form);
  }
  await fetchProducts();
  cancel();
}

async function removeProduct(id) {
  await api.delete(`/products/${id}`);
  await fetchProducts();
}

function cancel() {
  showForm.value = false;
  editingId.value = null;
}

fetchProducts();
</script>

<style scoped>
.input {
  @apply w-full rounded-lg border border-slate-700 bg-slate-950 px-3 py-2 text-slate-100 focus:border-brand-500 focus:outline-none;
}
</style>
