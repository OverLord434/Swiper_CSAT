<template>
  <div>
    <section
      class="bg-[url('../assets/images/triangle-black.png')] bg-cover bg-center bg-no-repeat min-h-[625px] who_section">
      <div class="max-w-[1360px] mx-auto px-2">
        <div class="flex flex-col md:flex-row justify-between items-center pt-[87px]">
          <div class="flex flex-col md:w-1/2 items-center md:items-start">
            <h1 class="text-[64px] mb-[56px] leading-[52px] text-center md:text-left section-title">Кто мы</h1>
            <p class="max-w-[453px] min-h-[143px] mb-[46px] text-center md:text-left section-paragraph">
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Veniam iusto sed fugiat sunt
              maxime neque quisquam libero ea nobis, corporis id tempora. Non placeat cumque odio
              facilis labore velit porro? Lorem, ipsum. Lorem ipsum dolor sit amet consectetur
              adipisicing elit. Esse neque corrupti omnis cumque non ea adipisci perspiciatis
              exercitationem nesciunt libero.
            </p>
            <a href="#"
              class="border-4 border-[#FCDE00] bg-transparent rounded-[20px] w-[252px] text-center uppercase transition duration-700 ease-in-out text-[#FCDE00] py-[26px] hover:bg-[#FCDE00] hover:text-white section-button mb-6">
              Читать более
            </a>
          </div>
          <div class="md:w-1/2 flex justify-center md:justify-end mt-6 md:mt-0">
            <img src="../assets/images/notebook.png" alt="Ноутбук" class="w-full max-w-[600px] section-image" />
          </div>
        </div>
      </div>
    </section>


    <section class="relative min-h-[713px] overflow-hidden pb-[30px]">
      <img class="absolute right-0 top-0 h-full z-2" src="../assets/images/triangle-yellow.png" alt="" />
      <img class="absolute bottom-0 left-0" src="../assets/images/min_triangle-black.png" alt="" />

      <div class="max-w-[1360px] mx-auto px-[10px] relative md:static z-10">
        <p class="text-[64px] leading-[52px] pt-[70px] mb-[72px] slider-title">Как мы работаем</p>

        <div class="flex justify-between relative z-12">
          <div>
            <p class="max-w-[413px] mb-[226px] text-justify slider-paragraph">
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Ipsum totam consequuntur
              harum praesentium maxime quidem saepe quae ut cum beatae architecto, nostrum commodi
              laudantium? Atque laboriosam accusantium architecto aut enim!
            </p>
            <div
              class="border-4 border-black md:border-[#FCDE00] bg-transparent rounded-[20px] w-[252px] text-center uppercase transition duration-700 ease-in-out text-black md:text-[#FCDE00] py-[26px] hover:bg-[#FCDE00] hover:text-white slider-btn">
              <a href="#">Перейти к решению</a>
            </div>
          </div>
        </div>
      </div>

      <div class="absolute top-[65px] right-0 h-full flex items-center w-[1000px] overflow-visible slider-container">
        <swiper :slides-per-view="1.5" :space-between="-50" :loop="true">
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

    <section class="relative pb-[149px] responsive-section">
      <img class="absolute top-0 left-0 z-10" src="../assets/images/triangle-black-2.png" alt="" />
      <img class="absolute top-0 right-0 z-10" src="../assets/images/triangle-yellow-2.png" alt="" />
      <img class="absolute bottom-0 left-0 z-10" src="../assets/images/min_triangle-yellow.png" alt="" />

      <div class="max-w-[1360px] mx-auto px-2 relative z-10">
        <div class="flex flex-wrap justify-center gap-3">
          <div
            class="bg-[#D9D9D9] flex-shrink-0 w-[256px] flex-grow transition-all duration-300 hover:flex-grow-2 rounded-[5px] px-4 pb-8 responsive-card">
            <h2 class="font-normal text-[38px] mb-8 mt-8 responsive-title">Топ товары</h2>
            <div class="product-list">
              <div class="bg-white px-4 py-2 flex items-center rounded-[3px] gap-4">
                <img src="../assets/images/avatar.png" alt="Avatar"
                  class="w-[36px] h-[36px] rounded-full responsive-avatar" />
                <p class="text-[13px] font-normal">Вопрос по сборке ПК, ждет!</p>
              </div>
            </div>
          </div>

          <div
            class="bg-[#D9D9D9] flex-grow w-full md:w-[808px] transition-all duration-300 rounded-[5px] px-6 pb-8 responsive-card">
            <h2 class="font-normal text-[38px] mb-8 mt-8 responsive-title">Вопросы участников</h2>
            <div class="mb-12 flex">
              <input type="text" placeholder="Задайте свой вопрос здесь"
                class="flex-grow px-4 py-2 border border-yellow-400 text-[25px] font-normal bg-transparent outline-none responsive-input" />
              <button class="bg-[#FCDE00] text-[25px] font-normal text-white px-4 responsive-button">Задать
                вопрос</button>
            </div>
            <div class="question-list">
              <div class="bg-white px-6 py-4 flex items-center rounded-[5px]">
                <img src="../assets/images/avatar.png" alt="Avatar" class="w-12 h-12 rounded-full responsive-avatar" />
                <p class="ml-4 flex-grow text-[18px] font-normal">Почему регулярно происходит кратковременная потеря
                  стабильности интернет-соединения?</p>
                <button>
                  <img src="../assets/images/message-icon.svg" alt="icon" class="w-8 h-8 responsive-icon" />
                </button>
              </div>
            </div>
          </div>
          <div
            class="bg-[#D9D9D9] flex-shrink-0 w-[256px] flex-grow transition-all duration-300 hover:flex-grow-2 rounded-[5px] px-4 pb-8 responsive-card">
            <h2 class="font-normal text-[38px] mb-8 mt-8 text-center responsive-title">Лидеры</h2>
            <div class="leader-list">
              <div class="bg-white px-4 py-2 flex items-center rounded-[3px] gap-4">
                <img src="../assets/images/avatar.png" alt="Avatar"
                  class="w-[36px] h-[36px] rounded-full responsive-avatar" />
                <p class="text-[13px] font-normal">Вопрос по сборке ПК, ждет!</p>
              </div>
            </div>
          </div>
        </div>

        <div class="hidden fixed inset-0 flex items-center justify-center bg-black bg-opacity-70" id="model">
          <div
            class="bg-white p-6 sm:p-8 rounded-xl shadow-2xl max-w-md sm:max-w-[1200px] w-full min-h-[700px] relative transform transition-all duration-300 scale-95 hover:scale-100 pop-up">
            <div class="flex flex-col sm:flex-row justify-center items-start mt-4">
              <div class="flex flex-col items-center justify-center w-full sm:w-[40%] mb-6 sm:mb-0">
                <div class="flex flex-col items-center justify-center mb-4 w-full">
                  <img id="edit-img" src="" alt="Product"
                    class="w-[300px] h-[250px] mb-4 border-4 border-yellow-500 rounded-xl object-cover">
                  <label for="product"
                    class="cursor-pointer bg-yellow-400 text-white px-4 py-2 rounded-lg shadow-md hover:bg-yellow-700 transition duration-300">Добавить
                    фото</label>
                  <input id="product" type="file" class="hidden" />
                </div>
                <div class="max-w-[300px] mx-auto">
                  <label class="block mb-2 text-center">Характеристики</label>
                  <h2 class="text-[16px] font-normal mb-4">{{ characteristics.charackterstick1 }}</h2>
                  <h2 class="text-[16px] font-normal mb-4">{{ characteristics.charackterstick2 }}</h2>
                  <h2 class="text-[16px] font-normal mb-4">{{ characteristics.charackterstick3 }}</h2>
                  <h2 class="text-[16px] font-normal mb-4">{{ characteristics.charackterstick4 }}</h2>
                  <h2 class="text-[16px] font-normal mb-4">{{ characteristics.charackterstick5 }}</h2>
                </div>
              </div>

              <div class="w-full sm:w-[40%]">
                <h2 id="addProductTitle" class="text-3xl font-bold mb-4 text-center"></h2>
                <form class="space-y-4" id="productForm" @submit.prevent="submitForm">
                  <label class="block mb-2">Название:</label>
                  <input type="text" v-model="productName"
                    class="text-[16px] bg-gray-100 font-normal mb-4 border rounded-lg p-2 w-full outline-none ring-2 ring-yellow-400"
                    placeholder="Введите название" />

                  <select v-model="selectedCategory" @change="fetchCharacteristics"
                    class="font-normal text-[16px] border border-gray-300 rounded-lg p-2 ring-2 ring-yellow-400 outline-none transition duration-150 ease-in-out w-full">
                    <option disabled selected>Выберите категорию</option>
                    <option v-for="category in categories" :key="category.id_category" :value="category.id_category">{{ category.name }}</option>
                  </select>

                  <label class="block mb-2">Описание:</label>
                  <textarea v-model="productDescription"
                    class="text-[16px] bg-gray-100 font-normal mb-4 border rounded-lg p-2 w-full outline-none ring-2 ring-yellow-400"
                    rows="4" placeholder="Введите описание"></textarea>

                  <div class="flex justify-center items-center gap-2">
                    <button id="undoBtn" type="button"
                      class="bg-gradient-to-r from-gray-300 to-gray-500 text-white px-4 py-2 rounded-full w-full shadow-md hover:shadow-xl transition-all">Отмена</button>
                    <button type="submit"
                      class="bg-gradient-to-r from-[#fcde00] to-[#ff7f00] text-white px-4 py-2 rounded-full w-full shadow-md hover:shadow-xl transition-all">Добавить</button>
                  </div>
                </form>
              </div>
            </div>
          </div>
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
  },
  data() {
    return {
      categories: [],
      selectedCategory: null,
      productName: '',
      productDescription: '',
      characteristics: {
        charackterstick1: '',
        charackterstick2: '',
        charackterstick3: '',
        charackterstick4: '',
        charackterstick5: '',
      },
    };
  },
  mounted() {
    this.fetchCategories();

    // Событие для кнопки "Отмена"
    document.getElementById('undoBtn').addEventListener('click', () => {
      document.getElementById('model').classList.add('hidden');
      window.location.reload();
    });

    // Событие для загрузки изображения продукта
    document.getElementById('product').addEventListener('change', function () {
      const file = this.files[0];
      if (file) {
        const reader = new FileReader();
        reader.onload = () => {
          document.getElementById('edit-img').src = reader.result;
        };
        reader.readAsDataURL(file);
      }
    });
  },
  methods: {
    // Загрузка категорий
    async fetchCategories() {
      try {
        const response = await fetch('http://127.0.0.1:8000/main/api/categories/');
        const data = await response.json();
        this.categories = data;
      } catch (error) {
        console.error('Ошибка при загрузке категорий:', error);
      }
    },

    // Загрузка характеристик для выбранной категории
    async fetchCharacteristics() {
      if (this.selectedCategory) {
        try {
          const response = await fetch(`http://127.0.0.1:8000/main/api/characteristics/${this.selectedCategory}/`);
          const data = await response.json();
          this.characteristics = data;
        } catch (error) {
          console.error('Ошибка при загрузке характеристик:', error);
        }
      }
    },

    // Отправка формы с товаром
    async submitForm() {
      if (this.productName && this.productDescription && this.selectedCategory) {
        try {
          const response = await fetch('http://127.0.0.1:8000/main/api/products/', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify({
              name: this.productName,
              textdes: this.productDescription,
              category: this.selectedCategory,
            }),
          });

          if (!response.ok) {
            throw new Error('Ошибка при сохранении товара');
          }

          const data = await response.json();
          console.log('Товар успешно сохранен:', data);
        } catch (error) {
          console.error('Ошибка при отправке формы:', error);
        }
      } else {
        alert('Заполните все поля!');
      }
    },
  },
};
</script>

