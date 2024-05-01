window.addEventListener('load', function() {
    var image = document.getElementById('image');

    // Desired width and height
    var maxWidth = 8000; // Change this to your desired maximum width
    var maxHeight = 800; // Change this to your desired maximum height

    // Get the original width and height of the image
    var originalWidth = image.width;
    var originalHeight = image.height;

    image.width = maxWidth;
    image.height = maxHeight;

    // Set the new width and height with a slight delay to ensure smooth transition
    setTimeout(function() {
        image.style.width = originalWidth + 'px';
        image.style.height = originalHeight + 'px';
    }, 20);
});
