<?php
	// Yes, this code is so dirty, I know, but I need to sleep, sorry :(
	ini_set('memory_limit', '1900M');
	$input = file("php://stdin", FILE_IGNORE_NEW_LINES);
	$inputLength = strlen($input[0]);
	$keys = array(
		//'482a9a4cd222fc2086c52698893e6b22', // MD5 of the image???
		'ed8ce15da9b7b5e2ee70634cc235e363', // Code from the Bidi (I used my iPhone :) )
		$input[0]);

	// Claculate the solution for the given keys array
	function calcSolution($inKeys) {
		for ($count = 0; $count < strlen($inKeys[0]); $count++) {
			$char = 0;
			foreach ($inKeys as $key)
				$char += hexdec($key[$count]);
	
			$ret .= dechex($char % 16);
		}

		return $ret;
	}

	// Vendor class used to get the chunks and the code inside
	class PNG_Reader {
		private $_chunks;
		private $_fp;
	
		function __construct($file) {
			if (!file_exists($file)) {
				throw new Exception('File does not exist');
			}
	
			$this->_chunks = array ();
	
			// Open the file
			$this->_fp = fopen($file, 'r');
	
			if (!$this->_fp)
				throw new Exception('Unable to open file');
	
			// Read the magic bytes and verify
			$header = fread($this->_fp, 8);
	
			if ($header != "\x89PNG\x0d\x0a\x1a\x0a")
				throw new Exception('Is not a valid PNG image');
	
			// Loop through the chunks. Byte 0-3 is length, Byte 4-7 is type
			$chunkHeader = fread($this->_fp, 8);
	
			while ($chunkHeader) {
				// Extract length and type from binary data
				$chunk = @unpack('Nsize/a4type', $chunkHeader);
	
				// Store position into internal array
				if ($this->_chunks[$chunk['type']] === null)
					$this->_chunks[$chunk['type']] = array ();
				$this->_chunks[$chunk['type']][] = array (
					'offset' => ftell($this->_fp),
					'size' => $chunk['size']
				);
	
				// Skip to next chunk (over body and CRC)
				fseek($this->_fp, $chunk['size'] + 4, SEEK_CUR);
	
				// Read next chunk header
				$chunkHeader = fread($this->_fp, 8);
			}
		}
	
		function __destruct() { fclose($this->_fp); }
	
		// Returns all chunks of said type
		public function get_chunks($type) {
			if ($this->_chunks[$type] === null)
				return null;
	
			$chunks = array ();
	
			foreach ($this->_chunks[$type] as $chunk) {
				if ($chunk['size'] > 0) {
					fseek($this->_fp, $chunk['offset'], SEEK_SET);
					$chunks[] = fread($this->_fp, $chunk['size']);
				} else {
					$chunks[] = '';
				}
			}
	
			return $chunks;
		}
	}

	$imageParser = new PNG_Reader('CANTTF.png');
	$codes = $imageParser->get_chunks('tEXt');
	$keys[] = substr($codes[0], $inputLength * -1);

	$image = imagecreatefrompng('CANTTF.png');

	$width = imagesx($image);
	$height = imagesy($image);

	//echo $width . " - " . $height . PHP_EOL;

	// Using the LSB Method to obtain the secret code...
	for($y = $height; $y >= 0; $y--)
	{
		for($x = $width; $x >= 0; $x--)
		{
			//echo $x . " - " . $y . PHP_EOL;
			$color = imagecolorat($image, $x, $y);

			$pix = array(
				'B' => ($color >> 16) & 0xFF,
				'G' => ($color >> 8) & 0xFF,
				'R' => $color & 0xFF);

			// Possible bite orders
			//$data .= ($pix['R'] & 1) . ($pix['B'] & 1);
			//$data .= ($pix['R'] & 1) . ($pix['G'] & 1);
			//$data .= ($pix['G'] & 1) . ($pix['R'] & 1);
			//$data .= ($pix['G'] & 1) . ($pix['B'] & 1);
			//$data .= ($pix['B'] & 1) . ($pix['R'] & 1);
			//$data .= ($pix['B'] & 1) . ($pix['G'] & 1);
			//$data .= ($pix['B'] & 1);
			//$data .= ($pix['R'] & 1);
			//$data .= ($pix['G'] & 1);
			$data .= ($pix['R'] & 1) . ($pix['G'] & 1) . ($pix['B'] & 1);
			//$data .= ($pix['R'] & 1) . ($pix['B'] & 1) . ($pix['G'] & 1);
			//$data .= ($pix['B'] & 1) . ($pix['R'] & 1) . ($pix['G'] & 1);
			//$data .= ($pix['B'] & 1) . ($pix['G'] & 1) . ($pix['R'] & 1);
			//$data .= ($pix['G'] & 1) . ($pix['B'] & 1) . ($pix['R'] & 1);
			//$data .= ($pix['G'] & 1) . ($pix['R'] & 1) . ($pix['B'] & 1);
		}
	}

	$len = strlen($data);

	// Reverse the bites
	for ($count = $len - 1; $count >= 0; $count--)
		$final .= $data[$count];

	$data = $final;

	$finalStr = '';

	$lastPos = 0;
	for ($count = 0; $count < $len; $count += 8)
	{
		$ch = chr(bindec(substr($data, $count, 8)));

		if ((ord($ch) > 31) && (ord($ch) < 123)) {
			$lastPos = $count;
			$finalStr .= $ch;
		}
	}

	$keys[] = substr($finalStr, 0, $inputLength);

	echo calcSolution($keys) . PHP_EOL;
