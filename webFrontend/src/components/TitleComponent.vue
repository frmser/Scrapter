<template>
  <div class="flex flex-col items-center justify-center text-center min-h-fit">
    <h1
      :class="size === 'small' ? 'text-6xl' : 'text-6xl sm:text-8xl'"
      class="font-bold"
    >
      <slot name="title"></slot>
    </h1>
    <p class="text-gray text-2xl font-bold w-2/4">
      <slot name="subtitle"></slot>
    </p>
  </div>
</template>

<script setup lang="ts">
defineProps<{
  size: "large" | "small";
}>();
</script>
