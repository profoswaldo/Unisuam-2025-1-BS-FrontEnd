class Aluno {
    constructor() {
        this.mat = "0000";
        this.nm = "Visitante";
        this.n1 = -1;
        this.n2 = -1;
        this.n3 = -1;
    }

    set matricula(aux) {
        this.mat = aux;
    }
    set nome(aux) {
        this.nm = aux;
    }
    set nota1(aux) {
        this.n1 = aux;
    }
    set nota2(aux) {
        this.n2 = aux;
    }
    set nota3(aux) {
        this.n3 = aux;
    }

    calcularMedia() {
        return (this.n1 + this.n2 + this.n3) / 3
    }

    identificarStatus() {
        if (this.calcularMedia() >= 7)
            return "Aprovado";
        else
            if (this.calcularMedia() < 5) 
                return "Reprovado"
            else
                return "Final"
    }

    exibir(){
        alert("Matricula: " + this.mat 
                    + " Nome: " + this.nm
                    + " Média: " + this.calcularMedia()
                    + " Situação: " + this.identificarStatus()
        )
    }

}



function calcular(){
    aluno = new Aluno();
    aluno.matricula = document.getElementById("txtMatricula").value
    aluno.nome = document.getElementById("txtNome").value
    aluno.nota1 = parseFloat(document.getElementById("txtNota1").value)
    aluno.nota2 = parseFloat(document.getElementById("txtNota2").value)
    aluno.nota3 = parseFloat(document.getElementById("txtNota3").value)
    
    aluno.exibir();
}