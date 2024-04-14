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
    echo "Retry";
}

// Get form data
$username = $_POST['username'];
$password = $_POST['password'];

// Prepare SQL statement to prevent SQL injection
$stmt = $conn->prepare("SELECT id, username, password FROM users WHERE username=?");
$stmt->bind_param("s", $username);
$stmt->execute();
$result = $stmt->get_result();

if ($result->num_rows == 1) {
    $row = $result->fetch_assoc();
    $hashed_password = $row['password'];
    
    // Verify password
    if (password_verify($password, $hashed_password)) {
        // Password is correct
        session_start();
        $_SESSION['username'] = $row['username'];
        $_SESSION['user_id'] = $row['id'];
        header("home.html"); // Redirect to welcome page
    } else {
        // Password is incorrect
        echo "Incorrect password.";
    }
} else {
    // User not found
    echo "Invalid user.";
}

$stmt->close();
$conn->close();
?>
