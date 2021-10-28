function carregar () {
var msg = window.document.getElementById('msg')
var img = window.document.getElementById('imagem')
var data = new Date()
var hora = data.getHours()
if (hora >=0 && hora <12)                  {
        msg.innerHTML = `Agora são ${hora} horas. BOM DIA!`
          img.src = `imagens/fotomanha.png`
          document.body.style.backgroundColor = `#dfe4b5`
    }   else if (hora >= 12 && hora <=18)  {
        msg.innerHTML = `Agora são ${hora} horas. BOA TARDE!`
          img.src = `imagens/fototarde.png`
          document.body.style.backgroundColor = `#ee8e3b`
    }   else                               {
        msg.innerHTML = `Agora são ${hora} horas. BOA NOITE!`
          img.src = `imagens/fotonoite.png`
          document.body.style.backgroundColor = `#aa5a05`
    }
                     }
 