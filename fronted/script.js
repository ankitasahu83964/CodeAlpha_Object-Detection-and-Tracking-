const streamURL = "http://127.0.0.1:5000/video";

function startCamera() {
    const video = document.getElementById("videoStream");

    video.src = streamURL;
    video.style.display = "block";
    document.getElementById("status").innerText = "🟢 Camera: ON";

}
function stopCamera() {
    const video = document.getElementById("videoStream");
    video.src = "";
    video.style.display = "none";

    document.getElementById("status").innerText = "🔴 Camera: OFF";
}
function updateCount() {
    fetch("http://127.0.0.1:5000/count")
        .then(res => res.json())
        .then(data => {
            document.getElementById("count").innerText =
                "Total Persons: " + data.total;
        });
}