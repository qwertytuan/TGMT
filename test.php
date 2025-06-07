<!DOCTYPE html>
<html>
<head>
    <title>Read Text File</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            background-color: #f4f4f4;
        }
        .container {
            background-color: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        pre {
            background-color: #e9e9e9;
            padding: 15px;
            border-radius: 5px;
            white-space: pre-wrap; /* Ensures long lines wrap */
            word-wrap: break-word; /* Ensures long words break */
        }
        .error {
            color: red;
            font-weight: bold;
        }
    </style>
</head>
<body>

    <div class="container">
        <h1>Content of data.txt</h1>

        <?php
        $filename = '1.txt'; // The name of your text file

        // Check if the file exists
        if (file_exists($filename)) {
            // Check if the file is readable
            if (is_readable($filename)) {
                // Read the entire file into a string
                $file_content = file_get_contents($filename);

                // Display the content within a <pre> tag to preserve formatting
                echo "<pre>" . htmlspecialchars($file_content) . "</pre>";
            } else {
                echo "<p class='error'>Error: The file '$filename' is not readable. Please check file permissions.</p>";
            }
        } else {
            echo "<p class='error'>Error: The file '$filename' does not exist.</p>";
        }
        ?>
    </div>

</body>
</html>
