
const btnCopiarPassword = document.getElementById('txt-copiar-password');
btnCopiarPassword.addEventListener('click', copiar_password_click);

const btnGenerarPassword = document.getElementById('txt-update-password');
btnGenerarPassword.addEventListener('click', generar_password_click);

generar_password_click();



function verificar_swiches(){
    let minusculas = 'abcdefghijklmnñopqrstuvxyz';
    let mayusculas = minusculas.toUpperCase();
    let numeros = '0123456789';
    let caracteres = document.getElementById('txt-input-caracteres').value;

    const tieneMayusculas = document.getElementById('txt-switch-mayusculas').checked;
    const tieneMinusculas = document.getElementById('txt-switch-minusculas').checked;
    const tieneNumeros = document.getElementById('txt-switch-numeros').checked;
    const tieneCaracteres = document.getElementById('txt-switch-caracteres').checked;

    let cadenaDeCaracteres = '';
    if (tieneMayusculas){
        cadenaDeCaracteres = cadenaDeCaracteres + mayusculas;
    }
    if (tieneMinusculas){
        cadenaDeCaracteres = cadenaDeCaracteres + minusculas;
    }
    if (tieneNumeros){
        cadenaDeCaracteres = cadenaDeCaracteres + numeros;
    }
    if (tieneCaracteres){
        cadenaDeCaracteres = cadenaDeCaracteres + caracteres;
    }
    return cadenaDeCaracteres;
}

function longitud_de_password(){
    let longitudPassword = parseInt(document.getElementById('txt-longitud-password').value);
    if (longitudPassword > 32){
        longitudPassword = 32;
    }else if (longitudPassword < 8){
        longitudPassword = 8;
    }
    return longitudPassword;
}
function generar_password_click(){
    let longitudPassword = longitud_de_password();
    let caracteresSeleccionados = verificar_swiches();
    let password = '';
    for (let i = 0; i < longitudPassword; i++) {
        password += caracteresSeleccionados.charAt(Math.floor(Math.random() * caracteresSeleccionados.length));
    }
    let passwordGenerado = document.getElementById('txt-password-generado');
    passwordGenerado.value = password;
}

function copiar_password_click(){
    const passwordGenerado = document.getElementById('txt-password-generado');
    passwordGenerado.focus();
    document.execCommand('selectAll');
    document.execCommand('copy');
}


