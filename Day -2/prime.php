<?php
 $number = 59;

 for ($i=2; $i <$number; $i++) { 
      if($number%$i == 0){
             break;
      }
 }
 
 if($i == $number){
    echo "is a prime number";
 }
 else{
     echo "is not a prime number";
 }
?>
