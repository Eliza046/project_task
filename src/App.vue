<template>
    <NavBar />
    <TaskCat />
</template>

<script>

import NavBar from "@/components/NavBar.vue";
import TaskCat from "@/components/TaskCat.vue";

export default {
    name: 'App',
    components: {TaskCat, NavBar}
}
</script>

<style>
</style>

