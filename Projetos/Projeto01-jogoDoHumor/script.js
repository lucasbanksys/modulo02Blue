var btn = document.getElementById('btn_01');
var mudaHumor = document.getElementById('estado');

btn.onclick = function() {

    if(btn.value == 'first') {
        mudaHumor.src = 'https://raw.githubusercontent.com/lucasbanksys/modulo02Blue/main/Projetos/Projeto01-jogoDoHumor/images/gokufeliz.jpg';
        btn.value = 'sec';
    
    } else if (btn.value == 'sec') {
        mudaHumor.src = 'https://raw.githubusercontent.com/lucasbanksys/modulo02Blue/main/Projetos/Projeto01-jogoDoHumor/images/gokutriste.jpg';
        btn.value = 'first'
    }    
}
