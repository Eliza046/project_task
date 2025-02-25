<script>
export default {
    name: "TaskCard",
    props: [
        'task'
    ],
    methods: {
        editTask() {
            this.$emit('edit', this.task);
        },
        deleteTask() {
            this.$emit('delete', this.task);
        },
        saveDone(is_done) {

            this.$emit('saving', this.task, is_done)
        }
    }
}
</script>

<template>
    <div class="card position-relative">
        <button
            class="btn btn-sm btn-light position-absolute top-0 end-0 m-2"
            @click="editTask"
            aria-label="Редактировать"
        >
            <i class="bi bi-pencil"></i>
        </button>

        <button
            class="btn btn-sm btn-light position-absolute top-0 end-0 m-2"
            @click="deleteTask"
            aria-label="Удалить"
        >
            <i class="bi bi-pencil"></i>
        </button>

        <div class="card-body">
            <input type="checkbox" v-model="is_done" @click="saveDone(is_done)"/>
            <span class="card-title" v-if="!is_done"><h5>{{ task.title }}</h5></span>
            <span class="card-title" v-else style="text-decoration: line-through"><h5>{{ task.title }}</h5></span>

        </div>
    </div>
</template>

<style scoped>
.btn-light {
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.card {
    overflow: hidden;
}
</style>