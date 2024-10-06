<template>
  <section class="h-screen flex items-center justify-center bg-gray-200">
    <div
      class="w-full max-w-3xl lg:max-w-7xl flex flex-col lg:flex-row items-center justify-center space-y-6 lg:space-y-0 lg:space-x-6"
    >
      <div class="w-full lg:w-1/2 p-8 bg-white rounded-xl shadow-xl">
        <h2 class="text-center text-3xl font-bold mb-8">Вход</h2>
        <form @submit.prevent="login">
          <div class="mb-6">
            <label for="username" class="block text-lg font-medium mb-3"
              >Email</label
            >
            <input
              v-model="form.username"
              type="username"
              id="username"
              class="w-full px-5 py-4 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-yellow-400 text-lg"
              placeholder="Введите Email"
              required
            />
          </div>

          <div class="mb-6">
            <label for="password" class="block text-lg font-medium mb-3"
              >Пароль</label
            >
            <input
              v-model="form.password"
              type="password"
              id="password"
              class="w-full px-5 py-4 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-yellow-400 text-lg"
              placeholder="Введите пароль"
              required
            />
          </div>

          <div class="flex justify-between items-start">
            <div class="mb-6">
              <span class="text-[16px] mb-2 block">
                Еще не зарегистрированы?
              </span>
              <div class="flex flex-col mb-4">
                <router-link
                  to="/register/users"
                  class="text-[16px] text-blue-500 hover:underline mb-1"
                >
                  Регистрация для пользователей
                </router-link>
                <router-link
                  to="/register/agency"
                  class="text-[16px] text-blue-500 hover:underline"
                >
                  Регистрация для организации
                </router-link>
              </div>
            </div>

            <div class="flex justify-center mb-6">
              <a href="#" class="text-[16px] text-blue-500 hover:underline">
                Забыли пароль?
              </a>
            </div>
          </div>

          <div class="flex justify-center">
            <button
              type="submit"
              class="bg-yellow-400 hover:bg-yellow-500 text-black font-semibold py-3 px-12 rounded-lg text-lg transition duration-300"
            >
              Войти
            </button>
          </div>
        </form>
        {{ error }}
      </div>

      <div class="hidden lg:block lg:w-1/2">
        <img
          src="../assets/images/regenter-bg.png"
          class="w-170px h-auto rounded-xl"
          alt="image-bg"
        />
      </div>
    </div>
  </section>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      form: {
        username: '',
        password: ''
      },
      error: ''
    }
  },
  methods: {
    async login() {
      try {
        const response = await axios.post('http://127.0.0.1:8000/auth/enter/user', this.form)
        localStorage.setItem('token', response.data.token.access)
        this.$router.push('/')
      } catch (error) {
        this.error = error.response.data.message
      }
    }
  }
}
</script>
