window.onscroll = function () {
    var doc = document.documentElement
    percentage = Math.ceil(100 * doc['scrollTop'] / (doc['scrollHeight'] - doc['clientHeight']))
    
    var percent_bar = document.getElementById('percentage_bar')
    percent_bar.style.backgroundImage = `linear-gradient(to right, #116927 ${percentage}%, #ffffff ${percentage}%)`
}
