<?php

define("MAX_SIZE", 100000); // 100 kb
define("DIR", "space/");

$servername = "db";
$username = "root";
$password = "justdummypass1337";
$dbname = "into_space";

$conn = mysqli_connect($servername, $username, $password, $dbname);

if (!$conn) {
  die("Connection failed: " . mysqli_connect_error());
}

function upload_image($fp) {
  // echo var_dump($fp);
  $fname = basename($fp["name"]);
  $type = strtolower(pathinfo($fname, PATHINFO_EXTENSION));
  $name = hash("md5", $fname.time()) . "." . $type;
  $path = DIR . $name;
  $status = 1;
  $message = "";

  if($type != "jpg" && $type != "png" && $type != "jpeg") {
    $status = 0;
    $message = "Unsupported file type detected.";
    goto end;
  }

  if($fp["size"] > MAX_SIZE) {
    $status = 0;
    $message = "File is too large.";
    goto end;
  }

  if(getimagesize($fp["tmp_name"]) == false) {
    $status = 0;
    $message = "Not an image file.";
  }

  end:
  if ($status == 0) {
    return "ERROR: " . $message;
  } else {
    $x = insert($name);
    if (move_uploaded_file($fp["tmp_name"], $path) && $x === true) {
      return "File ". $name ." uploaded.";
    } else {
      return "If this happen, report to problem setter.".$x;
    }
  }
}

function insert($filename) {
  global $conn;
  $sql = "INSERT INTO images (filename, upload_date) VALUES ('".$filename."', CURDATE())";
  if($conn->query($sql)) {
    return true;
  } else {
    return $conn->error;
  }
}

function list_uploaded() {
  global $conn;
  $sql = "SELECT id, filename, upload_date FROM images";
  $result = $conn->query($sql);
  return $result;
}

function view_image($id) {
  global $conn;
  $id = base64_decode($id);
  $sql = "SELECT filename, upload_date FROM images WHERE id = ".$id;
  $result = $conn->query($sql);
  return $result;
}

?>
<html>
<head>
  <title>into-space</title>
  <link rel="stylesheet" href="https://cdn.simplecss.org/simple.min.css">
  <style>
  .center {
      text-align: center;
  }
  .img {
      margin-bottom: 25px;
  }
  :root {
      --accent: #4B07D3;
  }
  .custom-file-upload {
    border: 1px solid #4B07D3;
    border-radius: 0.3rem;
    display: inline-block;
    padding: 8px 12px;
    cursor: pointer;
  }
  input[type="file"] {
    display: none;
  }
  table {
      table-layout: fixed;
    }
  tr, td, th {
    border: 0px;
    border-bottom: 2px solid #4B07D3;
  }
  .fid {
    width: 70px;
  }
  .fname {
    width: 380px;
  }
  .fdate {
    width: 150px;
  }
  .faction {
    width: 55px;
  }
  </style>
</head>
<body>
  <script>
  function uploadFile(target) {
    document.getElementById("filename").innerHTML = target.files[0].name;
  }
  </script>
  <div class=center>
  <h1>into-space</h1>
  <div style="height: 350px">
    <img id=img class=img src="space/space.gif" style="max-height: 100%; max-width: 100%"><br>
  </div>
  <p>[ <a href=?upload>Upload</a> ] - [ <a href=?list>List</a> ]</p>
    <?php
    if(isset($_GET['upload'])) {
    ?>
    <form method="post" enctype="multipart/form-data">
      <p>Upload your image to space (max: 100 kB)</p>
      <label class="custom-file-upload">
        <input type="file" name="upload" onchange="uploadFile(this)">
        <text id=filename>No File Choose</text>
      </label>
      <input type="submit" value="Upload Image" name="submit">
      <p><?php
      if(isset($_POST['submit'])) {
	//echo var_dump($_FILES["upload"]);
	$fp = $_FILES["upload"];      
	echo upload_image($fp);
      }
    ?></p>
    </form>
    <?php
    } elseif(isset($_GET['list'])) {
    ?>
    <table class=border>
      <tr>
        <th class=fid>File ID</th>
        <th class=fname>Filename</th>
        <th class=fdate>Upload Date</th>
        <th class=faction>Action</th>
      </tr>
      <?php
      $list = list_uploaded();
      if($list->num_rows > 0) {
        while($row = $list->fetch_assoc()) {
      echo "<tr>
        <td>".$row['id']."</td>
        <td>".$row['filename']."</td>
        <td>".$row['upload_date']."</td>
        <td><a href=?view=".base64_encode($row['id']).">View</a></td>
      </tr>";
        }
      }
      ?>
    </table>
    <?php
    } elseif(isset($_GET['view'])) {
      $data = view_image($_GET['view']);
      $data = $data->fetch_row();
      echo "
    ".$data[0]." (".$data[1].")
    <script>
    document.getElementById('img').src='space/".$data[0]."';
    </script>";
    }
    ?>
  </div>
</body>
</html>
