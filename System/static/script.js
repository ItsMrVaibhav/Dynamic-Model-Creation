var fields = document.querySelector(".Fields");
var addColumnButton = document.querySelector(".Add-Column-Button");
var fieldCount = 1;
var messageCross = document.querySelector("#Message img");
var message = document.querySelector("#Message");

messageCross.onclick = function() {
    message.remove();
};

addColumnButton.onclick = function(event) {
    event.preventDefault();
    var fieldHTML = `<div class="Field">
    <label class="Label">Column Name</label>
    <input type="text" name="columnName${fieldCount}" placeholder="Enter the column name" class="Input-Field"></input>
    <label class="Label">Field Type</label>
    <select class="Field-Type" name="fieldType${fieldCount}">
        <option value="C">Char</option>
        <option value="FF">FileField</option>
        <option value="IF">ImageField</option>
        <option value="IF2">ImageField</option>
    </select>
</div>`;
    fieldCount++;
    fields.insertAdjacentHTML("beforeend", fieldHTML);
};
