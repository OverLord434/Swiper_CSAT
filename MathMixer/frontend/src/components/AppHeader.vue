<template>
  <header class="shadow-sm min-h-[137px]">
    <div class="max-w-[1360px] mx-auto px-[10px]">
      <div class="flex justify-between items-center h-[137px] flex-wrap">
        <div class="flex-shrink-0 order-1 logo">
          <a href="#">
            <img src="../assets/images/logo.svg" alt="Логотип сайта" />
          </a>
        </div>

        <nav class="w-full md:w-auto order-2">
          <ul class="flex justify-between items-center menu-list w-full md:w-[525px]">
            <li><a href="#">Категории</a></li>
            <li><a href="#">Лидеры</a></li>
            <li><a href="#">Добавить</a></li>
          </ul>
        </nav>

        <div v-if="!isSearchHidden" 
          class="flex justify-between items-center w-full md:w-[532px] bg-[#D9D9D9] rounded-[5px] px-[7px] mt-2 md:mt-0 order-3"
        >
          <input
            type="text"
            class="font-normal placeholder-black placeholder-opacity-50 w-full bg-transparent outline-none pr-[10px]"
            placeholder="Поиск по вопросам"
          />
          <div class="search-icon opacity-60">
            <img
              src="../assets/images/search-icon.svg"
              alt="Иконка поиска"
              class="w-6 h-6"
            />
          </div>
        </div>

        <div class="flex-shrink-0 order-4 profile">
          <router-link to="/enter">
            <img src="../assets/images/profile-icon.svg" alt="Иконка профиля" />
          </router-link>
        </div>
      </div>
    </div>
  </header>
</template>

<script>
export default {
  name: "AppHeader",
  computed: {
    isSearchHidden() {
      return this.$route.path === '/product';
    }
  }
};
</script>

<style>
header {
  font-size: 25px;
}
.menu-list {
  flex-wrap: wrap; 
}

.menu-list a {
  opacity: 0.6;
  transition: all 0.3s;
}

.menu-list a:hover {
  opacity: 1;
}

@media (max-width: 1340px) {
  header {
    font-size: 23px;
  }
  .search-icon {
    padding-left: 5px;
  }
}

@media (max-width: 768px){
  header {
    padding-bottom: 10px;
    font-size: 19px;
  }
  .profile {
    order: 1;
  }

  .menu-list {
    justify-content: space-evenly;
  }
}

@media (max-width: 360px) {
  header {
    font-size: 15px; 
  }
  
  .logo {
    width: 90px;
  }
  .profile {
    width: 25px;
  }
}
</style>
