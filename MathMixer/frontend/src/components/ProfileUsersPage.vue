<template>
  <div>
    <AppHeader></AppHeader>
    <section class="bg-[url('../assets/images/triangle-black.png')] bg-cover bg-center min-h-[625px] py-[50px]">
      <div class="max-w-[1200px] mx-auto px-4">
        <div class="flex flex-col md:flex-row justify-between items-center mb-[50px]">
          <div class="flex flex-col items-center w-full md:w-[30%] bg-gray-100 p-[20px] rounded-lg mb-6 md:mb-0">
            <img
              src=""
              alt="User Avatar"
              class="w-[200px] h-[200px] rounded-full mb-[20px] border-4 border-yellow-400"
            />
            <h2 class="text-[25px] font-semibold">Никнейм</h2>
            <p class="text-[14px] text-gray-600">Зарегистрирован 2022-05-16</p>
            <div class="flex items-center space-x-2 mt-2">
              <div
                class="w-3 h-3 rounded-full"
                :class="{ 'bg-green-500': isOnline, 'bg-red-500': !isOnline }"
              ></div>
              <p class="text-[18px] font-bold text-gray-600">Онлайн</p>
            </div>
            <p class="text-[20px] font-light text-gray-600 mb-[20px]">ivan@list.ru</p>
            <div class="flex items-center gap-[2px] mb-[20px]">
              <span class="text-[18px] font-semibold">2500</span>
              <img class="h-7 w-7 pb-[6px]" src="../assets/images/star.svg" alt="Иконка звёздочки" />
            </div>
            <button
              class="border-4 border-yellow-400 bg-transparent rounded-full w-[200px] py-[12px] text-yellow-400 hover:bg-yellow-400 hover:text-white transition duration-500"
            >
              Редактировать
            </button>
          </div>

          <div class="w-full md:w-[65%] bg-gray-100 p-[30px] rounded-lg">
            <h3 class="text-[28px] font-semibold mb-[30px]">История отзывов</h3>

            <div class="max-h-[400px] overflow-y-auto pr-2">
              
              <a href="#" class="block bg-white p-[20px] mb-[20px] rounded-lg shadow-md hover:bg-gray-50 transition">
                <p class="text-[20px] font-medium">Отзыв о ноутбуке ASUS ROG Strix</p>
                <p class="text-[16px] text-gray-600">Очень доволен качеством. Работает отлично.</p>
                <p class="text-[14px] text-gray-400 mt-[10px]">2024-09-28</p>
              </a>

              <a href="#" class="block bg-white p-[20px] mb-[20px] rounded-lg shadow-md hover:bg-gray-50 transition">
                <p class="text-[20px] font-medium">Отзыв о мониторе Samsung</p>
                <p class="text-[16px] text-gray-600">Удобный и качественный монитор, рекомендую!</p>
                <p class="text-[14px] text-gray-400 mt-[10px]">2024-09-25</p>
              </a>

              <a href="#" class="block bg-white p-[20px] mb-[20px] rounded-lg shadow-md hover:bg-gray-50 transition">
                <p class="text-[20px] font-medium">Отзыв о видеокарте NVIDIA RTX 3080</p>
                <p class="text-[16px] text-gray-600">Отличная производительность, но шумный кулер.</p>
                <p class="text-[14px] text-gray-400 mt-[10px]">2024-09-20</p>
              </a>

              <a href="#" class="block bg-white p-[20px] mb-[20px] rounded-lg shadow-md hover:bg-gray-50 transition">
                <p class="text-[20px] font-medium">Отзыв о клавиатуре Logitech G Pro</p>
                <p class="text-[16px] text-gray-600">Отличная клавиатура для игр.</p>
                <p class="text-[14px] text-gray-400 mt-[10px]">2024-09-15</p>
              </a>

            </div>
          </div>
        </div>
      </div>
    </section>
    <AppFooter></AppFooter>
  </div>
</template>

<script>
import AppHeader from "./AppHeader.vue";
import AppFooter from "./AppFooter.vue";

export default {
  name: "ProfileUsersPage",
  components: {
    AppHeader,
    AppFooter,
  },
  data() {
    return {
      isOnline: true, // Пример состояния, которое определяет онлайн статус
    };
  },
};
</script>
