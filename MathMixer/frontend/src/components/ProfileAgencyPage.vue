<template>
  <div>
    <section class="bg-[url('../assets/images/triangle-black.png')] bg-cover bg-center min-h-[625px] py-12">
      <div class="max-w-[1200px] mx-auto px-4">
        <div class="flex flex-col md:flex-row justify-between items-center mb-12">
          <div class="flex flex-col items-center w-full md:w-[30%] bg-gray-100 p-5 rounded-lg mb-6 md:mb-0">
            <img src="" alt="Organization Avatar"
              class="w-48 h-48 rounded-full mb-5 border-4 border-yellow-400" />
            <div class="flex items-center space-x-1">
              <h2 class="text-lg font-semibold">Название организации</h2>
              <img class="h-6 w-6" src="../assets/images/tick.svg" alt="Иконка подтвержденной организации" />
            </div>
            <p class="text-sm text-gray-600">Зарегистрирован 2022-05-16</p>
            <div class="flex items-center space-x-2 mt-2">
              <div class="w-3 h-3 rounded-full" :class="{ 'bg-green-500': isOnline, 'bg-red-500': !isOnline }"></div>
              <p class="text-lg font-bold text-gray-600">Онлайн</p>
            </div>
            <p class="text-lg font-light text-gray-600 mb-5">ivan@list.ru</p>
            <div class="flex items-center gap-1 mb-5">
              <span class="text-lg font-semibold">4.8</span>
              <img class="h-7 w-7" src="../assets/images/star.svg" alt="Иконка звёздочки" />
              <p class="text-gray-600 text-sm">Средняя оценка</p>
            </div>
            <button id="EditProfileBtn"
              class="border-4 border-yellow-400 bg-transparent rounded-full w-full md:w-48 py-3 text-yellow-400 hover:bg-yellow-400 hover:text-white transition duration-500">
              Редактировать
            </button>
            <div class="flex justify-center mt-5">
              <button
                class="border-4 border-red-500 bg-transparent rounded-full w-full md:w-48 py-3 text-red-500 hover:bg-red-500 hover:text-white transition duration-500">
                Выйти из аккаунта
              </button>
            </div>
          </div>

          <div class="w-full md:w-2/3 bg-gray-100 p-5 md:p-7 rounded-lg mb-6 md:mb-0">
            <h3 class="text-2xl font-semibold mb-6">История товаров</h3>

            <div class="max-h-[400px] overflow-y-auto pr-2">
              <a href="#" class="block bg-white p-5 mb-5 rounded-lg shadow-md hover:bg-gray-50 transition">
                <p class="text-lg font-medium">Ноутбук ASUS ROG Strix</p>
                <p class="text-md text-gray-600">Продан за 1200$</p>
                <p class="text-sm text-gray-400 mt-2">2024-09-28</p>
              </a>
              <a href="#" class="block bg-white p-5 mb-5 rounded-lg shadow-md hover:bg-gray-50 transition">
                <p class="text-lg font-medium">Монитор Samsung</p>
                <p class="text-md text-gray-600">Продан за 350$</p>
                <p class="text-sm text-gray-400 mt-2">2024-09-25</p>
              </a>
              <a href="#" class="block bg-white p-5 mb-5 rounded-lg shadow-md hover:bg-gray-50 transition">
                <p class="text-lg font-medium">Видеокарта NVIDIA RTX 3080</p>
                <p class="text-md text-gray-600">Продана за 950$</p>
                <p class="text-sm text-gray-400 mt-2">2024-09-20</p>
              </a>
              <a href="#" class="block bg-white p-5 mb-5 rounded-lg shadow-md hover:bg-gray-50 transition">
                <p class="text-lg font-medium">Мышь Logitech G Pro</p>
                <p class="text-md text-gray-600">Продана за 150$</p>
                <p class="text-sm text-gray-400 mt-2">2024-09-15</p>
              </a>
            </div>
          </div>
        </div>

        <div class="hidden fixed inset-0 flex items-center justify-center bg-black bg-opacity-70 z-50" id="modal">
          <div class="bg-white rounded-lg p-5 md:p-8 w-11/12 md:w-1/3 shadow-2xl transition-transform transform scale-95 hover:scale-100">
            <h3 class="text-xl font-semibold text-center text-gray-800 mb-4">Редактировать профиль</h3>
            <div class="flex flex-col items-center mb-4">
              <img src="" alt="Avatar" id="edit-img"
                class="rounded-full w-32 h-32 mb-4 border-4 border-yellow-400 transition-transform transform hover:scale-110" />
              <label for="avatar"
                class="cursor-pointer bg-yellow-400 text-white px-4 py-2 rounded-lg shadow-md hover:bg-yellow-500 transition duration-300">Изменить
                аватарку</label>
              <input id="avatar" type="file" class="hidden" />
            </div>
            <form>
              <div class="mb-4">
                <label for="username" class="block text-sm font-medium text-gray-700">Название организации</label>
                <input type="text" id="username"
                  class="border rounded-lg w-full p-2 border-gray-300 focus:outline-none focus:ring-2 focus:ring-yellow-400 transition"
                  placeholder="Введите новое название организации" />
              </div>
              <div class="mb-4">
                <label for="email" class="block text-sm font-medium text-gray-700">Email</label>
                <input type="email" id="email"
                  class="border rounded-lg w-full p-2 border-gray-300 focus:outline-none focus:ring-2 focus:ring-yellow-400 transition"
                  placeholder="Введите новый email" />
              </div>
              <div class="mb-4">
                <label for="password" class="block text-sm font-medium text-gray-700">Пароль</label>
                <input type="password" id="password"
                  class="border rounded-lg w-full p-2 border-gray-300 focus:outline-none focus:ring-2 focus:ring-yellow-400 transition"
                  placeholder="Введите новый пароль" />
              </div>
              <div class="mb-4">
                <label for="confirmPassword" class="block text-sm font-medium text-gray-700">Подтверждение
                  пароля</label>
                <input type="password" id="confirmPassword"
                  class="border rounded-lg w-full p-2 border-gray-300 focus:outline-none focus:ring-2 focus:ring-yellow-400 transition"
                  placeholder="Подтвердите новый пароль" />
              </div>
              <div class="flex justify-end">
                <button type="button" id="UndoBtn"
                  class="mr-4 text-gray-500 hover:text-gray-700 transition duration-300">Отмена</button>
                <button type="submit"
                  class="bg-yellow-400 text-white rounded-lg px-4 py-2 shadow-md hover:bg-yellow-500 transition duration-300">Сохранить
                  изменения</button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>


<script>
export default {
  name: "ProfileAgencyPage",
  data() {
    return {
      isOnline: true, // Пример состояния, которое определяет онлайн статус
    };
  },
  mounted() {
    document.getElementById('EditProfileBtn').addEventListener('click', function () {
      document.getElementById('modal').classList.remove('hidden');
    });
    document.getElementById('UndoBtn').addEventListener('click', function () {
      document.getElementById('modal').classList.add('hidden');
    });

    document.getElementById('avatar').addEventListener('change', function () {
      var file = this.files[0];
      if (file) {
        var reader = new FileReader();
        reader.onload = function () {
          document.getElementById('edit-img').src = reader.result;
        }
        reader.readAsDataURL(file);
      }
    });
  }
};
</script>

<style>
  
</style>