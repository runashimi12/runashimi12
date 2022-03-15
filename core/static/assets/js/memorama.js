let iconos = []
let selecciones = []

generarTablero()

function cargarIconos() {
    iconos = [
        '<img src="/static/assets/img/leccion7/burro.jpg" width="50%">',
        '<img src="/static/assets/img/leccion7/caballo.jpg" width="50%">',
        '<img src="/static/assets/img/leccion7/gato.jpg" width="50%">',
        '<img src="/static/assets/img/leccion7/pollito.jpg" width="50%">',
        '<img src="/static/assets/img/leccion7/aguila.jpg" width="50%">',
        '<img src="/static/assets/img/leccion7/Lobo.jpg" width="50%">',
        '<img src="/static/assets/img/leccion7/picaflor.jpg" width="50%">',
        '<img src="/static/assets/img/leccion7/conejo.jpg" width="50%">',
        '<img src="/static/assets/img/leccion7/perro.jpg" width="50%">',
        '<img src="/static/assets/img/leccion7/buho.jpg" width="50%">',
        '<img src="/static/assets/img/leccion7/oveja.jpg" width="50%">',
        '<img src="/static/assets/img/leccion7/sapo.jpg" width="50%">',
    ]
}

function generarTablero() {
    cargarIconos()
    let len = iconos.length
    selecciones = []
    let tablero = document.getElementById("tablero")
    let tarjetas = []
    // ${iconos[0]} 
    for (let i = 0; i < len * 2; i++) {
        tarjetas.push(`
            <div class="area-tarjeta" onclick="seleccionarTarjeta(${i})">
                <div class="tarjeta" id="tarjeta${i}">
                    <div class="cara trasera" s>
                     
                        ${iconos[0]}
                    </div>
                    <div class="cara superior">
                        <i class="far fa-question-circle"></i>
                    </div>
                </div>
            </div>        
            `)
        if (i % 2 == 1) {
            iconos.splice(0, 1)
        }
    }
    tarjetas.sort(() => Math.random() - 0.5)
    tablero.innerHTML = tarjetas.join(" ")
}

function seleccionarTarjeta(i) {
    let tarjeta = document.getElementById("tarjeta" + i)
    if (tarjeta.style.transform != "rotateY(180deg)") {
        tarjeta.style.transform = "rotateY(180deg)"
        selecciones.push(i)
    }
    if (selecciones.length == 2) {
        deseleccionar(selecciones)
        selecciones = []
    }
}

function deseleccionar(selecciones) {
    setTimeout(() => {
        let trasera1 = document.getElementById("trasera" + selecciones[0])
        let trasera2 = document.getElementById("trasera" + selecciones[1])
        if (trasera1.innerHTML != trasera2.innerHTML) {
            let tarjeta1 = document.getElementById("tarjeta" + selecciones[0])
            let tarjeta2 = document.getElementById("tarjeta" + selecciones[1])
            tarjeta1.style.transform = "rotateY(0deg)"
            tarjeta2.style.transform = "rotateY(0deg)"
        } else {
            trasera1.style.background = "red"
            trasera2.style.background = "red"
        }
    }, 1000);
}