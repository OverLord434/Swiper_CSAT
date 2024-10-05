<template>
    <div>
        <section class="bg-gray-50 py-10">
            <div class="max-w-[1200px] mx-auto px-4">
                <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                    <div class="bg-white shadow-lg rounded-lg overflow-hidden mb-6">
                        <img src="../assets/images/product-photo.jpg" alt="Product Image"
                            class="w-full h-64 object-cover" />
                        <div class="p-4">
                            <h2 class="text-lg font-semibold text-gray-800">Шорты Bossa Nova</h2>
                            <p v-if="isDescriptionExpanded" class="text-gray-600 mt-1 font-medium">
                                Форма спроектирована с достаточной свободой на облегание. Карманы с подкройным бочком
                                прямого среза.
                                Пояс фиксируется широкой резинкой и декоративным светлым шнуром. Добавьте к ним футболку
                                из новой
                                коллекции и у вашего ребенка будет полноценный комплект на весну.
                            </p>
                            <button @click="toggleDescription" class="text-blue-500 text-sm mt-2">
                                {{ isDescriptionExpanded ? 'Скрыть описание' : 'Показать описание' }}
                            </button>
                            <div class="flex items-center mt-2">
                                <span class="text-yellow-500 font-semibold">4.5 ⭐</span>
                                <p class="text-gray-600 text-sm ml-2">Средняя оценка</p>
                            </div>
                            <p class="text-gray-500 mt-2">Производитель: Название компании</p>
                            <button
                                class="mt-4 w-full px-4 py-2 bg-yellow-400 text-white rounded-lg hover:bg-yellow-500 transition duration-300">Добавить
                                в избранное</button>
                        </div>
                        <div class="p-4 border-t mt-4">
                            <h3 class="text-lg font-semibold mb-2">Характеристики</h3>
                            <div class="grid grid-cols-1 gap-2">
                                <div class="flex justify-between border-b pb-2">
                                    <span>Материал:</span>
                                    <span>100% хлопок</span>
                                </div>
                                <div class="flex justify-between border-b pb-2">
                                    <span>Цвет:</span>
                                    <span>Синий</span>
                                </div>
                                <div class="flex justify-between border-b pb-2">
                                    <span>Размер:</span>
                                    <span>М</span>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="bg-white shadow-lg rounded-lg p-6 col-span-2">
                        <h3 class="text-2xl font-semibold mb-4">Отзывы</h3>
                        <div class="max-h-[300px] overflow-y-auto pr-2 mb-4"> 
                            <div v-if="reviews.length === 0" class="text-gray-500">Отзывов пока нет.</div>
                            <div v-for="review in reviews" :key="review.id"
                                class="bg-gray-100 p-4 mb-4 rounded-lg shadow-sm flex">
                                <img src="https://via.placeholder.com/50" alt="User Avatar"
                                    class="w-12 h-12 rounded-full mr-4" />
                                <div class="flex-1">
                                    <div class="flex justify-between">
                                        <span class="font-bold text-gray-700">{{ review.author }}</span>
                                        <span class="text-yellow-500">{{ review.rating }} ⭐</span>
                                    </div>
                                    <p class="mt-2 text-gray-600">{{ review.text }}</p>
                                    <p class="text-gray-500 text-sm mt-1">{{ review.date }}</p>
                                    <button class="mt-2"></button>
                                </div>
                            </div>
                        </div>

                        <h4 class="text-lg font-semibold mb-2">Оставьте свой отзыв:</h4>
                        <textarea v-model="newReview.text" placeholder="Напишите ваш отзыв"
                            class="w-full p-2 border border-gray-300 rounded-lg mb-2" rows="3"></textarea>
                        <div class="flex justify-between items-center">
                            <select v-model="newReview.rating" class="w-48 p-2 border border-gray-300 rounded-lg">
                                <option value="" disabled>Выберите оценку</option>
                                <option value="1">1 ⭐</option>
                                <option value="2">2 ⭐</option>
                                <option value="3">3 ⭐</option>
                                <option value="4">4 ⭐</option>
                                <option value="5">5 ⭐</option>
                            </select>

                            <button @click="submitReview"
                                class="w-48 px-4 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600 transition duration-300">Отправить
                                отзыв</button>
                        </div>
                    </div>
                </div>

                <div class="mt-10">
                    <h3 class="text-2xl font-semibold mb-4">Популярные товары</h3>
                    <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6">
                        <div
                            class="bg-white shadow-lg rounded-lg overflow-hidden transition-transform transform hover:scale-105">
                            <img src="https://via.placeholder.com/150" alt="Популярный товар"
                                class="w-full h-32 object-cover" />
                            <div class="p-4">
                                <h4 class="font-semibold text-gray-800">Популярный товар 1</h4>
                                <p class="text-gray-600">Краткое описание.</p>
                            </div>
                        </div>
                        <div
                            class="bg-white shadow-lg rounded-lg overflow-hidden transition-transform transform hover:scale-105">
                            <img src="https://via.placeholder.com/150" alt="Популярный товар"
                                class="w-full h-32 object-cover" />
                            <div class="p-4">
                                <h4 class="font-semibold text-gray-800">Популярный товар 2</h4>
                                <p class="text-gray-600">Краткое описание.</p>
                            </div>
                        </div>
                        <div
                            class="bg-white shadow-lg rounded-lg overflow-hidden transition-transform transform hover:scale-105">
                            <img src="https://via.placeholder.com/150" alt="Популярный товар"
                                class="w-full h-32 object-cover" />
                            <div class="p-4">
                                <h4 class="font-semibold text-gray-800">Популярный товар 3</h4>
                                <p class="text-gray-600">Краткое описание.</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </div>
</template>

<script>
export default {
    name: "ProductDiscussionPage",
    data() {
        return {
            reviews: [], // Инициализация отзывов как пустого массива
            newReview: {
                text: "",
                rating: "",
            },
            isDescriptionExpanded: false, // Управление видимостью описания
        };
    },
    methods: {
        toggleDescription() {
            this.isDescriptionExpanded = !this.isDescriptionExpanded;
        },
        submitReview() {
            if (!this.newReview.text || !this.newReview.rating) return;

            const newReview = {
                id: this.reviews.length + 1,
                author: "Пользователь", 
                text: this.newReview.text,
                rating: this.newReview.rating,
                date: new Date().toLocaleString(),
            };

            this.reviews.push(newReview);
            this.newReview.text = "";
            this.newReview.rating = "";
        },
    },
};
</script>