<template>
  <section class="h-screen flex items-center justify-center bg-gray-200">
    <div
      class="w-full max-w-3xl lg:max-w-7xl flex flex-col lg:flex-row items-center justify-center space-y-6 lg:space-y-0 lg:space-x-6"
    >
      <div class="w-full lg:w-1/2 p-8 bg-white rounded-xl shadow-xl">
        <h2 class="text-center text-3xl font-bold mb-8">Вход</h2>
        <form>
          <div class="mb-6">
            <label for="username" class="block text-lg font-medium mb-3"
              >Email</label
            >
            <input
              type="text"
              id="username"
              class="w-full px-5 py-4 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-yellow-400 text-lg"
              placeholder="Введите Email"
            />
          </div>

          <div class="mb-6">
            <label for="password" class="block text-lg font-medium mb-3"
              >Пароль</label
            >
            <input
              type="password"
              id="password"
              class="w-full px-5 py-4 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-yellow-400 text-lg"
              placeholder="Введите пароль"
            />
          </div>

          <div
            class="flex flex-col lg:flex-row justify-between items-center mb-6 text-sm"
          >
            <span class="text-[16px] mb-2 lg:mb-0">
              Еще не зарегистрированы?
              <router-link to="/register" class="text-[16px] text-blue-500 hover:underline">
                Регистрация
              </router-link>
            </span>
            <a href="#" class="text-[16px] text-blue-500 hover:underline"
              >Забыли пароль?</a
            >
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
export default {
  name: "EnterPage",
};
</script>
