<template>
    <div class="wrapper">
      <NavBar />
      <MainPage />
    </div>
</template>

<script>
  import MainPage from "@/views/MainPage.vue";
  import NavBar from "@/components/NavBar.vue";
  export default {
    components: {NavBar, MainPage}
  }

</script>

<style>

  body, html {
    padding: 0;
    margin: 0;
    width: 100%;
    background: white;
  }

  #app {
    margin: 0;
  }

  .wrapper {
      display: flex;
      height: 100vh;
  }
</style>
