<?php
if(isset($_COOKIE['auth'])) {
  header('Location: index.php');
  exit();
}

if(isset($_POST['username'])) {
  $username = $_POST['username'];
  $password = $_POST['password'];
  $token = bin2hex(openssl_random_pseudo_bytes(12));
  $auth = serialize(array("username" => $username, "password" => $password, "token" => $token));
  setcookie("auth", base64_encode($auth), time() + (86400 * 30), "/");
  header("Location: index.php");
} else {
?>
<html>
<head>
  <title>Prototype</title>
  <link rel="stylesheet" href="https://cdn.simplecss.org/simple.min.css">
  <link href="//cdn.jsdelivr.net/npm/@sweetalert2/theme-dark@4/dark.css" rel="stylesheet">
  <style>
    .center {
      text-align: center;
    }
    .img {
      margin: 10px;
      margin-bottom: 15px;
    }
    :root {
      --accent: #079DB0;
    }
  </style>
</head>
<body>
  <div class=center>
    <h1>Admin Login</h1>
    <form method=post action=login.php>
      <label>Username: </label><input type=text name=username>
      <label>Password: </label><input type=password name=password><br>
      <input type=submit name=login value=Login>
    </form>
  </div>
  <script src="//cdn.jsdelivr.net/npm/sweetalert2@11/dist/sweetalert2.min.js"></script>
</body>
<?php
if(isset($_GET['error'])) {
  echo "<script>Swal.fire({
  icon: 'error',
  title: 'Oops...',
  text: 'Invalid username or password!'
})</script>";
}
}
?>
