<!DOCTYPE html>
<?php
require('Connection.php');
 ?>
<html lang="en">
<head>
	<title>تسجيل دخول</title>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<link rel="icon" href="eyfadLogo.png">

<!--===============================================================================================-->
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="vendor/bootstrap/css/bootstrap.min.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="fonts/font-awesome-4.7.0/css/font-awesome.min.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="fonts/Linearicons-Free-v1.0.0/icon-font.min.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="vendor/animate/animate.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="vendor/css-hamburgers/hamburgers.min.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="vendor/animsition/css/animsition.min.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="vendor/select2/select2.min.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="vendor/daterangepicker/daterangepicker.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="css/utillog.css">
	<link rel="stylesheet" type="text/css" href="css/mainlog.css">

<!--===============================================================================================-->

    <!-- Site Icons -->
    <link rel="shortcut icon" href="images/logoicon.ico" type="image/x-icon" />
    <link rel="apple-touch-icon" href="images/apple-touch-icon.png">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="css/bootstrap.min.css">
    <!-- Site CSS -->
    <link rel="stylesheet" href="style.css">
    <!-- Responsive CSS -->
    <link rel="stylesheet" href="css/responsive.css">
    <!-- Custom CSS -->
    <link rel="stylesheet" href="css/custom.css">
	<script src="js/modernizr.js"></script> <!-- Modernizr -->

    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
	  <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
	<![endif]-->
	
  <!-- Font Awesome -->
  <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.8.2/css/all.css">
  <!-- Google Fonts -->
  <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap">
  <!-- Bootstrap core CSS -->
  <link href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.5.0/css/bootstrap.min.css" rel="stylesheet">
  <!-- Material Design Bootstrap -->
  <link href="https://cdnjs.cloudflare.com/ajax/libs/mdbootstrap/4.19.0/css/mdb.min.css" rel="stylesheet">

<!-- For motion word-->
<link href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.0/css/bootstrap.min.css" rel="stylesheet" id="bootstrap-css">
<script src="//maxcdn.bootstrapcdn.com/bootstrap/3.3.0/js/bootstrap.min.js"></script>
<script src="//code.jquery.com/jquery-1.11.1.min.js"></script>
<style>
	body {
  text-align: center;
 
}

</style>
</head>
	<body id="page-top" class="politics_version">

    <nav  style="justify-content: flex-start; "class="navbar navbar-expand-sm navbar-dark">

	<a ><img src="eyfadLogo.png" alt="logo" height="150" width="150" /> </a>
	  </nav>
	  <script>
		  var TxtType = function(el, toRotate, period) {
        this.toRotate = toRotate;
        this.el = el;
        this.loopNum = 0;
        this.period = parseInt(period, 10) || 2000;
        this.txt = '';
        this.tick();
        this.isDeleting = false;
    };

    TxtType.prototype.tick = function() {
        var i = this.loopNum % this.toRotate.length;
        var fullTxt = this.toRotate[i];

        if (this.isDeleting) {
        this.txt = fullTxt.substring(0, this.txt.length - 1);
        } else {
        this.txt = fullTxt.substring(0, this.txt.length + 1);
        }

        this.el.innerHTML = '<span class="wrap">'+this.txt+'</span>';

        var that = this;
        var delta = 200 - Math.random() * 100;

        if (this.isDeleting) { delta /= 2; }

        if (!this.isDeleting && this.txt === fullTxt) {
        delta = this.period;
        this.isDeleting = true;
        } else if (this.isDeleting && this.txt === '') {
        this.isDeleting = false;
        this.loopNum++;
        delta = 500;
        }

        setTimeout(function() {
        that.tick();
        }, delta);
    };

    window.onload = function() {
        var elements = document.getElementsByClassName('typewrite');
        for (var i=0; i<elements.length; i++) {
            var toRotate = elements[i].getAttribute('data-type');
            var period = elements[i].getAttribute('data-period');
            if (toRotate) {
              new TxtType(elements[i], JSON.parse(toRotate), period);
            }
        }
        // INJECT CSS
        var css = document.createElement("style");
        css.type = "text/css";
        css.innerHTML = ".typewrite > .wrap { border-right: 0.08em solid #fff}";
        document.body.appendChild(css);
    };
	  </script>

