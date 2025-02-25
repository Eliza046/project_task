<script>
import TaskCard from "@/components/TaskCard.vue";
import SearchBar from "@/components/SearchBar.vue";
import TaskEditor from "@/components/TaskEditor.vue";

import {addTask, getTask, updateTask, deletingTask, saveTask} from "@/api";

export default {
    name: "TaskCat",
    components: { TaskCard, SearchBar, TaskEditor },
    data() {
        return {
            searchText: "",
            tasks: [],
            isEditorVisible: false,
            editingTask: null
        };
    },
    computed: {
        filteredTasks() {
            const search = this.searchText.toLowerCase();
            return this.tasks.filter(task =>
                task.title.toLowerCase().includes(search)
            );
        }
    },
    methods: {
        async savingTask(task, is_done) {
            this.task.is_done = is_done
            return await saveTask(task)
        },
        async removeTask(task) {
            this.tasks = this.tasks.filter((t) => t.id !== task.id);
            return await deletingTask(task)
        },

        openEditor(task) {
            this.editingTask = task !== undefined ? task : null;
            this.isEditorVisible = true;
        },
        closeEditor() {
            this.isEditorVisible = false;
        },
        async saveTask(task) {
            if (task.id) {
                const index = this.tasks.findIndex(t => t.id === task.id);
                if (index !== -1) {
                    this.tasks.splice(index, 1, await updateTask(task));
                }
            } else {
                this.tasks.push(await addTask(task));
            }
            this.closeEditor();
        }
    },
    async mounted() {
        this.tasks = await getTask()
    }
};
</script>

<template>
    <div class="container my-3">
        <div class="d-flex align-items-center justify-content-between mb-3">
            <div class="flex-grow-1 me-1">
                <SearchBar v-model:search="searchText" />
            </div>


            <button class="btn btn-primary ms-3" @click="openEditor()">
                Добавить задачу
            </button>
        </div>

        <div class="row">
            <div
                class="col-12 col-sm-6 col-md-3 col-lg-2 p-1"
                v-for="task in filteredTasks"
                :key="task.id"
            >
                <TaskCard
                :task="task"
                @delete="removeTask(task)"
                @edit="openEditor(task)"
                @saving="savingTask(task)"
                class="h-100" />
            </div>
        </div>

        <div v-if="filteredTasks.length === 0" class="text-center mt-3">
            <p>Ничего не найдено</p>
        </div>

        <div
            class="modal fade show"
            v-if="isEditorVisible"
            style="display: block; background-color: rgba(0, 0, 0, 0.5);"
        >
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title">{{ editingTask ? 'Редактировать задачу' : 'Добавить задачу' }}</h5>
                        <button type="button" class="btn-close" aria-label="Закрыть" @click="closeEditor"></button>
                    </div>
                    <div class="modal-body">
                        <TaskEditor
                            :task="editingTask"
                            @save="saveTask"
                        />
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>

</style>