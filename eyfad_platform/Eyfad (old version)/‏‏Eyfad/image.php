<?php
 $connect = mysqli_connect("localhost", "root", "", "test_upload_image");
 //require('Connection.php');
 if(isset($_POST["insert"]))
 {
      $file = addslashes(file_get_contents($_FILES["image"]["tmp_name"]));
	  $volunteerID=$_POST["volunteerID"];
	  
      $query = "INSERT INTO image VALUES ('','$volunteerID','$file');";
      if(mysqli_query($connect, $query))
      {
           echo '<script>alert("Image Inserted into Database")</script>';
      }
 }
 ?>
 <!DOCTYPE html>
 <html>
      <head>
        <meta charset="UTF-8">
           <title>رفع الصور</title>
           <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.2.0/jquery.min.js"></script>
           <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" />
           <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>
           <meta charset="UTF-8">
           <meta name="viewport" content="width=device-width, initial-scale=1">
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
      </head>
      <body>


        	<!-- ملاحظة: اضفنا الهيدر-->
        	<!-- Navigation -->
          <nav class="navbar navbar-expand-lg navbar-dark fixed-top" id="mainNav">
        		<div class="container">
        			<a class="navbar-brand js-scroll-trigger" href="#page-top">
        		<img class="img-fluid" src="images/logo.png" alt="" width="90" height="10"/>
        	</a>
        			<button class="navbar-toggler navbar-toggler-right" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
        				القائمة الرئيسية
        				<i class="fa fa-bars"></i>
        			</button>
        			<div class="collapse navbar-collapse" id="navbarResponsive">
        				<ul class="navbar-nav text-uppercase ml-auto">
        					<li class="nav-item">
        						<a class="nav-link js-scroll-trigger" href="#">تواصل معنا </a>
        					</li>
        					<li class="nav-item">
        						<a class="nav-link js-scroll-trigger" href="#">من نحن؟</a>
        					</li>

        					<li class="nav-item">
        						<a class="nav-link js-scroll-trigger active" href="#">الصفحة الرئيسية</a>
        					</li>
        				</ul>
        			</div>
        		</div>
        	</nav>

        <section id="home"  style="background: url('images/header.png')">


        		<h1 style="color:#485459; text-align:right; font-size:50px;serif;padding-bottom:140px ; padding-Top:140px; padding-right:150px;" >
        		رفع الصور  </h1>
        </section>
           <br /><br />
           <div class="container" style="width:500px;" align="center">
                <h3 align="center">فضلا قم برفع الصورة ثم انقر على زر ارسال</h3>
                <br />
                <form method="post" enctype="multipart/form-data">
                     <input type="file" name="image" id="image" />
					 <input type="text" name="volunteerID" id="volunteerID" />
                     <br />
                     <input type="submit" name="insert" id="insert" value="ارسال"class="login100-form-btn" style="background-color:#90A4AE"  />
                </form>
                <br />
                <br />
                <table class="table table-bordered">
                     <tr>
                          <th>Image</th>
                     </tr>
                <?php
                $query = "SELECT * FROM image";
                $result = mysqli_query($connect, $query);
                while($row = mysqli_fetch_array($result))
                {
                     echo '
                          <tr>
                               <td>
                                    <img src="data:image/jpeg;base64,'.base64_encode($row['imagePath'] ).'" height="200" width="200" class="img-thumnail" />
                               </td>
                          </tr>
                     ';
                }
                ?>
                </table>
           </div>
      </body>
 </html>
 <script>
 $(document).ready(function(){
      $('#insert').click(function(){
           var image_name = $('#image').val();
           if(image_name == '')
           {
                alert("Please Select Image");
                return false;
           }
           else
           {
                var extension = $('#image').val().split('.').pop().toLowerCase();
                if(jQuery.inArray(extension, ['gif','png','jpg','jpeg','tif']) == -1)
                {
                     alert('Invalid Image File');
                     $('#image').val('');
                     return false;
                }
           }
      });
 });
 </script>
