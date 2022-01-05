<?php
  $num = 55885;  
  $rev = 0;  
     while($num!=0)  
   {  
     $rem=$num%10;  
     $rev = $rev  * 10 + $rem;  
     $num= (int)($num/10) ;  
   }  
   echo "Sum of digits 55885 is $rev"; 
?>

