<template>
  <div>
    <section class="bg-[url('../assets/images/triangle-black.png')] bg-cover bg-center min-h-[625px] py-12">
      <div class="max-w-[1200px] mx-auto px-4">
        <div class="flex flex-col md:flex-row justify-between items-center mb-12">
          <div class="flex flex-col items-center w-full md:w-[30%] bg-gray-100 p-5 rounded-lg mb-6 md:mb-0">
            <img src="@/assets/images/avatar.jpg" alt="Avatar" id="edit-img"
            class="rounded-full w-32 h-32 mb-4 border-4 border-yellow-400 transition-transform transform hover:scale-110" />
            <h2 class="text-[32px] font-semibold mb-[10px]">{{ user.username }}</h2>
            <p class="text-[14px] text-gray-600">Зарегистрирован {{ formattedDate(user.date_joined) }}</p>
            <div class="flex items-center space-x-2 mt-2">
              <div class="w-3 h-3 rounded-full" :class="{ 'bg-green-500': !isOnline }"></div>
              <p class="text-[19px] font-bold text-gray-600">Онлайн</p>
            </div>
            <p class="text-[20px] font-light text-gray-600 mb-[30px]">{{ user.email }}</p>
            <div class="flex items-center gap-1 mb-5">
              <span class="text-lg font-semibold">2500</span>
              <img class="h-7 w-7" src="../assets/images/star.svg" alt="Иконка звёздочки" />
            </div>
            <button @click="openModal"
              class="border-4 border-yellow-400 bg-transparent rounded-full w-[180px] md:w-[195px] py-3 text-yellow-400 hover:bg-yellow-400 hover:text-white transition duration-500">
              Редактировать
            </button>
            <div class="flex justify-center mt-5">
              <button
                @click="logout"
                class="border-4 border-red-500 bg-transparent rounded-full w-[180px] md:w-[195px] py-3 text-red-500 hover:bg-red-500 hover:text-white transition duration-500">
                Выйти из аккаунта
              </button>
            </div>
          </div>

          <div class="w-full md:w-2/3 bg-gray-100 p-5 md:p-7 rounded-lg">
            <h3 class="text-2xl font-semibold mb-6">История отзывов</h3>

            <div class="max-h-[400px] overflow-y-auto pr-2">
              <a href="#" class="block bg-white p-5 mb-5 rounded-lg shadow-md hover:bg-gray-50 transition">
                <p class="text-lg font-medium">Отзыв о ноутбуке ASUS ROG Strix</p>
                <p class="text-md text-gray-600">Очень доволен качеством. Работает отлично.</p>
                <p class="text-sm text-gray-400 mt-2">2024-09-28</p>
              </a>
              <a href="#" class="block bg-white p-5 mb-5 rounded-lg shadow-md hover:bg-gray-50 transition">
                <p class="text-lg font-medium">Отзыв о мониторе Samsung</p>
                <p class="text-md text-gray-600">Удобный и качественный монитор, рекомендую!</p>
                <p class="text-sm text-gray-400 mt-2">2024-09-25</p>
              </a>
              <a href="#" class="block bg-white p-5 mb-5 rounded-lg shadow-md hover:bg-gray-50 transition">
                <p class="text-lg font-medium">Отзыв о видеокарте NVIDIA RTX 3080</p>
                <p class="text-md text-gray-600">Отличная производительность, но шумный кулер.</p>
                <p class="text-sm text-gray-400 mt-2">2024-09-20</p>
              </a>
              <a href="#" class="block bg-white p-5 mb-5 rounded-lg shadow-md hover:bg-gray-50 transition">
                <p class="text-lg font-medium">Отзыв о клавиатуре Logitech G Pro</p>
                <p class="text-md text-gray-600">Отличная клавиатура для игр.</p>
                <p class="text-sm text-gray-400 mt-2">2024-09-15</p>
              </a>
            </div>
          </div>
        </div>