<style>
.pop-up::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 40%;
  background-image: linear-gradient(to top, #fcde00, #ff7f00);
  z-index: -1;
}

@media (max-width: 1335px) {
  .slider-title {
    font-size: 48px;
    line-height: 40px;
  }

  .slider-paragraph {
    max-width: 350px;
    margin-bottom: 100px;
  }

  .slider-container {
    width: 800px;
  }
}

@media (max-width: 1200px) {
  .custom-container {
    max-width: 100%;
  }

  .custom-column {
    width: 100%;
    margin-bottom: 20px;
  }

  .custom-heading {
    font-size: 30px;
    margin-top: 40px;
    margin-bottom: 20px;
  }

  .custom-input,
  .custom-button {
    font-size: 20px;
  }

  .space-y-4 {
    margin-bottom: 20px;
  }
}

@media (max-width: 1085px) {
  .slider-title {
    font-size: 40px;
    line-height: 36px;
  }

  .slider-paragraph {
    max-width: 300px;
    margin-bottom: 80px;
  }

  .slider-container {
    width: 700px;
  }
}

@media (max-width: 960px) {
  .slider-title {
    font-size: 36px;
    line-height: 32px;
  }

  .slider-paragraph {
    max-width: 250px;
    margin-bottom: 60px;
  }

  .slider-container {
    width: 600px;
  }
}

