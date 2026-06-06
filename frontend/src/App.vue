<template>
  <div class="min-h-screen">
    <SiteHeader />
    <main class="mx-auto max-w-7xl px-4 py-8 sm:px-6 lg:px-8">
      <router-view />
    </main>
  </div>
</template>

<script setup>
import SiteHeader from "./components/SiteHeader.vue";
</script>
