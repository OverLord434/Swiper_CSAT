<template>
  <header class="text-[25px] shadow-sm">
    <div class="max-w-[1360px] mx-auto px-[10px]">
      <div class="flex justify-between items-center h-[137px]">
        <div>
          <a href="#">
            <img src="../assets/images/logo.svg" alt="Логотип сайта" />
          </a>
        </div>

        <nav class="w-[525px]">
          <ul class="flex justify-between items-center max-w-[525px] menu-list">
            <li><a href="#">Категории</a></li>
            <li><a href="#">Лидеры</a></li>
            <li><a href="#">Добавить</a></li>
          </ul>
        </nav>

        <div
          class="flex justify-between items-center w-[532px] bg-[#D9D9D9] rounded-[5px] px-[7px]"
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

        <div>
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
};
</script>

<style>
.menu-list a {
  opacity: 0.6;
  transition: all 0.3s;
}

.menu-list a:hover {
  opacity: 1;
}
</style>
