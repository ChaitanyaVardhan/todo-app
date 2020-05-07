## Rest todo app

```python
GET /todo/api/v1.0/tasks
GET /todo/api/v1.0/tasks/[task_id]
POST /todo/api/v1.0/tasks/
PUT /todo/api/v1.0/tasks/[task_id]
DELETE /todo/api/v1.0/tasks/[task_id]
```

### Task Description
1. id: unique, identifies a task
2. title: short task description, String
3. description: long task description, Text
4. done: task completion state, boolean