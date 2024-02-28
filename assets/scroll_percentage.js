window.onscroll = function () {
    var doc = document.documentElement
    percentage = 100 * doc['scrollTop'] / (doc['scrollHeight'] - doc['clientHeight'])
    if (percentage > 100) {
        percentage = 100
    }
    
    var percent_bar = document.getElementById('percentage_bar');
    percent_bar.style.backgroundImage = `linear-gradient(to right, #116927 ${percentage}%, #ffffff ${percentage}%)`
}
