const result = document.getElementById('result');
const btn = document.getElementById('btn');

btn.addEventListener('click', operation);

function operation() {
    let option = document.getElementById('option').value;
    let num1 = document.getElementById('num1').value;
    let num2 = document.getElementById('num2').value;

    option = parseInt(option);

    if (option === 6) {
        salir();
        return;
    }

    if ((isNaN(option)) || (option === "") || (option === 0)) {
        result.innerHTML = 'Por favor seleccione una opción valida';
        return;
    }

    if ((isNaN(num1)) || (num1 === '') || (isNaN(num2)) || (num2 === '')) {
        result.innerHTML = 'Por favor ingrese datos validos para realizar la operación';
        return;
    }

    num1 = parseInt(num1);
    num2 = parseInt(num2);

    switch (option) {

        case 1: sumar(num1, num2);
            break;
        case 2: restar(num1, num2);
            break;
        case 3: multiplicar(num1, num2);
            break;
        case 4: dividir(num1, num2);
            break;
        case 5: modulo(num1, num2);
            break;
        default:
            break;
    }
}

function sumar(n1, n2) {
    return result.innerHTML = `Resultado de sumar: ${n1} + ${n2} = ${n1 + n2}`;
}

function restar(n1, n2) {
    return result.innerHTML = `Resultado de restar: ${n1} - ${n2} = ${n1 - n2}`;
}

function multiplicar(n1, n2) {
    return result.innerHTML = `Resultado de multiplicar: ${n1} x ${n2} = ${n1 * n2}`;
}

function dividir(n1, n2) {
    return result.innerHTML = `Resultado de dividir: ${n1} / ${n2} = ${n1 / n2}`;
}

function modulo(n1, n2) {
    return result.innerHTML = `Resultado del módulo: ${n1} % ${n2} = ${n1 % n2}`;
}

function salir() {
    result.innerHTML = 'Cerrando la ventana actual . . .';
    setTimeout(() => {
        window.open('index.html', 'Nueva ventana');
        window.close();
    }, 1000);
}