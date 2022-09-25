<template>
  <div>
    <video autoplay id="videoPlayer" ref="videoPlayer" v-show="loaded" class="h-full rounded border-bglightest border-2"></video>
    <div v-show="!loaded" class="text-gray flex flex-col justify-center h-full">
      <p>Please allow the use of your camera</p>
      <br>
      <Spinner></Spinner>
    </div>
  </div>
</template>

<script lang="ts" setup>
import {onBeforeUnmount, onMounted, ref} from "vue";
import Spinner from "./Spinner.vue";


const videoPlayer = ref<HTMLVideoElement>();
const loaded = ref(false);


let device: MediaStream | null = null;

onMounted(async () => {
  while (!loaded.value) {
    try {
      await loadCamera();
    } catch (e) {
      console.error(`error loading camera: ${e}`);
    }
  }
});

onBeforeUnmount(() => {
  device?.getTracks().forEach(t => t.stop());
  loaded.value = false;
});

async function loadCamera() {
  loaded.value = false;

  device = await navigator.mediaDevices.getUserMedia({
    audio: false,
    video: true
  });

  videoPlayer.value!.srcObject = device;

  await new Promise(r => setTimeout(r, 500));
  loaded.value = true;
}

</script>

<style scoped>

</style>
