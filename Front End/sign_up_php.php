<?php
// Database connection
$servername = "localhost"; // Change this to your database server
$username = "username"; // Change this to your database username
$password = "password"; // Change this to your database password
$dbname = "database"; // Change this to your database name

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Get form data
$user_id = $_POST['username'];
$name = $_POST['name'];
$semester = $_POST['semester'];
$email = $_POST['mail'];
$password = $_POST['password'];

// Hash the password for security
$hashed_password = password_hash($password, PASSWORD_DEFAULT);

// Prepare SQL statement to prevent SQL injection
$stmt = $conn->prepare("INSERT INTO users (user_id, name, semester, email, password) VALUES (?, ?, ?, ?, ?)");
$stmt->bind_param("ssiss", $user_id, $name, $semester, $email, $hashed_password);

// Execute the prepared statement
if ($stmt->execute() === TRUE) {
    echo "User created successfully";
    header("index.html");
} else {
    echo "Error: " . $stmt->error;
}

$stmt->close();
$conn->close();
?>
