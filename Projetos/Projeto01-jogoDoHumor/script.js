var btn = document.getElementById('btn_01');
var mudaHumor = document.getElementById('estado');

btn.onclick = function() {

    if(btn.value == 'first') {
        mudaHumor.src = '/images/gokufeliz.jpg';
        btn.value = 'sec';
    
    } else if (btn.value == 'sec') {
        mudaHumor.src = '/images/gokutriste.jpg';
        btn.value = 'first'
    }    
}
