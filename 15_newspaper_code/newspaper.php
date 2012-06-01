<?php
	// The next sentence was obtained using the image who results of the script
	// after the die
	// Original chars:
	// thesecrethasbeenrevealedtosolvethechallengewhichisthetwentiethemirp
	// Decoded text: The secret has been revealed to solve the challenge which is the twentieth emirp
	// emirp: http://en.wikipedia.org/wiki/Emirp
	// You can get the list from: http://oeis.org/A006567
	// And the winner is......:
	echo "389" . PHP_EOL;
	die();

	ini_set('memory_limit', '1900M');

	$image = imagecreatefrompng('newspaper.png');

	$width = imagesx($image);
	$height = imagesy($image);

	$outImage = imagecreate($width, $height);


	/**
	  * Create a new PNG image file, and read each byte of the original trying to
	  * find a special color, the 2147483647 , and put a X in red over the corresponding
	  * position, and put the image into the standar output, after that... read it?
	  */
	$background = imagecreatefrompng('newspaper.png');
	$font = 'arial.ttf';

	$textColorRed = imagecolorallocate($background, 255, 0, 0);
	$textColorBlue = imagecolorallocate($background, 0, 0, 255);

	$colors = array();
	for($x = 0; $x < $width; $x++)
	{
		for($y = $height; $y >= 0; $y--)
		{
			//echo $x . " - " . $y . PHP_EOL;
			$color = imagecolorat($image, $x, $y);

			//print($color . " -- " . $x . " - " . $y . PHP_EOL);


			if (isset($colors[$color]))
				$colors[$color]++;
			else
				$colors[$color] = 1;

			/*
				[0] => 32721
				[16777215] => 248510
				[14211288] => 7233
				[15921906] => 8365
				[13421772] => 7177
				[15066597] => 8045
				[8355711] => 27167
				[12566463] => 17531
				[4144959] => 26689
				[2147483647] => 56
				[2146628338] => 5
				[2145773029] => 5
				[2144917720] => 1
			*/

			if ($color == 2144917720)
				imagettftext($background, 8, 0, $x - 3, $y, $textColorBlue, $font, '_');

			if ($color == 2145773029)
				imagettftext($background, 8, 0, $x - 3, $y, $textColorRed, $font, '_');

			if ($color == 2146628338)
				imagettftext($background, 8, 0, $x - 3, $y, $textColorRed, $font, '_');

			if ($color == 2147483647)
				imagettftext($background, 8, 0, $x - 3, $y, $textColorRed, $font, '_');
		}
	}

	imagepng($background);
