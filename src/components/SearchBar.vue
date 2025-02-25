<script>
export default {
    name: "SearchBar",
    props: [
        'search'
    ],
    emits: ['update:search'],
    methods: {
        updateSearch(event) {
            this.$emit('update:search', event.target.value);
        }
    }
}
</script>

<template>
    <div class="search-bar">
        <input
            type="text"
            class="form-control"
            :value="search"
            @input="updateSearch"
            placeholder="Поиск задачи..."
        />
    </div>
</template>

<style scoped>
</style>
