<?php

if(isset($_POST['Sign_Up'])){
    // Database connection
    $servername = "localhost"; // Change this to your database server
    $username = "root"; // Change this to your database username
    $password = "password"; // Change this to your database password
    $dbname = "sign_up"; // Change this to your database name

    // Create connection
    $conn = new mysqli($servername, $username, $password, $dbname);

    // Check connection
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }

    // Get form data
    $user_id = $_POST['username'];
    $namee = $_POST['namee'];
    $batch = $_POST['batch'];
    $email = $_POST['mail'];
    $password = $_POST['password'];

    // Hash the password for security
    $hashed_password = password_hash($password, PASSWORD_DEFAULT);

    // Prepare SQL statement to prevent SQL injection
    $stmt = $conn->prepare("INSERT INTO credentials (username, namee, batch, email, hashed_password) VALUES (?, ?, ?, ?, ?)");
    $stmt->bind_param("ssiss", $user_id, $namee, $batch, $email, $hashed_password);

    // Execute the prepared statement
    if ($stmt->execute() === TRUE) {
        echo '<script>window.alert("User Created Successfully."); setTimeout(function(){ window.location.href = "index.php"; },500);</script>';
        
    } else {
        echo '<script>window.alert("Error."); setTimeout(function(){ window.location.href = "sign_up.php"; },500);</script>';
    }

    $stmt->close();
    $conn->close();
}
?>