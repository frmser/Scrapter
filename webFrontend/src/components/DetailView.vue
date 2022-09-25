<template>
  <div class="w-full h-full child:float-right">
    <div v-show="product == null" class="flex flex-col items-center text-gray w-full">
      <span class="material-symbols-outlined text-6xl text-red">warning</span>
      <p>
        No product detected. <br>
        Try a different angle
      </p>
    </div>
    <div v-if="product != null" class="flex w-full h-full px-4">
      <div>
        <span class="text-gray">Product Name</span>: {{ product.name }}
        <br>
        <span class="text-gray">Classification</span>: {{ product.productType }}
      </div>
      <div class="ml-auto bg-bglightest p-4 h-[180px] w-[180px] flex justify-center items-center rounded">
        <img alt="product image" v-if="product.image != null" :src="product.image" class="h-full">
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import Product from "../models/product";

defineProps<{
  product: Product | null
}>();
</script>

<style scoped>

</style>
