<html>
<head>
<link rel="stylesheet" type="text/css" href="style.css">
</head>
<body topmargin="0">
<center>
<?php

echo "<a id='top'></a>";

$alpha = range(A,Z);
foreach($alpha as $letter)
	{
	$location = "<a href='FramesetBottomFrame.php#".$letter."' target='bottomframe'>".$letter."</a>";
    echo $location."&nbsp;&nbsp;&nbsp;";
	}
?>
</center>
</body>
</html>
