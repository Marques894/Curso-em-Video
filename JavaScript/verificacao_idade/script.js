function carregar() {

}

function verificar() {
    var data = new Date()
    var ano = data.getFullYear()
    var fano = document.getElementById("txtano")
    var res = document.querySelector("div#res")

    if (fano.value.length == 0 || Number(fano.value) > ano) {
        window.alert("[ERRO] Verifique os dados e tente novamente")
    } else {
        var fsex = document.getElementsByName('radsex');
        var idade = ano - Number(fano.value);
        var gênero = '';

        var img = document.createElement('img')
        img.setAttribute('id', 'foto')

        if (fsex[0].checked) {
            gênero = 'Homem';
            if (idade > 0 && idade <= 12) {
                //Criança
                img.setAttribute('src', './asset/homem-criança.svg')
            } else if (idade >= 13 && idade <= 18) {
                //Adolecente
                img.setAttribute('src', './asset/homem-adolecente.svg')
            } else if (idade >= 19 && idade < 60) {
                //Adulto
                img.setAttribute('src', 'homem-adulto.svg')
            } else if (idade > 60) {
                //Idoso
                img.setAttribute('src', 'homem-idoso.svg')
            }

        } else if (fsex[1].checked) {
            gênero = 'Mulher';
            if (idade > 0 && idade <= 12) {
                //Criança
                img.setAttribute('src', 'mulher-criança.svg')
            } else if (idade >= 13 && idade <= 18) {
                //Adolecente
                img.setAttribute('src', 'mulher-adolecente.svg')
            } else if (idade >= 19 && idade < 60) {
                //Adulto
                img.setAttribute('src', 'mulher-adulta.svg')
            } else if (idade > 60) {
                //Idoso
                img.setAttribute('src', 'mulher-idosa.svg')
            }
        }
        res.innerHTML = `Detectamos ${gênero} com ${idade} anos.`;
        res.appendChild(img)
    }
}