from django.shortcuts import render

def index(request):
    if request.method == "POST":
        schemaName = request.POST["schemaName"]
        tableName = request.POST["tableName"]
        numberOfColumns = int(request.POST["tableColumns"])
        fields = {}

        for i in range(numberOfColumns):
            fields[request.POST[f"columnName{i + 1}"]] = request.POST[f"fieldType{i + 1}"]

        print(schemaName)
        print(tableName)
        print(numberOfColumns)
        for x in fields:
            print(f"{x} --> {fields[x]}")

        return render(request, "index.html", context = {
            "message": "Model created successfully!"
        })
    return render(request, "index.html", context = {
        "message": "Some error occurred! Try again."
    })