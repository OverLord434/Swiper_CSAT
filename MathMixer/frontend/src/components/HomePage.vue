<template>
  <div>
    <section
      class="bg-[url('../assets/images/triangle-black.png')] bg-cover bg-center bg-no-repeat min-h-[625px]"
    >
      <div class="max-w-[1360px] mx-auto px-[10px]">
        <div class="flex justify-between items-center pt-[87px]">
          <div class="flex flex-col">
            <h1 class="text-[64px] mb-[56px] leading-[52px]">Кто мы</h1>
            <p class="max-w-[453px] min-h-[143px] mb-[46px]">
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Veniam iusto sed fugiat sunt
              maxime neque quisquam libero ea nobis, corporis id tempora. Non placeat cumque odio
              facilis labore velit porro? Lorem, ipsum. Lorem ipsum dolor sit amet consectetur
              adipisicing elit. Esse neque corrupti omnis cumque non ea adipisci perspiciatis
              exercitationem nesciunt libero.
            </p>
            <a
              href="#"
              class="border-4 border-[#FCDE00] bg-transparent rounded-[20px] w-[252px] text-center uppercase transition duration-700 ease-in-out text-[#FCDE00] py-[26px] hover:bg-[#FCDE00] hover:text-white"
              >Читать более</a
            >
          </div>
          <div class="">
            <img src="../assets/images/notebook.png" alt="Ноутбук" class="w-[600px]" />
          </div>
        </div>
      </div>
    </section>

    <section class="relative min-h-[713px] overflow-hidden">
      <img class="absolute right-0 top-0" src="../assets/images/triangle-yellow.png" alt="" />
      <img class="absolute bottom-0 left-0" src="../assets/images/min_triangle-black.png" alt="" />

      <div class="max-w-[1360px] mx-auto px-[10px] relative">
        <p class="text-[64px] leading-[52px] pt-[70px] mb-[72px]">Как мы работаем</p>

        <div class="flex justify-between">
          <div>
            <p class="max-w-[413px] mb-[226px] text-justify">
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Ipsum totam consequuntur
              harum praesentium maxime quidem saepe quae ut cum beatae architecto, nostrum commodi
              laudantium? Atque laboriosam accusantium architecto aut enim!
            </p>
            <div
              class="border-4 border-[#FCDE00] bg-transparent rounded-[20px] w-[252px] text-center uppercase transition duration-700 ease-in-out text-[#FCDE00] py-[26px] hover:bg-[#FCDE00] hover:text-white"
            >
              <a href="#">Перейти к решению</a>
            </div>
          </div>
        </div>
      </div>

      <!-- Контейнер для слайдера с вертикальным центрированием -->
      <div class="absolute top-[65px] right-0 h-full flex items-center w-[1000px] overflow-visible">
        <swiper
          :slides-per-view="1.5"
          :space-between="-140"
          :loop="true"
          :autoplay="{ delay: 2000, disableOnInteraction: false }"
        >
          <swiper-slide>
            <img src="../assets/images/slide.png" alt="Slide 1" class="w-full" />
          </swiper-slide>
          <swiper-slide>
            <img src="../assets/images/slide.png" alt="Slide 2" class="w-full" />
          </swiper-slide>
          <swiper-slide>
            <img src="../assets/images/slide.png" alt="Slide 3" class="w-full" />
          </swiper-slide>
        </swiper>
      </div>
    </section>

    <section class="relative pb-[149px]">
      <img class="absolute top-0 left-0 z-10" src="../assets/images/triangle-black-2.png" alt="" />
      <img
        class="absolute top-0 right-0 z-10"
        src="../assets/images/triangle-yellow-2.png"
        alt=""
      />
      <img
        class="absolute bottom-0 left-0 z-10"
        src="../assets/images/min_triangle-yellow.png"
        alt=""
      />

      <div class="max-w-[1360px] mx-auto relative z-10">
        <div class="flex justify-between gap-[20px]">
          <!-- Левая колонка - Топ товары -->
          <div class="bg-[#D9D9D9] px-[16px] pb-[36px] flex-shrink-0 w-[256px] rounded-[5px]">
            <h2 class="font-normal text-[38px] mb-[35px] mt-[60px]">Топ товары</h2>
            <div class="space-y-4">
              <div class="bg-white px-[17px] py-[16px] flex items-center rounded-[3px] gap-[17px]">
                <img
                  src="../assets/images/avatar.png"
                  alt="Avatar"
                  class="w-[36px] h-[36px] rounded-full"
                />
                <p class="text-[13px] font-normal">Вопрос по сборке ПК, ждет!</p>
              </div>

              <div class="bg-white px-[17px] py-[16px] flex items-center rounded-[3px] gap-[17px]">
                <img
                  src="../assets/images/avatar.png"
                  alt="Avatar"
                  class="w-[36px] h-[36px] rounded-full"
                />
                <p class="text-[13px] font-normal">Вопрос по сборке ПК, ждет!</p>
              </div>

              <div class="bg-white px-[17px] py-[16px] flex items-center rounded-[3px] gap-[17px]">
                <img
                  src="../assets/images/avatar.png"
                  alt="Avatar"
                  class="w-[36px] h-[36px] rounded-full"
                />
                <p class="text-[13px] font-normal">Вопрос по сборке ПК, ждет!</p>
              </div>

              <div class="bg-white px-[17px] py-[16px] flex items-center rounded-[3px] gap-[17px]">
                <img
                  src="../assets/images/avatar.png"
                  alt="Avatar"
                  class="w-[36px] h-[36px] rounded-full"
                />
                <p class="text-[13px] font-normal">Вопрос по сборке ПК, ждет!</p>
              </div>

              <div class="bg-white px-[17px] py-[16px] flex items-center rounded-[3px] gap-[17px]">
                <img
                  src="../assets/images/avatar.png"
                  alt="Avatar"
                  class="w-[36px] h-[36px] rounded-full"
                />
                <p class="text-[13px] font-normal">Вопрос по сборке ПК, ждет!</p>
              </div>

              <div class="bg-white px-[17px] py-[16px] flex items-center rounded-[3px] gap-[17px]">
                <img
                  src="../assets/images/avatar.png"
                  alt="Avatar"
                  class="w-[36px] h-[36px] rounded-full"
                />
                <p class="text-[13px] font-normal">Вопрос по сборке ПК, ждет!</p>
              </div>

              <div class="bg-white px-[17px] py-[16px] flex items-center rounded-[3px] gap-[17px]">
                <img
                  src="../assets/images/avatar.png"
                  alt="Avatar"
                  class="w-[36px] h-[36px] rounded-full"
                />
                <p class="text-[13px] font-normal">Вопрос по сборке ПК, ждет!</p>
              </div>

              <div class="bg-white px-[17px] py-[16px] flex items-center rounded-[3px] gap-[17px]">
                <img
                  src="../assets/images/avatar.png"
                  alt="Avatar"
                  class="w-[36px] h-[36px] rounded-full"
                />
                <p class="text-[13px] font-normal">Вопрос по сборке ПК, ждет!</p>
              </div>
            </div>
          </div>

          <!-- Центральная колонка - Вопросы участников -->
          <div class="bg-[#D9D9D9] px-[30px] pb-[60px] flex-grow w-[808px] rounded-[5px]">
            <h2 class="font-normal text-[38px] mb-[35px] mt-[60px]">Вопросы участников</h2>
            <div class="mb-[49px] flex">
              <input
                type="text"
                placeholder="Задайте свой вопрос здесь"
                class="flex-grow px-[17px] py-[16px] pr-0 border border-yellow-400 text-[25px] font-normal bg-transparent outline-none"
              />
              <button class="bg-[#FCDE00] text-[25px] font-normal text-white px-[11px]">
                Задать вопрос
              </button>
            </div>
            <div class="space-y-4">
              <div class="bg-white px-[29px] py-[27px] flex items-center rounded-[5px]">
                <img
                  src="../assets/images/avatar.png"
                  alt="Avatar"
                  class="w-12 h-12 rounded-full"
                />
                <p class="ml-[38px] flex-grow text-[18px] font-normal">
                  Почему регулярно происходит кратковременная потеря стабильности
                  интернет-соединения?
                </p>
                <button>
                  <img src="../assets/images/message-icon.svg" alt="icon" class="w-8 h-8" />
                </button>
              </div>

              <div class="bg-white px-[29px] py-[27px] flex items-center rounded-[5px]">
                <img
                  src="../assets/images/avatar.png"
                  alt="Avatar"
                  class="w-12 h-12 rounded-full"
                />
                <p class="ml-[38px] flex-grow text-[18px] font-normal">
                  Почему регулярно происходит кратковременная потеря стабильности
                  интернет-соединения?
                </p>
                <button>
                  <img src="../assets/images/message-icon.svg" alt="icon" class="w-8 h-8" />
                </button>
              </div>

              <div class="bg-white px-[29px] py-[27px] flex items-center rounded-[5px]">
                <img
                  src="../assets/images/avatar.png"
                  alt="Avatar"
                  class="w-12 h-12 rounded-full"
                />
                <p class="ml-[38px] flex-grow text-[18px] font-normal">
                  Почему регулярно происходит кратковременная потеря стабильности
                  интернет-соединения?
                </p>
                <button>
                  <img src="../assets/images/message-icon.svg" alt="icon" class="w-8 h-8" />
                </button>
              </div>

              <div class="bg-white px-[29px] py-[27px] flex items-center rounded-[5px]">
                <img
                  src="../assets/images/avatar.png"
                  alt="Avatar"
                  class="w-12 h-12 rounded-full"
                />
                <p class="ml-[38px] flex-grow text-[18px] font-normal">
                  Почему регулярно происходит кратковременная потеря стабильности
                  интернет-соединения?
                </p>
                <button>
                  <img src="../assets/images/message-icon.svg" alt="icon" class="w-8 h-8" />
                </button>
              </div>
            </div>
          </div>

          <!-- Правая колонка - Лидеры -->
          <div class="bg-[#D9D9D9] px-[16px] pb-[36px] flex-shrink-0 w-[256px] rounded-[5px]">
            <h2 class="font-normal text-[38px] mb-[35px] mt-[60px] text-center">Лидеры</h2>
            <div class="space-y-4">
              <div class="bg-white px-[17px] py-[16px] flex items-center rounded-[3px] gap-[17px]">
                <img
                  src="../assets/images/avatar.png"
                  alt="Avatar"
                  class="w-[36px] h-[36px] rounded-full"
                />
                <p class="text-[13px] font-normal">Вопрос по сборке ПК, ждет!</p>
              </div>

              <div class="bg-white px-[17px] py-[16px] flex items-center rounded-[3px] gap-[17px]">
                <img
                  src="../assets/images/avatar.png"
                  alt="Avatar"
                  class="w-[36px] h-[36px] rounded-full"
                />
                <p class="text-[13px] font-normal">Вопрос по сборке ПК, ждет!</p>
              </div>

              <div class="bg-white px-[17px] py-[16px] flex items-center rounded-[3px] gap-[17px]">
                <img
                  src="../assets/images/avatar.png"
                  alt="Avatar"
                  class="w-[36px] h-[36px] rounded-full"
                />
                <p class="text-[13px] font-normal">Вопрос по сборке ПК, ждет!</p>
              </div>

              <div class="bg-white px-[17px] py-[16px] flex items-center rounded-[3px] gap-[17px]">
                <img
                  src="../assets/images/avatar.png"
                  alt="Avatar"
                  class="w-[36px] h-[36px] rounded-full"
                />
                <p class="text-[13px] font-normal">Вопрос по сборке ПК, ждет!</p>
              </div>

              <div class="bg-white px-[17px] py-[16px] flex items-center rounded-[3px] gap-[17px]">
                <img
                  src="../assets/images/avatar.png"
                  alt="Avatar"
                  class="w-[36px] h-[36px] rounded-full"
                />
                <p class="text-[13px] font-normal">Вопрос по сборке ПК, ждет!</p>
              </div>

              <div class="bg-white px-[17px] py-[16px] flex items-center rounded-[3px] gap-[17px]">
                <img
                  src="../assets/images/avatar.png"
                  alt="Avatar"
                  class="w-[36px] h-[36px] rounded-full"
                />
                <p class="text-[13px] font-normal">Вопрос по сборке ПК, ждет!</p>
              </div>

              <div class="bg-white px-[17px] py-[16px] flex items-center rounded-[3px] gap-[17px]">
                <img
                  src="../assets/images/avatar.png"
                  alt="Avatar"
                  class="w-[36px] h-[36px] rounded-full"
                />
                <p class="text-[13px] font-normal">Вопрос по сборке ПК, ждет!</p>
              </div>

              <div class="bg-white px-[17px] py-[16px] flex items-center rounded-[3px] gap-[17px]">
                <img
                  src="../assets/images/avatar.png"
                  alt="Avatar"
                  class="w-[36px] h-[36px] rounded-full"
                />
                <p class="text-[13px] font-normal">Вопрос по сборке ПК, ждет!</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="min-h-[708px] relative">
      <img class="absolute top-0 left-0 z-0" src="../assets/images/triangle-yellow-3.png" alt="" />
      <img class="absolute top-0 right-0 z-0" src="../assets/images/triangle-black-3.png" alt="" />

      <div class="text-center">
        <span class="text-[64px] leading-[52px]">Что говорит клиент</span>
      </div>

      <div
        class="absolute left-[400px] flex items-center mx-auto max-w-[973px] pt-[87px] gap-[80px] z-11"
      >
        <div class="relative w-[213px] h-[213px] mx-auto mt-28">
          <div
            class="w-full h-full transform rotate-45 border-[20px] border-[#D9D9D9] overflow-hidden"
          >
            <img
              src="../assets/images/client-photo.png"
              alt="Фото клиента"
              class="w-full h-full object-cover object-center -rotate-45"
            />
          </div>
        </div>

        <div class="mt-10">
          <p class="max-w-[650px] text-[20px] font-medium pt-[70px]">
            «В старом мире вы посвящали 30% своего времени созданию первоклассного обслуживания и
            70% времени кричали об этом. В новом мире все наоборот».
          </p>
          <p class="pt-[3px] font-normal">Лапаев А.С. руководитель</p>
        </div>
      </div>
    </section>

  </div>
</template>

<script>
import { Swiper, SwiperSlide } from 'swiper/vue'

export default {
  name: 'HomePage',
  components: {
    Swiper,
    SwiperSlide
  }
}
</script>
