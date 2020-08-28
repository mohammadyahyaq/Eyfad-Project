<!DOCTYPE html>
<?php
require('Connection.php');
?>
<html>
	<head>
		<meta charset="utf-8">
		<title>Login</title>
	</head>
	<body style="background: url('images/template.png')" >
<?php

      function check_ID_Pass(){
          require('Connection.php');
        $username = $_POST['username'];
        $password = $_POST['pass'];
      if(is_numeric($username)){
        $table="volunteer";
        $page="volunteer.php";
        $id="volunteerID";
        $pass="volunteerPass";
      }else{
        $table="supervisor";
        $page="supervisor.php";
        $id="supervisorID";
        $pass="supervisorPass";
      }
                 $sql_log_in = "SELECT * FROM $table WHERE $id = '$username' AND $pass ='$password'";
                 $stmt_log_in = $conn->prepare($sql_log_in);
                 $stmt_log_in->execute();
                 $row = $stmt_log_in->fetch();
                 if($row!=null) {

 									  	$myfile = fopen("id.txt", "w") or die("Unable to open file!");
 						         fwrite($myfile, $username);
 						         fclose($myfile);
                     header("Location: $page");
                     exit();
                 }
                 else {
                   $message = "اسم المستخدم او كلمة المرور خاطئة";
                   echo "<script>
                   alert('$message');
                   window.location.href= 'login.php';
                   </script>";
                 }
      }
check_ID_Pass();
        ?>
	</body>
</html>
