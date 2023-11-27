

function validanome(form){
    if (form.nome.value==="" || form.nome.value=== null) {
        alert("PREENCHA O CAMPO NOME");       
        form.nome.focus();
        return false;
        
    }
    if (form.idade.value==="" || form.idade.value=== null) {
        alert("PREENCHA O CAMPO IDADE");       
        form.idade.focus();
        return false;
        
    }

    if (form.cell.value==="" || form.cell.value=== null) {
        alert("PREENCHA O CAMPO TELEFONE");       
        form.cell.focus();
        return false;
        
    }

    if (form.email.value==="" || form.email.value=== null) {
        alert("PREENCHA O CAMPO E-MAIL");       
        form.email.focus();
        return false;
        
    }

    if (form.title[0].checked) {
        alert("OK");
        return false;
    }

    var escolha = false;
    var x = document.form.title;
    for (i=0; i<x.length; i++) {
        if (x[i].checked) {
            alert("OK");
            escolha = true;
            break;
        }

        
    }

    
}


    



console.log(1 == 2);
console.log(1 == "1");
console.log(1 == 1);
console.log(1 === 1);

