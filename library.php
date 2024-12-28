<?php

class PackageInstaller {
    // Method to install a package using 'sudo apt install'
    public function installPackage($packageName) {
        // Command to install the package
        $command = "sudo apt install -y " . escapeshellarg($packageName);
        
        // Execute the command
        $output = shell_exec($command);
        
        // Return the output of the command
        return $output;
    }
}

// Usage
$installer = new PackageInstaller();
$result = $installer->installPackage("powerpy");

// Output the result
echo "<pre>$result</pre>";

?>
