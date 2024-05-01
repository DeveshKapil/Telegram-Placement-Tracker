<?php
// aside_generator.php

// Start the session
session_start();

// Check if $_SESSION['batch'] is set and echo its value as the id attribute
echo isset($_SESSION['batch']) ? $_SESSION['batch'] : '';
?>