<!-- Модальное окно -->
        <div v-if="isModalOpen" class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-70 z-50">
          <div class="bg-white rounded-lg p-5 md:p-8 w-11/12 md:w-1/3 shadow-2xl transition-transform transform scale-95 hover:scale-100">
            <h3 class="text-xl font-semibold text-center text-gray-800 mb-4">Редактировать профиль</h3>
            <div class="flex flex-col items-center mb-4">
              <img src="../assets/images/avatar.jpg" alt="Avatar"
                class="rounded-full w-32 h-32 mb-4 border-4 border-yellow-400 transition-transform transform hover:scale-110" />
              <label for="avatar"
                class="cursor-pointer bg-yellow-400 text-white px-4 py-2 rounded-lg shadow-md hover:bg-yellow-500 transition duration-300">Изменить аватарку</label>
              <input id="avatar" type="file" class="hidden" @change="previewAvatar" />
            </div>
            <form @submit.prevent="updateProfile">
              <div class="mb-4">
                <label for="username" class="block text-sm font-medium text-gray-700">Никнейм</label>
                <input v-model="form.username" type="text" class="border rounded-lg w-full p-2" placeholder="Введите новый никнейм" />
              </div>
              <div class="mb-4">
                <label for="email" class="block text-sm font-medium text-gray-700">Email</label>
                <input v-model="form.email" type="email" class="border rounded-lg w-full p-2" placeholder="Введите новый email" />
              </div>
              <div class="mb-4">
                <label for="password" class="block text-sm font-medium text-gray-700">Пароль</label>
                <input v-model="form.password" type="password" class="border rounded-lg w-full p-2" placeholder="Введите новый пароль" />
              </div>
              <div class="mb-4">
                <label for="confirmPassword" class="block text-sm font-medium text-gray-700">Подтверждение пароля</label>
                <input v-model="form.password2" type="password" class="border rounded-lg w-full p-2" placeholder="Подтвердите новый пароль" />
              </div>
              <div class="flex justify-end">
                <button type="button" @click="closeModal" class="mr-4 text-gray-500 hover:text-gray-700">Отмена</button>
                <button type="submit" class="bg-yellow-400 text-white rounded-lg px-4 py-2">Сохранить изменения</button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      user: {},
      reviews: [], // добавляем данные отзывов
      isModalOpen: false,
      avatarPreview: '',
      form: {
        username: '',
        email: '',
        password: '',
        password2: ''
      }
    };
  },
  methods: {
    openModal() {
      this.isModalOpen = true;
    },
    closeModal() {
      this.isModalOpen = false;
    },
    previewAvatar(event) {
      const file = event.target.files[0];
      if (file) {
        const reader = new FileReader();
        reader.onload = () => {
          this.avatarPreview = reader.result;
        };
        reader.readAsDataURL(file);
      }
    },
  updateProfile() {
  axios.put('http://127.0.0.1:8000/auth/user/update', this.form, {
    headers: {
      'Authorization': `Bearer ${localStorage.getItem('token')}`
    }
  })
  .then(response => {
    alert(response.data.message);
    this.closeModal();
  })
  .catch(error => {
    console.log(error.response.data);
    this.closeModal();
  });
},
    logout() {
      localStorage.removeItem('token');
      this.$router.push('/');
    },
    async getUserDetails() {
      try {
        const response = await axios.get('http://127.0.0.1:8000/auth/profile/date', {
          headers: {
            'Authorization': `Bearer ${localStorage.getItem('token')}`
          }
        });
        this.user = response.data;
      } catch (error) {
        console.error("Error fetching user details:", error);
      }
    },
    formattedDate(dateString) {
      const options = { year: 'numeric', month: '2-digit', day: '2-digit' };
      return new Date(dateString).toLocaleDateString('ru-RU', options);
    }
  },
  mounted() {
    this.getUserDetails();
  }
}
</script>