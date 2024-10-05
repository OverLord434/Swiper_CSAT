<template>
  <section class="h-screen flex items-center justify-center bg-gray-200">
    <div class="w-full max-w-3xl lg:max-w-7xl flex flex-col lg:flex-row items-center justify-center space-y-6 lg:space-y-0 lg:space-x-6">
      <div class="w-full lg:w-1/2 p-8 bg-white rounded-xl shadow-xl">
        <h2 class="text-center text-3xl font-bold mb-8">Регистрация пользователей</h2>
        <form @submit.prevent="register">
          <div class="mb-6">
            <label for="username" class="block text-lg font-medium mb-3">Ваш никнейм</label>
            <input
              type="text"
              id="username"
              v-model="username"
              class="w-full px-5 py-4 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-yellow-400 text-lg"
              placeholder="Введите ваш никнейм"
              required
            />
          </div>
          <div class="mb-6">
            <label for="email" class="block text-lg font-medium mb-3">Ваш Email</label>
            <input
              type="email"
              id="email"
              v-model="email"
              class="w-full px-5 py-4 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-yellow-400 text-lg"
              placeholder="Введите ваш email"
              required
            />
          </div>
          <div class="mb-6">
            <label for="password" class="block text-lg font-medium mb-3">Пароль</label>
            <input
              type="password"
              id="password"
              v-model="password"
              class="w-full px-5 py-4 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-yellow-400 text-lg"
              placeholder="Введите пароль"
              required
            />
          </div>
          <div class="mb-6">
            <label for="password2" class="block text-lg font-medium mb-3">Повторите пароль</label>
            <input
              type="password"
              id="password2"
              v-model="password2"
              class="w-full px-5 py-4 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-yellow-400 text-lg"
              placeholder="Повторите пароль"
              required
            />
          </div>
          <div class="flex justify-center">
            <button
              type="submit"
              class="bg-yellow-400 hover:bg-yellow-500 text-black font-semibold py-3 px-12 rounded-lg text-lg transition duration-300"
            >
              Зарегистрироваться
            </button>
          </div>
        </form>
        <p v-if="error">{{ error }}</p>
      </div>
      <div class="hidden lg:block lg:w-1/2">
        <img src="../assets/images/regenter-bg.png" class="w-full h-auto rounded-xl" alt="image-bg" />
      </div>
    </div>
  </section>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      username: '',
      email: '',
      password: '',
      password2: '',
      error: '',
    };
  },
  methods: {
    async register() {
      try {
        // Сначала пытаемся зарегистрироваться
        await axios.post('http://localhost:8000/auth/register/', {
          username: this.username,
          email: this.email,
          password: this.password,
          password2: this.password2,
        });

        // Если регистрация успешна, сразу авторизуемся
        const loginResponse = await axios.post('http://localhost:8000/auth/login/', {
          username: this.username,
          password: this.password,
        });

        // После успешного логина сохраняем токен и перенаправляем на главную страницу
        localStorage.setItem('token', loginResponse.data.token.access); // Сохранение токена
        this.$router.push('/'); // Перенаправление на главную страницу
      } catch (error) {
        // Обработка ошибок
        if (error.response) {
          this.error = error.response.data;
        } else {
          this.error = 'Произошла ошибка. Попробуйте еще раз.';
        }
      }
    },
  },
};
</script>