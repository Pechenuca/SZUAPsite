<template>
  <div class="services-block-wrapper">
    <TitleBlock label="Услуги компании" :pHref="href"  />
  </div>
</template>

<script>
  import TitleBlock from "@/components/MainPage/TitleBlock.vue";
  export default {
    name: "Services",
    components: {TitleBlock},
    
  }
</script>

<style>
  .services-block-wrapper {
    display: flex;
    flex-direction:column;
  }
</style>