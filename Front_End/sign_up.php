<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>Sign Up</title>
  <link href="index_style.css" rel="stylesheet" type="text/css" />
</head>

<body>

  <div class="logo">
    <hr class="horizontal" >
      <img src="Images/logo_2.jpg" alt="Logo">
  </div>
  
  
  <div class="container">
  <h2>SIGN UP</h2>
  <form action="sign_up_php.php" method="POST">
    <fieldset>
      <div class="form-group">
          <label for="username">USER ID</label>
          <input type="text" id="username" name="username"   required >
      </div>
      <div class="form-group">
          <label for="name">NAME</label>
          <input type="text" id="name" name="namee"   required >
      </div>
      <div class="form-group">
        <label for="batch">PASSING BATCH</label>
        <input type="number" id="batch" name="batch"   required >
    </div>
    <div class="form-group">
        <label for="mail">GMAIL</label>
        <input type="email" id="mail" name="mail"   required >
    </div>
      <div class="form-group">
          <label for="password">CREATE PASSWORD</label>
          <input type="password" id="password" min="8" max="32" name="password" required >
      </div>
    
        <div class="form-group">
            <button type="submit" name="Sign_Up" value="Sign Up">
              SIGN UP
            </button>
        </div>

        <div class="forgot_password">
            <a href="index.php" rel="Sign in page">
            <button type="button" id="new" >SIGN IN</button>
            </a>
        </div>
           
      </fieldset>
  </form>


  <script src="index_script.js"></script>
</body>

</html>