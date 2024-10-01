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
            <h2 class="text-[32px] font-semibold mb-[10px]">Иван Иванов</h2>
            <p class="text-[19px] font-bold text-gray-600">Онлайн</p>
            <p class="text-[20px] font-light text-gray-600 mb-[30px]">ivan@list.ru</p>
            <button
              class="border-4 border-yellow-400 bg-transparent rounded-full w-[200px] py-[12px] text-yellow-400 hover:bg-yellow-400 hover:text-white transition duration-500"
            >
              Редактировать
            </button>
          </div>

          <div class="w-full md:w-[65%] bg-gray-100 p-[30px] rounded-lg">
            <h3 class="text-[28px] font-semibold mb-[30px]">Действия пользователя</h3>
            <div class="bg-white p-[20px] mb-[20px] rounded-lg shadow-md">
              <p class="text-[20px] font-medium">Задал вопрос по сборке ПК</p>
              <p class="text-[16px] text-gray-600">Почему не загружается операционная система после сборки?</p>
              <p class="text-[14px] text-gray-400 mt-[10px]">2024-09-28</p>
            </div>
            <div class="bg-white p-[20px] mb-[20px] rounded-lg shadow-md">
              <p class="text-[20px] font-medium">Оставил отзыв о сервисе</p>
              <p class="text-[16px] text-gray-600">Очень доволен качеством обслуживания.</p>
              <p class="text-[14px] text-gray-400 mt-[10px]">2024-09-25</p>
            </div>
            <div class="bg-white p-[20px] mb-[20px] rounded-lg shadow-md">
              <p class="text-[20px] font-medium">Присоединился к обсуждению по теме ПК</p>
              <p class="text-[16px] text-gray-600">Обсуждение проблем с выбором видеокарт.</p>
              <p class="text-[14px] text-gray-400 mt-[10px]">2024-09-20</p>
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
  name: "ProfilePage",
  components: {
    AppHeader,
    AppFooter,
  },
};
</script>
