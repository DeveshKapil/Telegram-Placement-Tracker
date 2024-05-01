<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>Login</title>
  <link href="index_style.css" rel="stylesheet" type="text/css" />
</head>

<body>

<div class="logo">
  <hr class="horizontal">
  <img src="Images/logo_2.jpg" id="image" alt="Logo">
</div>

<div class="container">
  <h2>SIGN IN</h2>
  <form action="login.php"  method="POST">
    <fieldset>
      <div class="form-group">
        <label for="username">USERNAME</label>
        <input type="text" id="username" name="username" required>
      </div>
      <div class="form-group">
        <label for="password">PASSWORD</label>
        <input type="password" id="password" name="password" required>
      </div>
      <div class="forgot_password">
        <a href="forgot_password.html" rel="Reset Password">
          <button type="button" id="forgot">Forgot Password ?</button>
        </a>
      </div>
      <div class="form-group">
        <button type="submit" value="Login" name="Sign_In">SIGN IN</button>
      </div>
      <div class="forgot_password">
        <a href="sign_up.php" rel="Sign up page">
          <button type="button" id="new" >SIGN UP</button>
        </a>
      </div>
    </fieldset>
  </form>
</div>

<script src="index_script.js"></script>

</body>

</html>
