import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import ProductsView from "../views/ProductsView.vue";
import ProductDetailView from "../views/ProductDetailView.vue";
import CartView from "../views/CartView.vue";
import CheckoutView from "../views/CheckoutView.vue";
import OrderConfirmationView from "../views/OrderConfirmationView.vue";
import AdminLoginView from "../views/admin/AdminLoginView.vue";
import AdminDashboardView from "../views/admin/AdminDashboardView.vue";
import AdminProductsView from "../views/admin/AdminProductsView.vue";
import AdminOrdersView from "../views/admin/AdminOrdersView.vue";
import AdminInventoryView from "../views/admin/AdminInventoryView.vue";
import { useAdminStore } from "../stores/admin";

const routes = [
  { path: "/", name: "home", component: HomeView },
  { path: "/products", name: "products", component: ProductsView },
  { path: "/products/:id", name: "product-detail", component: ProductDetailView },
  { path: "/cart", name: "cart", component: CartView },
  { path: "/checkout", name: "checkout", component: CheckoutView },
  { path: "/order-confirmation/:id", name: "order-confirmation", component: OrderConfirmationView },
  { path: "/admin/login", name: "admin-login", component: AdminLoginView },
  { path: "/admin/dashboard", name: "admin-dashboard", component: AdminDashboardView, meta: { requiresAuth: true } },
  { path: "/admin/products", name: "admin-products", component: AdminProductsView, meta: { requiresAuth: true } },
  { path: "/admin/orders", name: "admin-orders", component: AdminOrdersView, meta: { requiresAuth: true } },
  { path: "/admin/inventory", name: "admin-inventory", component: AdminInventoryView, meta: { requiresAuth: true } },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach((to, _, next) => {
  const adminStore = useAdminStore();
  if (to.meta.requiresAuth && !adminStore.isAuthenticated) {
    next({ name: "admin-login" });
    return;
  }
  next();
});

export default router;
