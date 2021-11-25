<template>
    <div class="navbar">
        <div class="navbar-elments">
            <img :src="logo">
            <div class="links">
                <ul>
                    <li><a v-on:click="updateSelectedDivId('about')" >О нас</a></li>
                    <li><a v-on:click="updateSelectedDivId('services')" >Услуги</a></li>
                    <li><a v-on:click="updateSelectedDivId('news')" >Новости</a></li>
                    <li><a v-on:click="updateSelectedDivId('audit')" >Аудит. отчеты</a></li>
                    <li><a v-on:click="updateSelectedDivId('contacts')" >Контакты</a></li>
                    <li><SearchBox /></li>
                </ul>
            </div>
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
</style>