let RunSentimentAnalysis = () => {
    const textToAnalyze = document.getElementById("textToAnalyze").value;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4) {
            if (this.status == 200) {
                const response = JSON.parse(xhttp.responseText);
                document.getElementById("system_response").innerHTML = response.response;
            } else if (this.status == 400) {
                const errorResponse = JSON.parse(xhttp.responseText);
                document.getElementById("system_response").innerHTML = errorResponse.error;
            }
        }
    };

    xhttp.open("POST", "/emotionDetector", true);
    xhttp.setRequestHeader("Content-Type", "application/json");

    const payload = JSON.stringify({ statement: textToAnalyze });
    xhttp.send(payload);
};
