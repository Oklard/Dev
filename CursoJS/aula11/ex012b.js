var agora = new Date()
var hora = agora.getHours()
console.log(`Agora são exatamente${hora}s.`)
if (hora < 12){
    console.log('bom dia!') 
} else if (hora <= 18){
console.log(`Boa tarde!`)
} else {
    console.log('Boa noite!')
}

