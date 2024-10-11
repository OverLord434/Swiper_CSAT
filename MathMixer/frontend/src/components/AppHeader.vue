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
          <ul v-show="isSuperUser" class="flex justify-end items-center menu-list w-full md:w-[525px] gap-[50px] menu-list">
            <li>
              <a href="#" @click.prevent="toggleDropdown">Добавить</a>
              <div v-if="isDropdownVisible" class="absolute bg-white border-[1px] shadow-md z-0 px-4 py-2 w-36 rounded-md" id="dropdown">
                <li><a href="#" class="text-[20px]" @click.prevent="addLinkClickHandler">Товары</a></li>
                <li><a href="#" class="text-[20px]" @click.prevent="addLinkClickHandler">Услуги</a></li>
              </div>
            </li>
          </ul>
        </nav>

        <div class="flex justify-between items-center w-full md:w-[532px] bg-[#D9D9D9] rounded-[5px] px-[7px] mt-2 md:mt-0 order-3">
          <input  v-model="searchQuery" type="text" class="font-normal placeholder-black placeholder-opacity-50 w-full bg-transparent outline-none pr-[10px]" placeholder="Поиск по вопросам"/>
          <button @click="search">
            <img src="../assets/images/search-icon.svg" alt="Иконка поиска" class="w-6 h-6" />
          </button>
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
import axios from 'axios';

export default {
  data() {
    return {
      user: {
        is_superuser: false,
      },
      isSuperUser: false,
      isDropdownVisible: false,
      searchQuery: '',
    }
  },
  methods:{
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
    },

    toggleDropdown(){
      this.isDropdownVisible = !this.isDropdownVisible;
    },
    addLinkClickHandler(){
      document.getElementById('model').classList.remove('hidden');
    },
    search() {
      this.$router.push({ name: 'ProductCardsPage', query: { query: this.searchQuery } });
    },
  },
  mounted() {
    this.getUserDetails();
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

@media (max-width: 410px){
  .menu-list{
    gap: 10px;
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

  .menu-list{
    gap: 10px;
  }
}
</style>
