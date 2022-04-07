<template>
    <div class="wrapper">
      <NavBar />
      <router-view />
    </div>
</template>

<script>
  import NavBar from "@/components/NavBar.vue";

  export default {
    components: {NavBar},
  }

</script>

<style>

  body, html {
    padding: 0;
    margin: 0;
    width: 100%;
    background: white;
    overflow-x: hidden;
  }

  #app {
    margin: 0;
  }

  .wrapper {
      display: flex;
      height: 100vh;
  }

  .main-block {
    padding: 10px;
    flex: 1 1 auto;
    overflow: auto;
  }

  @font-face {
    font-family: "AlkesLight";
    src: local("AlkesLight"), url(./fonts/AlkesLight.TTF) format("truetype");
  }

  h1, h2, h3, h4, h5, h6, p, a {
    font-family: AlkesLight
  }

  @media (max-width: 1191px) {
      .wrapper {
        display: block;
      }
    }

</style>
