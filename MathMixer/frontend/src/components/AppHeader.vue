<template>
  <header class="text-[25px] shadow-sm">
    <div class="max-w-[1360px] mx-auto px-[10px]">
      <div  class="flex justify-between items-center h-[137px]">
        <div>
          <router-link to="/">
            <img src="../assets/images/logo.svg" alt="Логотип сайта" />
          </router-link>
        </div>

            <nav class="w-[525px]">
              <ul v-if="isSuperUser" class="flex justify-between items-center max-w-[525px] menu-list">
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
            <router-link to="/product/cards">
            <img src="../assets/images/search-icon.svg" alt="Иконка поиска" class="w-6 h-6" />
            </router-link>
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
import axios from 'axios';

export default {
  data() {
    return {
      user: {
        is_superuser: false,
        // другие поля, если нужно
      },
      isSuperUser: false
    }
  },
  methods: {
    async getUserDetails() {
      try {
        const response = await axios.get('http://127.0.0.1:8000/auth/appheader/user', {
          headers: {
            'Authorization': `Bearer ${localStorage.getItem('token')}`
          }
        });
        this.user = response.data;
        this.isSuperUser = this.user.is_superuser;
      } catch (error) {
        console.error("Error fetching user details:", error);
      }
    }
  },
  goToAbout() {
      this.$router.push('/about');
    },
  mounted() {
    this.getUserDetails();
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
