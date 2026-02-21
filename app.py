<!DOCTYPE html>
<html lang="he">
<head>
    <meta charset="UTF-8">
    <title>טופס פרטים</title>
    <style>
        body {
            direction: rtl;
            font-family: Arial, sans-serif;
            background-color: #f2f2f2;
            padding: 20px;
        }

        .container {
            background: white;
            padding: 20px;
            border-radius: 10px;
            max-width: 400px;
            margin: auto;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }

        label {
            display: block;
            margin-top: 10px;
        }

        input, select {
            width: 100%;
            padding: 8px;
            margin-top: 5px;
        }

        button {
            margin-top: 15px;
            padding: 10px;
            width: 100%;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }

        button:hover {
            background-color: #45a049;
        }

        .result {
            margin-top: 20px;
            background-color: #e7f3ff;
            padding: 15px;
            border-radius: 8px;
            display: none;
        }
    </style>
</head>
<body>

<div class="container">
    <h2>טופס פרטים</h2>

    <label>מין:</label>
    <select id="gender">
        <option value="">בחר</option>
        <option value="זכר">זכר</option>
        <option value="נקבה">נקבה</option>
    </select>

    <label>שנת לידה:</label>
    <input type="number" id="age" placeholder="הכנס שנת לידה">

    <label>שם:</label>
    <input type="text" id="firstName" placeholder="הכנס שם">

    <label>שם משפחה:</label>
    <input type="text" id="lastName" placeholder="הכנס שם משפחה">

    <button onclick="showResult()">שלח</button>

    <div class="result" id="resultBox">
        <p id="resultText"></p>
    </div>
</div>

<script>
function showResult() {
    var gender = document.getElementById("gender").value;
    var age = document.getElementById("age").value;
    var firstName = document.getElementById("firstName").value;
    var lastName = document.getElementById("lastName").value;

    var result = 
        "מין: " + gender + "<br>" +
        "שנת לידה: " + age + "<br>" +
        "שם: " + firstName + "<br>" +
        "שם משפחה: " + lastName;

    document.getElementById("resultText").innerHTML = result;
    document.getElementById("resultBox").style.display = "block";
}
</script>

</body>
</html>
