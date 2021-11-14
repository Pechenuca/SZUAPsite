<template>
    <div class="navbar">
        <div class="navbar-elments">
            <img :src="logo">
            <div class="links">
                <ul>
                    <li><a>О нас</a></li>
                    <li><a>Услуги</a></li>
                    <li><a>Контакты</a></li>
                    <li><a>Новости</a></li>
                    <li><SearchBox label="Найти"/></li>
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
        logo
      };
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
    }

    .links li > a {
        text-decoration: none;
        color: black;
    }
</style>