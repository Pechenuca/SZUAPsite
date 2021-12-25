import { createWebHistory, createRouter } from "vue-router";
import MainPage from "@/views/MainPage.vue";
import Content from "@/views/Content.vue";
import NewsDetail from "@/views/NewsDetail";

const routes = [
  {
    path: "/",
    name: "MainPage",
    component: MainPage,
  },
  {
    path: "/content/:type/:search?",
    name: "Content",
    component: Content,
  },
  {
    path: "/detail/:id",
    name: "NewsDetail",
    component: NewsDetail,
  }
];
  
const router = createRouter({
  history: createWebHistory(),
  routes,
});
  
export default router;