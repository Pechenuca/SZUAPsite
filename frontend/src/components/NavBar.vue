<template>
  <div class="navbar">
    <div class="navbar-elments">
      <img :src="logo">
      <div class="links">
        <ul>
          
          <li v-on:click="updateSelectedDivId('about')">
            <router-link to="/">О нас</router-link>
          </li>

          <li v-on:click="updateSelectedDivId('services')">
            <router-link to="/">Услуги</router-link>
          </li>

          <li v-on:click="updateSelectedDivId('news')">
            <router-link to="/">Новости</router-link>
          </li>
          
          <li v-on:click="updateSelectedDivId('audit')">
            <router-link to="/">Аудиторские<br>Отчеты</router-link>
          </li>
          
          <li v-on:click="updateSelectedDivId('contacts')">
            <router-link to="/">Контакты</router-link>
          </li>
          
          <li><SearchBox /></li>
        
        </ul>
      </div>
    </div>
    <div class="navbar-mobile">
      <img :src="logo" class="navbar-image-mobile" >
      <h1>test</h1>
    </div>
  </div>
</template>

<script>
  import logo from "@/assets/logo.png"
  import SearchBox from "@/components/SearchBox";
  export default {
    name: "NavBar",
    components: {SearchBox},
    setup() {
      return {
        logo,
      };
    },
    methods: {
        updateSelectedDivId(id) {
          this.$store.commit("currentDiv", id)  
      }
    }
  }
</script>

<style scoped>
    .navbar {
        flex: 0 0 auto;
        width: 259px;
        height: 100%;
        background-color: white;
        box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
    }

    .navbar-elments {
        margin-top: 100px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        width: 100%;

    }

    .navbar-elments img {
        width: 180px;
        margin-bottom: 30px;
    }

    .links {
        display: flex;
        flex-direction: column;
        width: 100%;
        align-items: center;
        justify-content: center;
    }

    .links ul {
        list-style: none;
        padding: 0;
    }

    .links li {
        margin-bottom: 25px;
        text-decoration: none;
        color: black;
        font-style: normal;
        font-weight: 300;
        font-size: 24px;
        line-height: 41px;
        text-align: left;
        cursor: pointer;
    }

    .links li > a {
        text-decoration: none;
        color: black;
    }

    .navbar-mobile {
      display: none;
    }

    .navbar-component {
      height: 100%;
    }

    @media (max-width: 1191px) {
      .navbar {
        display: block;
        width: 100%;
        height: 60px;
      }
      
      .navbar-elments {
        display: none;
      }

      .navbar-mobile {
        display: flex;
        justify-content: space-between;
        align-items: center;
        flex-direction: row;
        height: 100%;
        width: 90%;
        margin: auto;
      }

      .navbar-image-mobile {
        width: 180px;
        height: 35px;
      }

    }
</style>