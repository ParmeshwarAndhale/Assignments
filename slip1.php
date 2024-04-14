<?php
// Start the session
session_start();

// Check if the page count session variable is set
if(isset($_SESSION['page_count'])){
    $_SESSION['page_count'] += 1; // Increment the page count
} else {
    $_SESSION['page_count'] = 1; // Set the page count to 1 if it's not set yet
}

// Display the page count
echo "You have visited this page ".$_SESSION['page_count']." time(s).";
?>
