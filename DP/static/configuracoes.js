function changeFont() {
    var fontSelect = document.getElementById("fontSelect");
    var selectedFont = fontSelect.options[fontSelect.selectedIndex].value;
    
    var body = document.getElementsByTagName("body")[0];
    body.style.fontFamily = selectedFont;
}

function changeFontSize(value) {
    var fontSizeValue = document.getElementById("fontSizeValue");
    fontSizeValue.textContent = value + "px";
    
    var body = document.getElementsByTagName("body")[0];
    body.style.fontSize = value + "px";
}

function changeFontColor(value) {
    var body = document.getElementsByTagName("body")[0];
    body.style.color = value;
}

function previewProfilePicture(event) {
    var profilePicturePreview = document.getElementById("profilePicturePreview");
    profilePicturePreview.src = URL.createObjectURL(event.target.files[0]);
}
