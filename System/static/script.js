var fields = document.querySelector(".Fields");
var addColumnButton = document.querySelector(".Add-Column-Button");
var fieldCount;
var messageCross = document.querySelector("#Message img");
var message = document.querySelector("#Message");
var numberOfColumns = document.getElementById("Number-Of-Columns");
var fieldCrosses;
var firstTime = true;

function eliminateField() {
    this.parentNode.remove();
    numberOfColumns.value--;
}

function removeMessage() {
    message.remove();
};

addColumnButton.onclick = function(event) {
    if (firstTime) {
        for (var i = 0 ; i < numberOfColumns.value ; i++) {
            var fieldHTML = `<div class="Field">
                <img class="Field-Cross" src="../static/Cross.png" alt="">
                <label class="Label">Column Name</label>
                <input type="text" name="columnName${i}" placeholder="Enter the column name" class="Input-Field"></input>
                <label class="Label">Field Type</label>
                <select class="Field-Type" name="fieldType${i}">
                    <option value="BigIntegerF">BigIntegerField</option>
                    <option value="BinaryF">BinaryField</option>
                    <option value="BooleanF">BooleanField</option>
                    <option value="CharF">CharField</option>
                    <option value="DateF">DateField</option>
                    <option value="DateTimeF">DateTimeField</option>
                    <option value="DecimalF">DecimalField</option>
                    <option value="IntegerF">IntegerField</option>
                    <option value="EmailF">EmailField</option>
                    <option value="PositiveBigIntegerF">PositiveBigIntegerField</option>
                    <option value="PositiveIntegerF">PositiveIntegerField</option>
                    <option value="SlugF">SlugField</option>
                    <option value="SmallIntegerF">SmallIntegerField</option>
                    <option value="TextF">TextField</option>
                </select>
            </div>`;
            fields.insertAdjacentHTML("beforeend", fieldHTML);
        }

        firstTime = false;
        fieldCount = numberOfColumns;
    } else {
        numberOfColumns.value++;
        var fieldHTML = `<div class="Field">
        <img class="Field-Cross" src="../static/Cross.png" alt="">
        <label class="Label">Column Name</label>
        <input type="text" name="columnName${fieldCount}" placeholder="Enter the column name" class="Input-Field"></input>
        <label class="Label">Field Type</label>
        <select class="Field-Type" name="fieldType${fieldCount}">
        <option value="BigIntegerF">BigIntegerField</option>
        <option value="BinaryF">BinaryField</option>
        <option value="BooleanF">BooleanField</option>
        <option value="CharF">CharField</option>
        <option value="DateF">DateField</option>
        <option value="DateTimeF">DateTimeField</option>
        <option value="DecimalF">DecimalField</option>
        <option value="IntegerF">IntegerField</option>
        <option value="EmailF">EmailField</option>
        <option value="PositiveBigIntegerF">PositiveBigIntegerField</option>
        <option value="PositiveIntegerF">PositiveIntegerField</option>
        <option value="SlugF">SlugField</option>
        <option value="SmallIntegerF">SmallIntegerField</option>
        <option value="TextF">TextField</option>
        </select>
    </div>`;
    fieldCount++;
    fields.insertAdjacentHTML("beforeend", fieldHTML);
    }

    fieldCrosses = document.querySelectorAll(".Field-Cross");

    for (var i = 0 ; i < fieldCrosses.length ; i++)
        fieldCrosses[i].addEventListener("click", eliminateField);
};
