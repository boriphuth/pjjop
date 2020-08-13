<?php
   $servername = "db";
   $username = "devops";
   $password = "devops101";

   $dbhandle = mysqli_connect($servername,$username,$password);
   $selected = mysqli_select_db($dbhandle, "titanic");

   echo "Hello : from cpsudevops.com<br>";
   echo "Connected database server<br>";
   echo "Selected database";
?>
