<?php
$folder = './TH_1';
$files = scandir($folder);

echo "<h1>Contents of .txt files in TH_1</h1>";
foreach ($files as $file) {
    $filePath = $folder . '/' . $file;
    if (is_file($filePath) && pathinfo($filePath, PATHINFO_EXTENSION) === 'py') {
        echo "<h2>File: $file</h2>";
        echo "<pre>" . htmlspecialchars(file_get_contents($filePath)) . "</pre>";
    }
}
?>
