from django.shortcuts import render
from django.db import models
from django.contrib import admin

def createModel(schemaName, tableName, numberOfColumns, fields):
    class Meta:
        pass

    setattr(Meta, "app_label", "System")

    fields = {'__module__': "", 'Meta': Meta}
    model =  type(tableName, (models.Model, ), fields)
    admin.site.register(model)
    print(model)

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

        print(schemaName)
        print(tableName)
        print(numberOfColumns)
        createModel(schemaName, tableName, numberOfColumns, fields)

        for x in fields:
            print(f"{x} --> {fields[x]}")

        return render(request, "index.html", context = {
            "message": "Model created successfully!"
        })
    return render(request, "index.html", context = {
        "message": "Some error occurred! Try again."
    })

fieldsDataTypes = {
    "AutoF": "models.AutoField()",
    "BigAutoF": "models.BigAutoField()",
    "BigIntegerF": "models.BigIntegerField()",
    "BinaryF": "models.BinaryField()",
    "BooleanF": "models.BooleanField()",
    "CharF": "models.CharField(max_length = 200)",
    "DateF": "models.DateField()",
    "DateTimeF": "models.DateTimeField()",
    "DecimalF": "models.DecimalField()",
    "IntegerF": "models.IntegerField()",
    "DurationF": "models.DurationField()",
    "EmailF": "models.EmailField(max_length = 200)",
    "FileF": "models.FileField(upload_to = Uploads/Files/)",
    "FloatF": "models.FloatField()",
    "ImageF": "models.ImageField(upload_to = Uploads/Images/)",
    "NullBooleanF": "models.NullBooleanField()",
    "PositiveBigIntegerF": "models.PositiveBigIntegerField()",
    "PositiveIntegerF": "models.PositiveIntegerField()",
    "SlugF": "models.(max_length = 200)",
    "SmallAutoF": "models.SmallAutoField()",
    "SmallIntegerF": "models.SmallIntegerField()",
    "TextF": "models.TextField()",
    "TimeF": "models.TimeField()",
    "URLF": "models.URLField(max_length=200)",
    "UUIDF": "models.UUIDField()",
    "ForeignK": "models.ForeignKey(on_delete = models.CASCADE)",
    "ManyToManyF": "models.ManyToManyField()",
    "OneToOneF": "models.OneToOneField(on_delete = models.CASCADE)",
}


    
    # <option value="AutoF">AutoField</option>
    # <option value="BigAutoF">BigAutoField</option>
    # <option value="BigIntegerF">BigIntegerField</option>
    # <option value="BinaryF">BinaryField</option>
    # <option value="BooleanF">BooleanField</option>
    # <option value="CharF">CharField</option>
    # <option value="DateF">DateField</option>
    # <option value="DateTimeF">DateTimeField</option>
    # <option value="DecimalF">DecimalField</option>
    # <option value="IntegerF">IntegerField</option>
    # <option value="DurationF">DurationField</option>
    # <option value="EmailF">EmailField</option>
    # <option value="FileF">FileField</option>
    # <option value="FloatF">FloatField</option>
    # <option value="ImageF">ImageField</option>
    # <option value="NullBooleanF">NullBooleanField</option>
    # <option value="PositiveBigIntegerF">PositiveBigIntegerField</option>
    # <option value="PositiveIntegerF">PositiveIntegerField</option>
    # <option value="SlugF">SlugField</option>
    # <option value="SmallAutoF">SmallAutoField</option>
    # <option value="SmallIntegerF">SmallIntegerField</option>
    # <option value="TextF">TextField</option>
    # <option value="TimeF">TimeField</option>
    # <option value="URLF">URLField</option>
    # <option value="UUIDF">UUIDField</option>
    # <option value="ForeignK">ForeignKey</option>
    # <option value="ManyToManyF">ManyToManyField</option>
    # <option value="OneToOneF">OneToOneField</option>