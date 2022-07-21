if ("serviceWorker" in navigator) {
    navigator.serviceWorker.register("/sw.js")
        .then((reg) => console.log("Service Worker Registered", reg))
        .catch((err) => console.log("Service Worker Failed", err));
}

const radios = document.querySelectorAll('.form-check-input')
for (const radio of radios) {
    radio.onclick = (e) => {
        let units = document.querySelector("label[for='" + radio.id + "']").innerHTML.trim();
        units = units === "Celsius" ? 1 : 0;
        let url = window.location.href;

        let dict_values = {units, url} //Pass the javascript variables to a dictionary.
        let s = JSON.stringify(dict_values); // Stringify converts a JavaScript object or value to a JSON string
        $.ajax({
            url:"/setUnits",
            type:"POST",
            contentType: "application/json",
            data: JSON.stringify(s),
            complete: function (data) {
                window.location.href = url;
            }
        });
    }
}