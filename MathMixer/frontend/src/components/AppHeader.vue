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
            <button
                @click="handleProfileClick"
                class="flex items-center p-2 bg-transparent hover:bg-gray-200 rounded transition duration-300 ease-in-out">
                <img src="../assets/images/profile-icon.svg" alt="Иконка профиля" class="h-6 w-6" />
            </button>
        </div>
      </div>
    </div>
  </header>
</template>

<script>
export default {
  name: 'AppHeader',
  props: {
    isAuthenticated: {
      type: Boolean,
      required: true
    }
  },
  methods: {
    handleProfileClick() {
      if (this.isAuthenticated) {
        this.$router.push({ name: 'ProfileUsers' }); // Переход на страницу профиля
      } else {
        this.$router.push({ name: 'Enter' }); // Переход на страницу авторизации
      }
    }
  }
}
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
