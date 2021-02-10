from django.shortcuts import render
from django.db import models
from django.contrib import admin
from django.core.management import call_command
from django.db import connection
from django.urls import clear_url_caches
from importlib import import_module, reload
from django.urls import reverse
from django.conf import settings

def createModel(schemaName, tableName, fields):
    class Meta:
        pass

    setattr(Meta, "app_label", "System") # Setting up the app label
    fields['__module__'] = "System.models"
    fields['Meta'] =  Meta
    model = type(tableName, (models.Model, ), fields) # Creating the model
    call_command('makemigrations') # Making migrations
    call_command('migrate') # Migrating
    admin.site.register(model) # Registering model
    reload(import_module(settings.ROOT_URLCONF)) # Updating url
    clear_url_caches() # Clearing caches of urls since urls got updated

    return model

def index(request):
    if request.method == "POST":
        global fieldsDataTypes
        schemaName = request.POST["schemaName"]
        tableName = request.POST["tableName"]
        numberOfColumns = int(request.POST["tableColumns"])
        fields = {}

        for i in range(numberOfColumns):
            fields[request.POST[f"columnName{i + 1}"]] = fieldsDataTypes[request.POST[f"fieldType{i + 1}"]]

        model = createModel(schemaName, tableName, fields)
        
        if model:
            return render(request, "index.html", context = {
                "message": "Model created successfully!"
            })
        else:
            return render(request, "index.html", context = {
                "message": "Some error occurred! Try again."
            })
            
    return render(request, "index.html", context = {})

fieldsDataTypes = {
    "AutoF": models.AutoField(),
    "BigAutoF": models.BigAutoField(),
    "BigIntegerF": models.BigIntegerField(),
    "BinaryF": models.BinaryField(),
    "BooleanF": models.BooleanField(),
    "CharF": models.CharField(max_length = 200),
    "DateF": models.DateField(),
    "DateTimeF": models.DateTimeField(),
    "DecimalF": models.DecimalField(),
    "IntegerF": models.IntegerField(),
    "DurationF": models.DurationField(),
    "EmailF": models.EmailField(max_length = 200),
    "FileF": models.FileField(upload_to = "Uploads/Files/"),
    "FloatF": models.FloatField(),
    "ImageF": models.ImageField(upload_to = "Uploads/Images/"),
    "NullBooleanF": models.NullBooleanField(),
    "PositiveBigIntegerF": models.PositiveBigIntegerField(),
    "PositiveIntegerF": models.PositiveIntegerField(),
    "SlugF": models.SlugField(max_length = 200),
    "SmallAutoF": models.SmallAutoField(),
    "SmallIntegerF": models.SmallIntegerField(),
    "TextF": models.TextField(),
    "TimeF": models.TimeField(),
    "URLF": models.URLField(max_length=200),
    "UUIDF": models.UUIDField(),
    # "ForeignK": models.ForeignKey({model}, on_delete = models.CASCADE),
    # "ManyToManyF": models.ManyToManyField({model}),
    # "OneToOneF": models.OneToOneField({model}, on_delete = models.CASCADE),
}
