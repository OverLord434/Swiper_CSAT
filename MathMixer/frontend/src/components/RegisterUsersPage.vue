<template>
  <section class="h-screen flex items-center justify-center bg-gray-200">
    <div
      class="w-full max-w-3xl lg:max-w-7xl flex flex-col lg:flex-row items-center justify-center space-y-6 lg:space-y-0 lg:space-x-6">
      <div class="w-full lg:w-1/2 p-8 bg-white rounded-xl shadow-xl">
        <h2 class="text-center text-3xl font-bold mb-8">Регистрация пользователей</h2>
        <form @submit.prevent="submitForm">
          <div class="mb-6">
            <label for="username" class="block text-lg font-medium mb-3"
              >Ваш никнейм</label
            >
            <input
              v-model="form.username"
              type="text"
              id="username"
              class="w-full px-5 py-4 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-yellow-400 text-lg"
              placeholder="Введите ваш никнейм"
              required
            />
          </div>

          <div class="mb-6">
            <label for="email" class="block text-lg font-medium mb-3"
              >Ваш Email</label
            >
            <input
              v-model="form.email"
              type="email"
              id="email"
              class="w-full px-5 py-4 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-yellow-400 text-lg"
              placeholder="Введите ваш email"
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

          <div class="mb-6">
            <label for="confirmPassword" class="block text-lg font-medium mb-3"
              >Повторите пароль</label
            >
            <input
              v-model="form.password2"
              type="password"
              id="confirmPassword"
              class="w-full px-5 py-4 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-yellow-400 text-lg"
              placeholder="Повторите пароль"
              required
            />
          </div>

          <div class="mb-6 flex items-center">
            <input
              v-model="acceptedTerms"
              type="checkbox"
              id="terms"
              class="w-4 h-4 border border-gray-300 rounded text-yellow-400 focus:outline-none focus:ring-2 focus:ring-yellow-400"
            />
            <label for="terms" class="ml-2 text-[16px] text-gray-700">
              Регистрируясь, вы принимаете
              <a href="#" class="text-blue-500 hover:underline"
                >Условия лицензионного договора</a
              >
            </label>
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
        <br>
        {{ error }}
      </div>

      <div class="hidden lg:block lg:w-1/2">
        <img
          src="../assets/images/regenter-bg.png"
          class="w-full h-auto rounded-xl"
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
        email: '',
        password: '',
        password2: '',
        group_name: ''
      },
      acceptedTerms: false,
      error: '',
    }
  },
methods: {
    submitForm() {
      this.register()},
    async register() {
      try {
        if (!this.acceptedTerms) {
          this.error = "Вы должны принять условия лицензионного договора";
        } else {
          this.form.group_name = 'ClassicUsers';
          await axios.post('http://127.0.0.1:8000/auth/register/users', this.form);
          this.$router.push('/profile');
        }
      } catch (error) {
        this.error = error.response.data;
      }
    }
  }
}
</script>