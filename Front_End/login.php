<?php

session_start();

if(isset($_POST['Sign_In'])){
    // Database connection
    $servername = "localhost";
    $username = "root";
    $password = "password";
    $dbname = "sign_up";

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
    // $stmt = $conn->prepare("SELECT id, username, password FROM users WHERE username=?");
    // $stmt->bind_param("s", $username);
    // $stmt->execute();
    // $result = $stmt->get_result();

    try {
      // Prepare the SQL statement
      $stmt = $conn->prepare("SELECT username, batch , hashed_password FROM credentials WHERE username=?");
      
      // Check if the statement was prepared successfully
      if (!$stmt) {
          throw new Exception("Error preparing statement: " . $conn->error);
      }
      
      // Bind parameters
      $stmt->bind_param("s", $username);
      
      // Execute the statement
      $stmt->execute();
      
      // Fetch results
      $result = $stmt->get_result();
      
      if ($result->num_rows == 1) {
        $row = $result->fetch_assoc();
        $hashed_password = $row['hashed_password'];
        
        // Verify password
        if (password_verify($password, $hashed_password)) {
            // Password is correct
            echo "Signing IN";
            $_SESSION['username'] = $row['username'];
            $user_id = $_SESSION['username'];
            $_SESSION['user_id'] = $row['id'];
            $_SESSION['batch'] = $row['batch'];

            header("Location: home.php"); // Redirect to welcome page
        } 
        else {
          // Password is incorrect
          session_destroy();
          echo '<script>window.alert("Incorrect Password."); setTimeout(function(){ window.location.href = "index.php"; },500);</script>';
        }
      } else {
        // User not found
        session_destroy();
        echo '<script>window.alert("Incorrect Password."); setTimeout(function(){ window.location.href = "index.php"; },500);</script>';
    }

      $stmt->close();
      $conn->close();
      
    } catch (Exception $e) {
      // Handle the exception
      echo "Error: " . $e->getMessage();
    }
}
?>