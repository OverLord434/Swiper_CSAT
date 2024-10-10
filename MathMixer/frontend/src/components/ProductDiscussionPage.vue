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
                                из новой коллекции и у вашего ребенка будет полноценный комплект на весну.
                            </p>
                            <button @click="toggleDescription" class="text-blue-500 text-sm mt-2">
                                {{ isDescriptionExpanded ? 'Скрыть описание' : 'Показать описание' }}
                            </button>

                            <p class="text-gray-500 mt-2">Цена: 500₽</p>
                            
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
                                    <span class="text-yellow-500">{{ ratings.material }} ⭐</span>
                                </div>
                                <div class="flex justify-between border-b pb-2">
                                    <span>Цвет:</span>
                                    <span>Синий</span>
                                    <span class="text-yellow-500">{{ ratings.color }} ⭐</span>
                                </div>
                                <div class="flex justify-between border-b pb-2">
                                    <span>Размер:</span>
                                    <span>М</span>
                                    <span class="text-yellow-500">{{ ratings.size }} ⭐</span>
                                </div>
                                <div class="flex justify-between border-b pb-2">
                                    <span>Стиль:</span>
                                    <span>Классические</span>
                                    <span class="text-yellow-500">{{ ratings.style }} ⭐</span>
                                </div>
                                <div class="flex justify-between border-b pb-2">
                                    <span>Вес:</span>
                                    <span>200г</span>
                                    <span class="text-yellow-500">{{ ratings.weight }} ⭐</span>
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
                                    </div>
                                    <p class="mt-2 text-gray-600">{{ review.text }}</p>
                                    <p class="text-gray-500 text-sm mt-1">{{ review.date }}</p>
                                </div>
                            </div>
                        </div>

                        <h4 class="text-lg font-semibold mb-2">Оставьте свой отзыв:</h4>
                        <textarea v-model="newReview.text" placeholder="Напишите ваш отзыв"
                            class="w-full p-2 border border-gray-300 rounded-lg mb-2" rows="3"></textarea>
                        <div class="flex flex-col sm:flex-row justify-between items-center">
                            <button @click="submitReview"
                                class="w-full sm:w-48 px-4 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600 transition duration-300">Отправить
                                отзыв</button>
                        </div>

                        <div class="mt-8 p-6 bg-white shadow-md rounded-lg">
                            <h4 class="text-xl font-semibold mb-4 text-gray-800">Оцените характеристики:</h4>
                            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                                <div>
                                    <label for="materialRating"
                                        class="block mb-1 font-medium text-gray-700">Материал:</label>
                                    <select v-model="ratings.material" id="materialRating"
                                        class="border border-gray-300 rounded-lg p-2 focus:ring-2 focus:ring-yellow-400 focus:outline-none transition duration-150 ease-in-out">
                                        <option value="" disabled>Выберите оценку</option>
                                        <option v-for="num in 5" :key="num" :value="num">{{ num }} ⭐</option>
                                    </select>
                                </div>
                                <div>
                                    <label for="colorRating" class="block mb-1 font-medium text-gray-700">Цвет:</label>
                                    <select v-model="ratings.color" id="colorRating"
                                        class="border border-gray-300 rounded-lg p-2 focus:ring-2 focus:ring-yellow-400 focus:outline-none transition duration-150 ease-in-out">
                                        <option value="" disabled>Выберите оценку</option>
                                        <option v-for="num in 5" :key="num" :value="num">{{ num }} ⭐</option>
                                    </select>
                                </div>
                                <div>
                                    <label for="sizeRating" class="block mb-1 font-medium text-gray-700">Размер:</label>
                                    <select v-model="ratings.size" id="sizeRating"
                                        class="border border-gray-300 rounded-lg p-2 focus:ring-2 focus:ring-yellow-400 focus:outline-none transition duration-150 ease-in-out">
                                        <option value="" disabled>Выберите оценку</option>
                                        <option v-for="num in 5" :key="num" :value="num">{{ num }} ⭐</option>
                                    </select>
                                </div>
                                <div>
                                    <label for="sizeRating" class="block mb-1 font-medium text-gray-700">Стиль:</label>
                                    <select v-model="ratings.style" id="sizeRating"
                                        class="border border-gray-300 rounded-lg p-2 focus:ring-2 focus:ring-yellow-400 focus:outline-none transition duration-150 ease-in-out">
                                        <option value="" disabled>Выберите оценку</option>
                                        <option v-for="num in 5" :key="num" :value="num">{{ num }} ⭐</option>
                                    </select>
                                </div>
                                <div>
                                    <label for="sizeRating" class="block mb-1 font-medium text-gray-700">Вес:</label>
                                    <select v-model="ratings.weight" id="sizeRating"
                                        class="border border-gray-300 rounded-lg p-2 focus:ring-2 focus:ring-yellow-400 focus:outline-none transition duration-150 ease-in-out">
                                        <option value="" disabled>Выберите оценку</option>
                                        <option v-for="num in 5" :key="num" :value="num">{{ num }} ⭐</option>
                                    </select>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>


                <div class="bg-white shadow-lg rounded-lg p-6 mt-8">
                    <h3 class="text-2xl font-semibold mb-4">Статистика оценок</h3>
                    <canvas id="userRatingChart" class="mb-4"></canvas>
                    <canvas id="averageRatingChart"></canvas>
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
import { Chart, registerables } from 'chart.js';

