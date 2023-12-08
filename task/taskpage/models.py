from django.db import models

# Create your models here.
# models.py


class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    def __str__(self):
        return self.username



class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    priority = models.CharField(max_length=20, choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')])
    status = models.CharField(max_length=20, choices=[('todo', 'To Do'), ('in_progress', 'In Progress'), ('done', 'Done')])
    deadline = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to='task_images/',null=True , blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    comment_type = models.CharField(max_length=20) 
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.comment_type} - {self.task.title}"