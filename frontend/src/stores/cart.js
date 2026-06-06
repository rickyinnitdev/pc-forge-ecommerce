import { defineStore } from "pinia";
import api from "../services/api";

function getSessionId() {
  let id = localStorage.getItem("session_id");
  if (!id) {
    id = crypto.randomUUID();
    localStorage.setItem("session_id", id);
  }
  return id;
}

export const useCartStore = defineStore("cart", {
  state: () => ({
    sessionId: getSessionId(),
    items: [],
    loading: false,
  }),
  getters: {
    totalItems: (state) => state.items.reduce((sum, item) => sum + item.quantity, 0),
    subtotal: (state) =>
      state.items.reduce((sum, item) => sum + item.product.price * item.quantity, 0),
  },
  actions: {
    async fetchCart() {
      this.loading = true;
      try {
        const { data } = await api.get(`/cart/${this.sessionId}`);
        this.items = data;
      } finally {
        this.loading = false;
      }
    },
    async addToCart(productId, quantity = 1) {
      await api.post(`/cart?session_id=${this.sessionId}`, { product_id: productId, quantity });
      await this.fetchCart();
    },
    async updateQuantity(cartItemId, quantity) {
      await api.put(`/cart/${cartItemId}`, { quantity });
      await this.fetchCart();
    },
    async removeItem(cartItemId) {
      await api.delete(`/cart/${cartItemId}`);
      await this.fetchCart();
    },
    async clearAfterCheckout() {
      this.items = [];
    },
  },
});
