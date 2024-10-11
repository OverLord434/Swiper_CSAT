<template>
    <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6 max-h-[800px] overflow-y-auto">
        <div  v-for="product in products" :key="product.id_product" class="bg-white rounded-lg shadow-lg overflow-hidden">
            <img  alt="Изображение товара" class="w-full h-64 object-cover" />
            <div class="p-4">
                <h2 class="text-lg font-semibold mb-2">{{ product.name }}</h2>
                <div class="flex items-center mt-2 mb-[20px]">
                    <span class="text-xl text-yellow-500 font-semibold"> {{ product.average_rating.toFixed(1) }} ⭐️</span>
                    <p class="text-gray-600 text-sm ml-2">Средняя оценка</p>
                </div>
                <router-link to="/product" class="inline-block bg-yellow-400 text-white rounded-lg py-2 px-4 hover:bg-yellow-500 transition">Перейти</router-link>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            products: [],
        };
    },
    mounted() {
        this.fetchProducts();
    },
    watch: {
        '$route.query.query': 'fetchProducts',
    },
    methods: {
        fetchProducts() {
            const query = this.$route.query.query || '';
            axios
                .get(`http://127.0.0.1:8000/main/api/products/search/?query=${encodeURIComponent(query)}`)
                .then((response) => {
                    this.products = response.data;
                })
                .catch((error) => {
                    console.error('Ошибка при получении продуктов:', error);
                });
        },
    },
};
</script>