@media (max-width: 860px) {
  .slider-title {
    font-size: 32px;
    line-height: 28px;
  }

  .slider-paragraph {
    max-width: 220px;
    margin-bottom: 50px;
  }

  .slider-container {
    width: 500px;
  }

}

@media (max-width: 768px) {
  .who_section {
    background-color: rgba(255, 255, 255, 0.5);
    background-blend-mode: overlay;
  }

  .slider-container {
    position: relative;
    top: auto;
    margin-left: auto;
    margin-top: 20px;
  }

  .slider-title {
    font-size: 40px;
  }

  .slider-paragraph {
    max-width: 100%;
  }

  .client-content {
    flex-direction: column;
    align-items: center;
    left: 0;
    max-width: 100%;
    padding-top: 20px;
  }

  .triangle-yellow,
  .triangle-black {
    width: 100%;
    height: 100%;
  }

  .title-text {
    font-size: 36px;
    line-height: 44px;
  }

  .text-content p {
    text-align: center;
    padding-top: 10px;

  }

  .custom-flex {
    flex-direction: column;
  }

  .custom-column {
    padding: 10px;
  }

  .custom-heading {
    font-size: 24px;
  }

  .custom-text {
    font-size: 12px;
  }

  .custom-question-text {
    font-size: 16px;
  }
}