Chart.register(...registerables);

export default {
    name: "ProductDiscussionPage",
    data() {
        return {
            reviews: [],
            newReview: {
                text: "",
            },
            ratings: {
                material: "",
                color: "",
                size: "",
                style: "",
                weight: "",
            },
            isDescriptionExpanded: false,
        };
    },

    mounted() {
        this.renderCharts();
    },

    methods: {
        toggleDescription() {
            this.isDescriptionExpanded = !this.isDescriptionExpanded;
        },
        submitReview() {
            if (!this.newReview.text) return;

            const newReview = {
                id: this.reviews.length + 1,
                author: "Пользователь",
                text: this.newReview.text,
                date: new Date().toLocaleString(),
            };

            this.reviews.push(newReview);
            this.newReview.text = "";
        },

        renderCharts() {
            const userRatingCtx = document.getElementById('userRatingChart').getContext('2d');
            const averageRatingCtx = document.getElementById('averageRatingChart').getContext('2d');

            const materialData = [4.5, 4.0, 4.2, 4.8, 4.6];
            const colorData = [3.0, 3.5, 4.0, 3.8, 4.2];
            const sizeData = [4.0, 4.5, 4.2, 4.3, 4.1];
            const styleData = [5.0, 4.8, 4.7, 5.0, 4.9];
            const weightData = [4.2, 4.0, 4.1, 4.3, 4.4];

            const averageRatingData = [4.2, 4.5, 4.0, 4.8, 4.6]; // Замените на реальные данные

            // График изменений оценок пользователей за последний день
            new Chart(userRatingCtx, {
                type: 'line',
                data: {
                    labels: ['Час 1', 'Час 2', 'Час 3', 'Час 4', 'Час 5'],
                    datasets: [
                        {
                            label: 'Материал',
                            data: materialData,
                            borderColor: 'rgba(255, 99, 132, 1)',
                            backgroundColor: 'rgba(255, 99, 132, 0.2)',
                            fill: true,
                        },
                        {
                            label: 'Цвет',
                            data: colorData,
                            borderColor: 'rgba(54, 162, 235, 1)',
                            backgroundColor: 'rgba(54, 162, 235, 0.2)',
                            fill: true,
                        },
                        {
                            label: 'Размер',
                            data: sizeData,
                            borderColor: 'rgba(255, 206, 86, 1)',
                            backgroundColor: 'rgba(255, 206, 86, 0.2)',
                            fill: true,
                        },
                        {
                            label: 'Стиль',
                            data: styleData,
                            borderColor: 'rgba(75, 192, 192, 1)',
                            backgroundColor: 'rgba(75, 192, 192, 0.2)',
                            fill: true,
                        },
                        {
                            label: 'Вес',
                            data: weightData,
                            borderColor: 'rgba(153, 102, 255, 1)',
                            backgroundColor: 'rgba(153, 102, 255, 0.2)',
                            fill: true,
                        }
                    ]
                },
                options: {
                    responsive: true,
                    scales: {
                        y: {
                            beginAtZero: true
                        }
                    }
                }
            });

            //График изменения средней оценки товара
            new Chart(averageRatingCtx, {
                type: 'line',
                data: {
                    labels: ['Час 1', 'Час 2', 'Час 3', 'Час 4', 'Час 5'],
                    datasets: [
                        {
                            label: 'Средняя оценка всех характеристик',
                            data: averageRatingData,
                            borderColor: 'rgba(255, 99, 132, 1)',
                            backgroundColor: 'rgba(255, 99, 132, 0.2)',
                            fill: true,
                        },
                    ]
                }
            });
        },
    },
};
</script>