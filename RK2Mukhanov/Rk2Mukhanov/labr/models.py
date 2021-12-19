from django.db import models


class myFile(models.Model):
    id = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    size = models.IntegerField(max_length=50)


class myDirectory:
    id = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    file = models.ForeignKey(myFile, on_delete=models.CASCADE)
    def __str__(self):
        return self.name


files = [
    myFile (1, 'Dz', 200, 1),
    myFile (2, 'Elteh', 700, 2),
    myFile (3, 'Proga', 500, 3),
    myFile(4, 'Lab1', 400, 3),
    myFile(5, 'Config', 300, 3),
]

directoties = [
    myDirectory(1, 'Labs'),
    myDirectory(2, 'dir'),
    myDirectory(3, 'Univer'),
    myDirectory(11, 'Work'),
    myDirectory(22, 'Fun'),
    myDirectory(33, 'Secret'),
]