@media (max-width: 600px) {
  .responsive-section {
    padding-bottom: 100px;
  }

  .responsive-card {
    padding: 8px;
  }

  .responsive-title {
    font-size: 24px;
    margin-bottom: 4px;
    margin-top: 4px;
  }

  .responsive-input {
    font-size: 16px;
    padding: 6px;
  }

  .responsive-button {
    font-size: 16px;
    padding: 6px 12px;
  }

  .product-list,
  .question-list,
  .leader-list {
    margin-bottom: 8px;
  }

  .responsive-avatar {
    width: 24px;
    height: 24px;
  }

  .responsive-icon {
    width: 24px;
    height: 24px;
  }
}

@media (max-width: 500px) {
  .section-title {
    font-size: 36px;
    margin-bottom: 24px;
    line-height: 40px;
  }

  .section-paragraph {
    max-width: 90%;
    min-height: 100px;
    margin-bottom: 24px;
    font-size: 14px;
  }

  .section-button {
    width: 180px;
    padding: 16px;
  }

  .section-image {
    max-width: 300px;
  }

  .slider-btn {
    font-size: 14px;
    width: 200px;
    border: solid 2px;
  }

  .title-text {
    font-size: 28px;
  }

  .client-content {
    padding: 10px;
  }
}

@media (max-width: 480px) {
  .custom-heading {
    font-size: 20px;
  }

  .custom-item,
  .custom-question-item {
    padding: 10px;
  }

  .custom-input {
    padding: 10px;
  }

  .custom-button {
    padding: 10px;
  }

  .custom-icon {
    width: 24px;
    height: 24px;
  }
}

@media (max-width: 368px) {
  .slider-title {
    font-size: 22px;
    line-height: 40px;
    padding-top: 30px;
    margin-bottom: 20px;
  }

  .slider-paragraph {
    max-width: 100%;
    margin-bottom: 40px;
    font-size: 14px;
  }

  .border-4 {
    width: 100%;
    padding: 15px;
  }

  .slider-container {
    width: 100%;
    overflow: hidden;
  }

  .swiper-slide img {
    max-width: 100%;
    height: auto;
    margin-top: 60px;
  }

  .slider-btn {
    font-size: 12px;
    width: 200px;
    margin: 0 auto;
    border: solid 2px;
  }
}
</style>