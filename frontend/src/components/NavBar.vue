<template>
  <div id="nvb" class="navbar">
    <div class="navbar-elments">
      <img :src="logo" v-on:click="redirect">
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
      <img :src="logo" class="navbar-image-mobile" v-on:click="redirect">
      <div id="nvb-hamburger" class="navbar-hamburger" v-on:click="openMobileMenu()">
        <span></span>
        <span></span>
        <span></span>
      </div>
    </div>
    <div id="nvb-menu" class="navbar-mobile-menu">
      <div class="links">
        <ul>
          
          <li v-on:click="updateSelectedDivId('about');openMobileMenu();">
            <router-link to="/">О нас</router-link>
          </li>

          <li v-on:click="updateSelectedDivId('services');openMobileMenu();">
            <router-link to="/">Услуги</router-link>
          </li>

          <li v-on:click="updateSelectedDivId('news');openMobileMenu();">
            <router-link to="/">Новости</router-link>
          </li>
          
          <li v-on:click="updateSelectedDivId('audit');openMobileMenu();">
            <router-link to="/">Аудиторские<br>Отчеты</router-link>
          </li>
          
          <li v-on:click="updateSelectedDivId('contacts');openMobileMenu();">
            <router-link to="/">Контакты</router-link>
          </li>
          
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
      let mobileMenuIsOpen = false
      return {
        logo,
        mobileMenuIsOpen
      };
    },
    methods: {
      updateSelectedDivId(id) {
        this.$store.commit("currentDiv", id)  
      },
      redirect() {
        this.$router.push('/');
      },
      openMobileMenu() {
        if (this.mobileMenuIsOpen) {
          document.getElementById("nvb-hamburger").classList.remove("open")
          document.getElementById("nvb").classList.remove("open")
          document.getElementById("nvb-menu").classList.remove("open")
          this.mobileMenuIsOpen = false
        } else {
          document.getElementById("nvb-hamburger").classList.add("open")
          document.getElementById("nvb").classList.add("open")
          document.getElementById("nvb-menu").classList.add("open")
          this.mobileMenuIsOpen = true
        }
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
        cursor: pointer;
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

    .navbar-mobile, .navbar-mobile-menu {
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
        transition: height 400ms;
      }

      .navbar.open {
        height: 510px;
      }

      .navbar-mobile-menu.open {
        display: flex;
        justify-content: center;
        flex-direction: column;
        justify-content: center;
      }
      
      .navbar-elments {
        display: none;
      }

      .navbar-mobile {
        display: flex;
        justify-content: space-between;
        align-items: center;
        flex-direction: row;
        height: 60px;
        width: 90%;
        margin: auto;
      }

      .navbar-image-mobile {
        width: 180px;
        height: 35px;
        cursor: pointer;
      }

      .navbar-hamburger {
        width: 45px;
        height: 45px;
        -webkit-transform: rotate(0deg);
        -moz-transform: rotate(0deg);
        -o-transform: rotate(0deg);
        transform: rotate(0deg);
        -webkit-transition: .5s ease-in-out;
        -moz-transition: .5s ease-in-out;
        -o-transition: .5s ease-in-out;
        transition: .5s ease-in-out;
        cursor: pointer;
      }

      .navbar-hamburger span {
        display: block;
        position: absolute;
        height: 9px;
        width: 100%;
        background: rgb(7, 191, 79);
        border-radius: 9px;
        opacity: 1;
        left: 0;
        -webkit-transform: rotate(0deg);
        -moz-transform: rotate(0deg);
        -o-transform: rotate(0deg);
        transform: rotate(0deg);
        -webkit-transition: .25s ease-in-out;
        -moz-transition: .25s ease-in-out;
        -o-transition: .25s ease-in-out;
        transition: .25s ease-in-out;
      }

      .navbar-hamburger span:nth-child(1) {
        top: 0px;
      }

      .navbar-hamburger span:nth-child(2) {
        top: 18px;
      }

      .navbar-hamburger span:nth-child(3) {
        top: 36px;
      }

      .navbar-hamburger.open span:nth-child(1) {
        top: 18px;
        -webkit-transform: rotate(135deg);
        -moz-transform: rotate(135deg);
        -o-transform: rotate(135deg);
        transform: rotate(135deg);
      }

      .navbar-hamburger.open span:nth-child(2) {
        opacity: 0;
        left: -60px;
      }

      .navbar-hamburger.open span:nth-child(3) {
        top: 18px;
        -webkit-transform: rotate(-135deg);
        -moz-transform: rotate(-135deg);
        -o-transform: rotate(-135deg);
        transform: rotate(-135deg);
      }

    }
</style>