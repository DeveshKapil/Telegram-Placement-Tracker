<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>Home</title>
  <link href="home.css" rel="stylesheet" type="text/css" />
</head>

<body>
  <?php
  session_start();
  $totalSize = 0;

  // Iterate through session variables
  foreach ($_SESSION as $key => $value) {
      // Calculate the size of each session variable
      $totalSize += strlen($key) + strlen(serialize($value));
  }
  if($totalSize == 0)
  {
    session_destroy();
    echo '<script>window.alert("Invalid Session."); setTimeout(function(){ window.location.href = "index.php"; });</script>';
  }
  ?>

  <aside id="<?php echo isset($_SESSION['batch'])? $_SESSION['batch'] : '' ;  ?>"></aside>
  
  <div class="logo">
    <hr class="horizontal">
    <div id="logo-content">
    <img src="Images/logo_2.jpg" alt="Logo">
    <button id="new" type="button" onclick="log_out()">LOG OUT</button>
    </div>
  </div>  
       
  <div id="parent">
    
  </div>
  <script src="apicall.js"></script>
</body>

</html>