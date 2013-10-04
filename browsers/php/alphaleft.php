<html>
<head>
<link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
<?php

$file = file_get_contents("http://www.altbibl.io/astrothesaurus/uat/termrecords/", "r");

preg_match_all("/\<a href\=\"(.*?).html\"\>/", $file, $links);
$term = str_replace("+", " ", $links[1]);

natcasesort($term);


$previous = null;
foreach($term as $value)
	{
    $html = str_replace(" ", "+", $value);
    $decode =  urldecode($value);
    $name = htmlentities($decode, ENT_NOQUOTES, "UTF-8");
    
    $firstLetter = substr($name, 0, 1);
    if(strtolower($previous) !== strtolower($firstLetter))
    	{
    	echo "<br/><b><a id='".$firstLetter."'>".$firstLetter."</a></b><br /><br />";
   		$previous = $firstLetter;
		}
    $url = "<a href='http://www.altbibl.io/astrothesaurus/uat/termrecords/".$html.".html' target='rightframe'>".$name."</a>";
    echo $url."<br/>";
	}

?>
</body>
</html>
