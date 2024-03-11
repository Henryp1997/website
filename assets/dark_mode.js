var num_clicks = 0
function toggle_dark_mode () {
    num_clicks += 1;
    if (num_clicks % 2 == 0) {
        return toggle_to_light()
    }
    return toggle_to_dark()
}

function toggle_to_light () {
    document.getElementById("pagestyle").setAttribute("href", "./assets/light.css")
}

function toggle_to_dark () {
    document.getElementById("pagestyle").setAttribute("href", "./assets/dark.css")
}