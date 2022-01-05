<?php
  
function pattern($n)
{
      
    for ($i = 0; $i < $n; $i++)
    {
          
        for($j = 0; $j <= $i; $j++ )
        {
            echo "* ";
        }

        echo nl2br("\n");
    }

}
$n = 5;
    pattern($n);

?>
