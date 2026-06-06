<template>
  <section class="mx-auto max-w-md rounded-2xl border border-slate-800 bg-slate-900/70 p-8">
    <h1 class="text-3xl font-bold text-white">Admin Login</h1>
    <p class="mt-2 text-sm text-slate-300">Use your admin credentials to manage products and orders.</p>

    <form class="mt-6 space-y-4" @submit.prevent="submitLogin">
      <input v-model="email" type="email" required placeholder="Admin Email" class="input" />
      <input v-model="password" type="password" required placeholder="Password" class="input" />
      <p v-if="error" class="text-sm text-rose-400">{{ error }}</p>
      <button type="submit" class="w-full rounded-xl bg-brand-600 px-4 py-3 font-semibold text-white hover:bg-brand-500">Login</button>
    </form>
  </section>
</template>

<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";
import { useAdminStore } from "../../stores/admin";

const admin = useAdminStore();
const router = useRouter();

const email = ref("admin@pcforge.com");
const password = ref("Admin@12345");
const error = ref("");

async function submitLogin() {
  error.value = "";
  try {
    await admin.login(email.value, password.value);
    router.push("/admin/dashboard");
  } catch {
    error.value = "Invalid credentials. Please try again.";
  }
}
</script>

<style scoped>
.input {
  @apply w-full rounded-lg border border-slate-700 bg-slate-950 px-3 py-2 text-slate-100 focus:border-brand-500 focus:outline-none;
}
</style>
