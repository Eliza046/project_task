let host = "http://localhost:8080/api"

async function getTask() {
    let tasks = await fetch(`${host}/tasks`)
    return await tasks.json()
}

async function addTask(task) {
    task = await fetch(`${host}/tasks`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(task)
    })
    return await task.json()
}

async function updateTask(task) {
    task = await fetch(`${host}/tasks/${task.id}`, {
        method: "PATCH",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(task)
    });

    return await task.json()
}

async function deletingTask(task) {
    task = await fetch(`${host}/tasks/${task.id}`, {
        method: "DELETE",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(task)
    });

    return await task.json()
}

async function saveTask(task) {
    task = await fetch(`${host}/tasks/${task.id}`, {
        method: "GET",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(task)
    })
    return await task.json()
}

export {getTask, addTask, updateTask, deletingTask, saveTask}