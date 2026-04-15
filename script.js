/* 
    BUG NOTES (for demonstration):
    1) "historyList" is declared without let/const, making it a global variable.
    2) Off-by-one bug in toggleImportantTask with "index - 1".
    3) Add important task does nothing if the input is empty, 
       but does not alert or show any error (inconsistent with regular tasks).
    4) Potential concurrency issue if save and retrieve are called simultaneously.
*/

// Arrays for tasks
let taskList = [];
let importantTaskList = [];
historyList = []; // Accidental global variable

window.onload = function() {
    // Load tasks from localStorage on page load
    retrieveTasksFromLocalStorage();
    renderTasks();
    renderImportantTasks();
    renderArchive();
};

// -----------------------------
// Task Functions
// -----------------------------
function addTask() {
    const taskInput = document.getElementById('taskInput');
    const task = taskInput.value.trim();

    if (task === '') {
        alert('Please enter a task.');
        return;
    }

    taskList.push({ text: task, completed: false });
    taskInput.value = '';
    renderTasks();
    saveTasksToLocalStorage();
}

function toggleTask(index) {
    taskList[index].completed = !taskList[index].completed;
    renderTasks();
    saveTasksToLocalStorage();
}

function deleteTask(index) {
    taskList.splice(index, 1);
    renderTasks();
    saveTasksToLocalStorage();
}

/**
 * Archive completed tasks
 * Visible bug: If no tasks are completed, pressing "Archive Completed Tasks"
 * might do something unexpected (or do nothing in a confusing way).
 */
function archiveCompleted() {
    const completedTasks = taskList.filter(task => task.completed);

    // Move completed tasks to history array
    historyList = historyList.concat(completedTasks);

    // Remove completed tasks from current list
    taskList = taskList.filter(task => !task.completed);

    renderTasks();
    renderArchive();
    saveTasksToLocalStorage();
}

// Renders the current tasks in the "Regular Tasks" section
function renderTasks() {
    const taskListElement = document.getElementById('taskList');
    taskListElement.innerHTML = '';

    taskList.forEach((task, index) => {
        const li = document.createElement('li');
        li.className = task.completed ? 'completed' : '';
        li.innerHTML = `
            <span onclick="toggleTask(${index})">${task.text}</span>
            <button class="delete" onclick="deleteTask(${index})">Delete</button>
        `;
        taskListElement.appendChild(li);
    });
}

// -----------------------------
// Important Task Functions
// -----------------------------
function addImportantTask() {
    const taskInput = document.getElementById('importantTaskInput');
    const task = taskInput.value.trim();

    // BUG: No alert or message if empty
    if (task === '') {
        // Not returning or alerting => inconsistency
        return; 
    }

    importantTaskList.push({ text: task, completed: false });
    taskInput.value = '';
    renderImportantTasks();
    saveTasksToLocalStorage();
}

function toggleImportantTask(index) {
    // BUG: Off-by-one error, mistakenly uses index - 1
    importantTaskList[index - 1].completed = !importantTaskList[index - 1].completed;
    renderImportantTasks();
    saveTasksToLocalStorage();
}

function deleteImportantTask(index) {
    importantTaskList.splice(index, 1);
    renderImportantTasks();
    saveTasksToLocalStorage();
}

function renderImportantTasks() {
    const listElement = document.getElementById('importantTaskList');
    listElement.innerHTML = '';

    importantTaskList.forEach((task, index) => {
        const li = document.createElement('li');
        li.className = task.completed ? 'completed' : '';
        li.innerHTML = `
            <span onclick="toggleImportantTask(${index})">${task.text}</span>
            <button class="delete" onclick="deleteImportantTask(${index})">Delete</button>
        `;
        listElement.appendChild(li);
    });
}

// -----------------------------
// Archive / History
// -----------------------------
function renderArchive() {
    const archiveListElement = document.getElementById('archiveList');
    archiveListElement.innerHTML = '';

    historyList.forEach(task => {
        const li = document.createElement('li');
        li.className = task.completed ? 'completed' : '';
        li.textContent = task.text;
        archiveListElement.appendChild(li);
    });
}

// -----------------------------
// Local Storage (JSON) Functions
// -----------------------------
function saveTasksToLocalStorage() {
    // Potential concurrency bug if called multiple times simultaneously
    const data = {
        tasks: taskList,
        important: importantTaskList,
        history: historyList
    };
    localStorage.setItem('todoData', JSON.stringify(data));
}

function retrieveTasksFromLocalStorage() {
    const savedData = localStorage.getItem('todoData');
    if (savedData) {
        try {
            const parsed = JSON.parse(savedData);
            taskList = parsed.tasks || [];
            importantTaskList = parsed.important || [];
            historyList = parsed.history || [];
        } catch (e) {
            // If JSON is corrupted, do nothing or handle error
            console.warn('Data in localStorage is invalid JSON');
        }
    }
}
