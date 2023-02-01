function func() {
    let opa = prompt("Change me");
    let text
    if (opa == null || opa == "") {
        text = "WTF"       
    } else {
        text = opa
    }
        document.getElementById("opa").innerText = text
}