<section id="home"  style="background: url('images/header.png')">

<h1>
  <a style="color:#fff; text-decoration: none; font-size:50px;"href="" class="typewrite" data-period="2000" data-type='[ "مرحباً بكم في منصة إيفاد", "ساهم معنا في إثراء المحتوى العربي", "كن أوائل المشاركين في المبادرة", "سجل معنا" ]'>
    <span class="wrap"></span>
  </a>
</h1>
		
		<main style="display: flex; justify-content: flex-start; padding-left:40px;">
	
        <img src="robotW.png" class="animated bounce infinite" alt="Eyfad Logo" id="animated-img1" width="150" height="150">
       
	  </main>
	  

	

</section>

	  
<div class="limiter">

<div class="container-login100">
	<div class="wrap-login100">
		<div class="login100-form-title" style="background-image: url('images/header.png');">
			<span class="login100-form-title-1">

			</span>
		</div>
 <div class="login">

	<form  action="new2.php" method="post" style="text-align:right; align-items:right;" class="login100-form validate-form">

			<div style="text-align:right; align-items:right;" class="wrap-input100 validate-input m-b-26" data-validate="Username is required">
				<span style="font-size:20px;">اسم المستخدم 		</span>

				<input style="text-align:right;font-size:16px;" class="input100" type="text" name="username" placeholder="ادخل اسم المستخدم" required>


				<span class="focus-input100"></span>
			</div>




			<div class="wrap-input100 validate-input m-b-18" data-validate = "Password is required">
				<span style="font-size:20px;">الرقم السري</span>
				<input style="text-align:right;font-size:16px;" class="input100" type="password" name="pass" placeholder="ادخل الرقم السري" required>
				<span class="focus-input100"></span>
			</div>


		</br></br></br>

			<div style="padding-left:230px;padding-top:20px;" class="container-login100-form-btn">
				<button style="  background-image: linear-gradient(to top, #19fcb8 0%, #35d0ba 100%);
"class="login100-form-btn" type ="submit" name="submit" value ="Submit"  style="background-color:#90A4AE">  <!-- add name and type and value -->
				تسجيل الدخول
				</button>

			</div>
			</br></br></br>
			</br></br></br>
			<div style="text-align:right; align-items:right;" class="wrap-input100 validate-input m-b-26">
				<p style="font-size:20px;text-align:right;align:right;font-size:16px;">مستخدم جديد؟	</p>
                <a href="https://docs.google.com/forms/d/e/1FAIpQLSc7V7jop5WEFSbkbzrDuKgHFyyVwsbxG7iHFa9-mz8u22wKcg/viewform">سجل هنا</a>
			</div>
		</form>
	</div>
</div>

</div>
</div>

<!--===============================================================================================-->
	<script src="vendor/jquery/jquery-3.2.1.min.js"></script>
<!--===============================================================================================-->
	<script src="vendor/animsition/js/animsition.min.js"></script>
<!--===============================================================================================-->
	<script src="vendor/bootstrap/js/popper.js"></script>
	<script src="vendor/bootstrap/js/bootstrap.min.js"></script>
<!--===============================================================================================-->
	<script src="vendor/select2/select2.min.js"></script>
<!--===============================================================================================-->
	<script src="vendor/daterangepicker/moment.min.js"></script>
	<script src="vendor/daterangepicker/daterangepicker.js"></script>
<!--===============================================================================================-->
	<script src="vendor/countdowntime/countdowntime.js"></script>
<!--===============================================================================================-->
	<script src="js/main.js"></script>


</body>
</html>
