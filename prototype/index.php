<?php
include("flag.php");

if(!isset($_COOKIE['auth'])) {
  header('Location: login.php');
  exit();
}

$token = bin2hex(openssl_random_pseudo_bytes(12));
$auth = unserialize(base64_decode($_COOKIE['auth']));

if($auth['username'] == "admin" && $auth['password'] == "secret") {
  if($auth['token'] == $token) {
    echo FLAG;
  } else {
    echo "You are an admin but no flag for you.";
  }
} else {
  setcookie("auth", FALSE, -1, "/");
  header("Location: login.php?error");
  exit();
}

?>
