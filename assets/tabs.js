function show_home_tab () {
    var home = document.getElementById("home_main_body");
    var prog = document.getElementById("programming_main_body");
    var piano = document.getElementById("piano_main_body");
    var photo = document.getElementById("photography_main_body");

    var home_link = document.getElementById("home_link");
    var prog_link = document.getElementById("programming_link");
    var piano_link = document.getElementById("piano_link");
    var photo_link = document.getElementById("photography_link");

    home.className = "content";
    prog.className = "display_none";
    piano.className = "display_none";
    photo.className = "display_none";
    
    home_link.innerHTML = "▾ Profile";
    prog_link.innerHTML = "▸ Programming";
    piano_link.innerHTML = "▸ Piano";
    photo_link.innerHTML = "▸ Photography";

    window.scrollTo(0, 0)
}

function show_prog_tab () {
    var home = document.getElementById("home_main_body");
    var prog = document.getElementById("programming_main_body");
    var piano = document.getElementById("piano_main_body");
    var photo = document.getElementById("photography_main_body");

    var home_link = document.getElementById("home_link");
    var prog_link = document.getElementById("programming_link");
    var piano_link = document.getElementById("piano_link");
    var photo_link = document.getElementById("photography_link");

    home.className = "display_none";
    prog.className = "content";
    piano.className = "display_none";
    photo.className = "display_none";
    
    home_link.innerHTML = "▸ Profile";
    prog_link.innerHTML = "▾ Programming";
    piano_link.innerHTML = "▸ Piano";
    photo_link.innerHTML = "▸ Photography"

    window.scrollTo(0, 0)
}

function show_piano_tab () {
    var home = document.getElementById("home_main_body");
    var prog = document.getElementById("programming_main_body");
    var piano = document.getElementById("piano_main_body");
    var photo = document.getElementById("photography_main_body");

    var home_link = document.getElementById("home_link");
    var prog_link = document.getElementById("programming_link");
    var piano_link = document.getElementById("piano_link");
    var photo_link = document.getElementById("photography_link");

    home.className = "display_none";
    prog.className = "display_none";
    piano.className = "content";
    photo.className = "display_none";

    home_link.innerHTML = "▸ Profile";
    prog_link.innerHTML = "▸ Programming";
    piano_link.innerHTML = "▾ Piano";
    photo_link.innerHTML = "▸ Photography"

    window.scrollTo(0, 0)
}

function show_photo_tab () {
    var home = document.getElementById("home_main_body");
    var prog = document.getElementById("programming_main_body");
    var piano = document.getElementById("piano_main_body");
    var photo = document.getElementById("photography_main_body");

    var home_link = document.getElementById("home_link");
    var prog_link = document.getElementById("programming_link");
    var piano_link = document.getElementById("piano_link");
    var photo_link = document.getElementById("photography_link");

    home.className = "display_none";
    prog.className = "display_none";
    piano.className = "display_none";
    photo.className = "content";

    home_link.innerHTML = "▸ Profile";
    prog_link.innerHTML = "▸ Programming";
    piano_link.innerHTML = "▸ Piano";
    photo_link.innerHTML = "▾ Photography"

    window.scrollTo(0, 0)
}