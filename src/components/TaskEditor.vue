<script>
export default {
    name: "TaskEditor",
    props: {
        task: {
            type: Object
        }
    },
    data() {
        return {
            localTask: this.task || {
                title: "",
                is_done: false
            },
        };
    },
    methods: {
        saveTask() {
            this.$emit("save", { ...this.localTask });
            this.resetForm();
        },
        resetForm() {
            this.localTask = {
                title: "",
                is_done: false
            };
        }
    },
    watch: {
        task(newTask) {
            this.localTask = { ...newTask };
        }
    }
};
</script>

<template>
    <div class="task-editor">
        <form @submit.prevent="saveTask">
            <!-- Имя артиста -->
            <div class="mb-3">
                <label for="task-title" class="form-label">Задача</label>
                <textarea
                    id="task-title"
                    v-model="localTask.title"
                    type="text"
                    class="form-control"
                    placeholder="Введите задачу"
                    required
                ></textarea>
            </div>

            <!-- Описание артиста -->


            <!-- Кнопки -->
            <div class="d-flex justify-content-between">
                <button type="submit" class="btn btn-success">Сохранить</button>
                <button type="button" class="btn btn-secondary" @click="resetForm">Очистить</button>
            </div>
        </form>
    </div>
</template>

<style scoped>
</style>