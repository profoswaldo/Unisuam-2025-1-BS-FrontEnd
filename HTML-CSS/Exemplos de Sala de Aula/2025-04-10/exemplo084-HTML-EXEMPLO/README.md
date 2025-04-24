# HTMLCSSI
Curso HTML5 e CSS3 I: Suas primeiras páginas da Web / https://cursos.alura.com.br/course/introducao-html-css

<p align="center">
  <img src="https://givingdata.com/wp-content/uploads/2013/07/html-css-js.png" alt="Imagem de HTML JS E CSS">
</p>

# Aula 1: Iniciando HTML
## 1.1 Aplicando o DocType na Pag HTML (Define a versão mais recente do HTML)
  ### 1.1.1 O que é DocType e para o que serve?
    Doctype é uma instrução de qual tipo de documento HTML iremos trabalhar na pagina web.

    Doctype serve para definir a versao do HTML, como HTML 4.1 e HTML5
  ### 1.1.2 Como aplicar o doctype?
  Para aplicar basta por...
  ```<!DOCTYPE html>```
  Primeiro de tudo, antes da tag ```<html>```

## 1.2 Atribuindo Tags HTML (Estrutura onde ficara todos os conteudo do site)

Colocamos todo o conteudo do site dentro de algumas tags: 

```html 
<!DOCTYPE html>
<html> 
    <head>
    <meta charset="UTF-8">
    <title>Titulo da pagina</title>
    <link rel="stylesheet" type="text/css" href="estilo.css">
    </head>
    <body>
    </body>
</html>
```
## 1.3 Entendo as diferença entre as 3 TAGS

## HTML

> A tag HTML informa ao navegador que este é um documento HTML

>Representa também a raiz de um documento HTML

> É um receptiente para outros elementos, exceto para o <!DOCTYPE>

```html
 <html>
     Conteudo
 </html>
```

## HEAD

> A tag HEAD reprensenta um contêiner para conteudos introdutorios e conjuntos de links da sua pagina.

>Informando icones para pagina , titulos e autorias.

```html
<html>
    <head>
    <meta name="description" content="Descrição do meta dentro da tag HEAD">
        <meta charset="utf-8">
        <title>Titulo site</title>
    </head>
</html>
```

## BODY

> A tag BODY é o corpo do elemento. onde vai conter todo o seu codigo de uma estrutura html.
> Como texto, hiperlinks, imagens, tabelas, listas etc.

```html
<html>
    <head>
    <meta name="description" content="Descrição do meta dentro da tag HEAD">
        <meta charset="utf-8">
        <title>Titulo site</title>
    </head>
    <body>
      The content of the document......
    </body>
</html>
```

## 1.4 Atribuindo Tag LINK  REL (diz que tipo de conteúdo que queremos referenciar com ela)

> A tag "rel" define um atributo na qual aquela classe ta se referindo

>Neste exemplo, o rel indica que o documento referenciado é uma folha de estilo:

```html
<link rel="stylesheet" href="css/estilo.css">
```


## 1.5 Atribuindo Tag LINK > href (diz onde esse conteúdo se encontra)
  ```html
 TAG LINK

 <link> : define um link entre um documento e um recurso externo, usada para chamar uma folha de estilo externas.
 ```
 > Exemplo da tag Link
 ```html
 <head>
   <link rel="stylesheet" type="text/css" href="estilos.css">
</head>
 ```
> O atributo href especifica o URL da página para onde o link vai ou a folha de estilo externa.

> Neste Exemplo o href mostra onde o arquivo estilo.css está.

```html
<link rel="stylesheet" href="css/estilo.css">
```
>Na pasta CSS onde a folha estilo.css se encontra

## 1.6 Atribuindo Tag META > charset="utf-8" (indicando que nossa página usa a codificação de caracteres UTF-8)
```html
TAG META

<meta> : Fornece dados sobre o documento HTML.
Geralmente sao usados para especificar as descrições da pagina, as palavras-chaves e o autor do documento.
```
> Mais Exemplos de metas:
 ```html
 <head>
  <meta charset="UTF-8">
  <meta name="description" content="Curso Alura HTML">
  <meta name="keywords" content="HTML5,CSS3,JavaScript">
  <meta name="author" content="Joey Andrade">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
 ```
## 1.7 Adicionando title na Aba do Navegador.. dando um titulo ao nosso site
```html
 TAG TITLE

<title> : Define um titulo para seu documento HTML, é necessária em todos os documentos HTML.
Fornece um título para a página quando ela é adicionada aos favoritos.
Exibe um título para a página nos resultados do mecanismo de pesquisa

Nota que você NÃO pode ter mais de um elemento <title> em um documento HTML.
```
> Exemplo da tag Title
 ```html
 <head>
  <title>Minha pagina Web</title>
</head>
 ```
## 1.8 Diferenças entre tags "p", "strong" e  "em" , e ultilizando na pagina HTML.

## 1.8.1 TAG  "**P**"
> A tag "p" usada geralmente para criaçoes de paragrafos, como o exemplo abaixo.
```html
    A tag <p>Paragrafo</p>
```
> Podemos atribuir varios paragrafos ao conteudo HTML

## 1.8.2 TAG "**STRONG**"
> Ja com a tag "strong" define um texto, conteudo importante, alem de deixar o texto em "**NEGRITO**" por assim dizer..
```html
    <strong> Conteudo importante da pagina e negrito </strong>
```
## 1.8.3 TAG "em"

>A tag "em" enfatiza um texto da pagina HTML, alem de deixar o texto "ITALICO" por assim dizer.

```html
    <em> Conteudo infatizado e italico </em>
```

## 1.9 Iniciando Blog index.
> Criando documento de Blog e index... Verificar no repositorio do github

# Aula 2: Introdução ao CSS
## 2.1 Criando estilo na pagina HTML bio e blog

>Entendo a criação de estilo inline onde voce pode por um estilo na propria linha html

>Exemplo :
```html
 <h1 style:font-size:16px"> Bom Trabalho </h1>
```
## 2.2 Atribuindo estilo a uma tag especifica:

>Você também pode por um estilo para um seletor especifica como o exemplo abaixo:

```html
<style type="text/css">
    h1 {
    	font-size: 16 px;
    }
</style>
```
>Assim todos os atributos que possuir a tag H1 vai ter o tamanho da fonte de 16px.

## 2.3 Atribuindo Tag "p" com estilo
>Podemos atribuir um elemento inline na tag "p" ou especifica-la na folha de estilo usando.

```html
<style type="text/css">
    p {
    	font-size:16px;
    }
</style>
```
OBS: Tema de um conteudo do alura.

## 2.4 Criando Estilo separado em um novo arquivo!!! css/estilo.css
>Como dito, voce pode criar um novo arquivo, nomear e por a extensão .css no fim do arquivo.

```
style.css
```

> E por fim chamar esse arquivo dentro do seu documento HTML utilizando a tag rel que mostramos acima.

## 2.5 Chamando estilo atravez da tag 

>Semanticamente falando ao usar o link para chamar a sua folha de estilo dará a voce mais organizacão, e nao deixa seu documento HTML sujo e bagunçado com varios codigos css, assim facilita mais na hora de trabalhar o estilo do seu site, vamos dividir as coisas e deixar mais organizados, por favor ne. :stuck_out_tongue:

>Para chamar sua folha de estilo basta fazer igual o exemplo abaixo:

```html
<link rel="stylesheet" href="css/estilo.css">
```
## 2.6 Adicionando e alterando fontes a elementos de texto, com fonte principal e fontes secundaria(Caso o usuario nao tiver a primeira fonte)

> Podemos atribuir varios tipos de fontes para o nosso site... a principal e a secundaria..
```html
<style type="text/css">
    h1 {
    	font-family: "Time New Roman" serif;
    }
</style>
```
>Como o exemplo acima, vimos que a fonte "Time New Roman" é a primeira fonte a ser chamada ao vizualizar nosso site. Caso o nosso usuario nao tiver essa fonte ele entao entrará no...

>Fonte Secundaria. que seria qualquer fonte do tipo serif... ou outra que você definir.

## 2.7 Entendendo as cores em RGB...
<p align="center">
  <img src="https://dicasdeprogramacao.com.br/images/entenda-como-funcionam-os-codigos-de-cores-rgb/cores-rgb.jpg" width="150" height="150" alt="imagem de cores RGB">
</p>

 >As cores RGB = RED, GREEN e BLUE que no português seria, Vermelho, Verde e Azul.3

 >Apartir dessa combinação é possiveis criar diversas cores para seu conteudo HTML com numeros que varia de 0 a 225.

 >O branco é quando se tem o maior valor para as 3 cores, ou seja, 255 para Red, Green e Blue. E o preto é formado quando se tem o valor 0 para essas 3 cores.

 >Assim sendo, quanto maior o valor mais claro fica e quanto menor o valor mais escuro fica.

 ```html 
  <style type="text/css">
    body {
         background-color: RGB(255, 255, 255);
    }
</style>
 ```

## 2.8 Cores mais especificas hexadecimal, #FFF, #EE8...

> Além disso a outras formas mais faceis de definir uma cor a sua pagina HTML.
 
 ```html 
  <style type="text/css">
    body {
         background-color: #FFFFFF;
    }
</style>
 ```
 > Uma cor pode ser especificada usando um valor hexadecimal

>Aqui voce encontra varias cores em Hexadecimal o nome e o formato em RGB:
<a href="https://site112.com/tabela-cores-html" target="_blank">Tabelas de cores em Hexadecimal</a>

> e por fim podemos usar nomes em Inglês da propria cor.
> 
 ```html 
  <style type="text/css">
    body {
         background-color: blue;
    }
</style>
 ```

# Aula 3: Aprofundando no HTML

> Aprofundamos mais no codigo HTML. Abaixo outras formas de ultilizar tags no nosso HTML.

## 3.1 Atribuindo links em textos 
>Quando queremos atribuir algum link em nossa pagina HTML, onde ao clicar ser direcionado a outra pagina temos duas formas de fazer esse caminho. Usamos um atributo de link como o exemplo abaixo.

```html
<a href=""> (links absolutos , links relativos) </a>
```
>A propriedade "a href" especifica um link a seu texto.

>como vimos no exemplo acima temos link Absolutos e links relativo. Abaixo temos 2 exemplos. olhem e veja a diferença.

### Links Absolutos:
```html
<a href="http://www.meusite.com.br/caminho.html">Home</a>
```
### Links Relativos:
```html
<a href="/caminho.html">Home</a>
```

## 3.2 Adicionando IMG na pagina 

>Uma coisa otima do HTML é a possibilidade de adicionar imagem em nosso documento HTMl.

>A Tag "IMG" define a imagem em nossa pagina HTML. Tendo com mais duas propriedades "OBRIGATORIA" que sao o "src" e o "alt".

>Como por exemplo:

```html
<img src="exemplo de como colocar" alt="Exemplo da tag img">

Nota q é uma Tag onde nao é nescessario fechar com </img>
```
<p align="center">
<img src="https://4.bp.blogspot.com/-0-_9i1nFi7k/VQgiuUl5ogI/AAAAAAAAAJ0/V2orNEV75bo/w800-h800/tag%2Bimg.png" width="150" height="110" alt="imagem da tag IMG">
</p>

>A imagem acima foi atribuida da mesma forma como o exemplo de codigo mais acima, basta por o link da pagina. Como vimos antes podemos por links relativo ou absoluto, nesse caso a imagem esta com link absoluto.

## 3.3 Tag alt="" tornando a pagina mais acessivel a deficientes visuais.

>Como o titulo ja fala um pouco da TAG "alt" notamos entao que.

>O atributo alt é necessário porque ele especifica um texto alternativo para uma imagem se a imagem não puder ser exibida.

>O atributo alt fornece informações da imagem para nosso usuario caso ele por algum motivo não puder visualizá-lo (devido à conexão lenta, a um erro no atributo src ou se o usuário usar um leitor de tela).

>Vimos muitos exemplos da TAG "**IMG**" COM "**ALT**" aqui vai mais um.

```html
    <img src="caminhoDaImagem" alt="Imagem sobre tal coisa">
```
## 3.4 Atribuindos citaçoes com tags ```<blockquote>``` e tag ```<cite>```

>Temos uma tag chamado "blockquote" que especifica uma seção na qual foi citado de uma outra fonte.
```html
    <blockquote> Lorem Ipsum is simply dummy text of the printing and typesetting industry. </blockquote>
```
>a imagem abaixo vai te da uma deia parecida.
<p align="center">
<img src="https://i0.wp.com/images.jcubic.pl/blockquote.png" alt="Imagem de citação blockquote" width="150">
</p>

> Quando usamos a tag "blockquote", provavelmente também usaremos a tag "cite".

>A Tag "cite" ela define um titulo.

>Titulo de uma obra, trabalho, um livro uma musica, filmes e etc...

>Um Exemplo:

```html
<p><cite>O Poderoso Chefao</cite>é um filme norte-americano de 1972.e etc e etc....</p>
```

## 3.5 HTML e Semântica ```<main>```: conteúdo principal da página

>A semântica no HTML é muito importante. Tem como objetivo descrever significado do conteudo no documento HTMl. tornando mais faceis para outros programadores que forem ler seu codigo HTML..

>O Elemtno "main" especifica o conteudo principal do seu documento HTML. E de maior relevância dentro da sua pagina, para ser considerada bem construida. tem como apresentar apenas um conteudo principal.

>Exemplos de de como usar a tag "main"

```html
<main>
  <h2>Titulo</h2>
  <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod ...</p>
  
  <article>
     <h3>Subtítulo</h3>
        <p>Duis aute irure dolor in reprehenderit in voluptate velit esse cillum...</p>
   </article>
</main>
```

## 3.6 outras tags importantantes com semântica
- ```<header>```: cabeçalho da página ou de uma região dela.
>Você pode ter vários elementos "header" em um documento
```html
<article>
  <header> <<<-------
    <h1>Most important heading here</h1>
    <h3>Less important heading here</h3>
    <p>Some additional information here</p>
  </header> <<<-------
  <p>Lorem Ipsum dolor set amet....</p>
</article>
```
- ```<footer>```: A tag "footer" define um rodapé para um documento ou seção.

>Você pode ter vários elementos "footer" em um documento.

>Como Exemplo:
```html
<footer>
  <p>Postado Por: Joel</p>
  <p>Contato: <a href="mailto:exemplo@email.com">
  exemplo@email.com</a>.</p>
</footer>
```

- ```<aside>```: conteúdo auxiliar ao conteúdo principal, como links relacionados ao conteúdo
>define algum conteúdo além do conteúdo em que é colocado.

>Como Exemplo:

```html
<p>Fui para Bahia de carro com minha familia. tem a gruta é tudo lindo e maravilhoso ...</p>

<aside>
  <h4>Bom jesus da lapa - Bahia</h4>
  <p>Bom jesus da lapa é uma otima cidade da Bahia..</p>
</aside>
```
- ```<article>```: conteúdo que, por si só, já tem um sentido completo, como um post de um blog ou uma notícia.

>especifica um conteudo como exemplo:
```html
<article>
  <h1>Meu Titulo</h1>
  <p>Minhas Informaçoes</p>
</article>
```

- ```<section>```: parte/seção de uma página ou texto
>Define seções em um documento, como capítulos, cabeçalhos, rodapés ou quaisquer outras seções do documento.

>Como Exemplo
```html 
<section>
  <h1>Titulo</h1>
  <p>Aqui Explicamos o que é sobre o titulo, ou outras coisas ..</p>
</section>
```
> uma imagem de exemplo de como podemos usar esses conteudos:

<p align="center">
<img src="https://ayudawordpress.com/wp-content/uploads/2010/05/estructura-tema-html5-500x250.gif" width="250" height="180" alt="Imagem resumida de como usar todos os elementos acima">
</p>

## 3.7 Listas com tag ```<ul>``` e ```<li>```

>Quando quisermos criar uma lista temos uma tag especifica para esses tipos de coisa que é a tag "ul"

>Essa tag define uma lista não ordenada.

>Use a tag "ul" junto com a tag "li" para criar listas não ordenadas

> A Tag "li" define um item da lista

>Como Exemplo
```html
   <ul>
     <li>Cafe</li>
     <li>Leite</li>
     <li>Suco</li>
   </ul>
```

>A imagem define melhor o que quero dizer:

<p align="center">
<img src="https://image.slidesharecdn.com/aula5-141124155334-conversion-gate02/95/aula5-listas-html-5-3-638.jpg?cb=1416844504" width="200" height="130">
</p>

## 3.8 Criando entidades no HTML

>ENTIDADES no HTML são simbolos que desejamos usar em nosso HTML..

>São usadas para exibir caracteres reservados em HTML

>Não basta apenas usar um atalho do teclado para por esse simbolo como > < © e etc. Ou ate mesmo pode nao conter no teclado e entao usamos os codigos.

>E mais facil voce por em codigo como o exemplo abaixo, assim o navegador vai interpretar melhor:

```html
<footer> 
 Todos os Direitos Reservados &copy;
</footer>

ou

<footer> 
 Todos os Direitos Reservados &#169;
</footer>

Ficaria Assim:  Todos os Direitos Reservados ©
```

>Imagem de Exemplo

> Aqui a uma lista grande de varios codigos de entidades 

><a href="http://arquivo.devmedia.com.br/artigos/devmedia/html-entities.html">Lista de Entidades</a>


## 3.9 Seletores de descendência
>O Seletor descendente é aplicado a um determinado elemento do documento, que descenda de outro. Exemplo, o elemento ```<em>``` está dentro diretamente do elemento ```<p>```, mas indiretamente dentro do elemento ```<div>```.

```html
    <div>
        <p>
            <em>
                conteudo
            </em>
        </p> 
    </div>

    Ficando assim na folha de estilo
    <style>
        div em{
             color: red;
        }
    </style>
```
> Lembrando que não é preciso definir todas as tags ate chegar na tag ```<em>```. Onde o elemento ```<em>```, está dentro de ```<p>```, que está dentro de ```<div>```

```css
    div p em {
        color: red;
    }
```
# Aula 4: O navegador trabalhando ao nosso favor
>Como Vimos no proprio titulo da Aula 4, podemos usar o navegador ao nosso favor para ajudar a projetar nosso site melhor ainda.

## 4.1 Abrindo inspetor de paginas no google crhome e FireFox

>Antes de iniciar pelo navegador precisamos abrir o inspetor do navegador. Bom eu mexo com o Google Crhome, mais vou por atalhos do FireFox também.

>No Google Crhome o atalho mais rapido e facil é o ```F12``` ou ```Ctrl + Shift + I```.

>No FireFox, se não me engano o comando seria ```Ctrl + Shift + I``` também.

## 4.2 Editando e adicionando propriedades do HTML e CSS com o inspetor.

>Com o inspetor aberto, podemos alterar varias coisas do seu documento HTML. Como o proprio HTML e CSS, sem contar que podemos adicionar novas tag no css e ver em "tempo real" as modificações.

>Para fazer isso é bem simples .. No seu codigo HTML ao clicar em qualquer tag, conseguimos alterar seu nome.

>Na parte do CSS, praticamente a mesma coisa, basta alterar ou adicionar um novo campo.

>Abaixo uma imagem para melhor entender sobre ambos.

<p align="center">
<img src="https://www.criarsites.com/wp-content/uploads/2012/08/lado-direito.png" width="250" height="200">
</p>

>O Element.style {
>    
>} é como se fosse o body da pagina, o que voce por ali vai diferenciar em todo o conteudo do seu documento HTML.

>Onde está escrito Matched CSS Rules: Ali encontra todo o seu codigo CSS na qual você escreveu no seu documento. e assim voce pode fazer edições e acompanhar as alteraçoes.

>É importante isso porque você pode fazer uma alteração, verificar como ficou, se gostar é so jogar para seu documento HTML.

## 4.3 Resolvendo ou procurando erros de digitação onde o inspetor mostra em casos dificeis.

>Outra coisa legal é você verificar se há algum erro no seu codigo HTML. O navegador consegue achar facilmente para gente.

<p align="center">
<img src="https://developers.google.com/web/tools/chrome-devtools/console/images/track-exceptions-example-error-message-expanded.png?hl=pt-br" width="400" height="200">
</p>

>Como ver na image acima, Sempre que tiver um X vermelho na aba superior, é sinal de que alguma linha está errada. basta clicar no icone ele vai te mostrar os erro.

# Aula 5: Aprimorando o Layout

## 5.1 Aplicando Espaçamento entre elementos ultilizando Padding e Margin.
 - ```Margin```: controla o espaço entre elementos de blocos.
 - ```Padding```: controla o espaço entre o conteúdo de um elemento e sua borda.

<p align="center">
<img src="https://static.daniweb.com/attachments/4/3cf29905c4a515a24556c7d869a599a3.png" width="400" height="200">
</p>

## 5.2 Propriedades Width , Height que controla apenas o tamanho de um elemento

- ```Width```: Especifica a largura de um elemento HTML.

- ```Height```: Especifica a altura de um elemento HTML.

>Por exemplo, para que o corpo de seu site tenha uma altura de 800 pixels e 500 pixels de largura, seria na folha de estilo mais ou menos assim:

```css
    .body {
        height: 800px;
        width:  600px;
        border: solid;
    }
```
>Abaixo uma imagem para melhor representar:

<p align="center">
<img src="https://openhome.cc/eGossip/JavaScript/images/ElementDimensions-2.png" width="400" height="200">
</p>

## 5.1 Propriedades Box-Sizing controla apenas como a largura e a altura de um elemento deve ser calculada.

>```Box-Sizing``` : permite incluir o preenchimento e a borda na largura e altura totais de um elemento.

>Isso porque quando definimos uma largura / altura para o nosso elemento, geralmente aparece maior do que definimos.

>EXEMPLO:
<p align="center">
<img src="https://cdn-images-1.medium.com/max/1600/1*guVy0tXjMKekfweA8rxsnA.png" width="450" height="200">
</p>

>Como mostrado na figura, exemplo #aa, não definimos nenhum tamanho de caixa. Por padrão, é a caixa de conteúdo. Portanto, a largura real desse elemento se torna 100 + 10 * 2 (preenchimento) + 5 * 2 (margem) = 130px.

>Ja o exemplo #bb, definimos o tamanho da caixa como: border-box. Portanto, a largura real desse elemento é 100px. Mas a largura de conteúdo exibida é 100 – 10 * 2 (preenchimento) - 5 * 2 (margem) = 70.

## 5.1 Propriedades Line-height controla apenas a altura entre as linhas de texto da página

>```line-height```: A propriedade especifica a altura de uma linha para a outra.

>Observe essa image e você terá uma noção.

<p align="center">
<img src="https://pearsonified.com/wp-content/uploads/2011/12/font-size-line-height.png" width="350" height="200">
</p>

>Ou teste em seu codigo HTML.

```css

    .p {
        line-height: 10px;
    }

```
>Jogue esse codigo em qualquer estilo css para definir o height da tag ```<p>``` entre as linhas, altura de ```10px```.

## 5.1 Atribuindo Bordas nos elementos, Tipos de bordas e espaçamentos e cores

>As bordars na propriedades CSS permitem que você especifique o estilo, a largura e a cor da borda de um elemento.

```css
    div {
        border:1px solid black;
    }

Aqui definimos uma div com borda de 1px solido da cor preta
```
>Exemplos de bordas.

<p align="center">
<img src="https://codando.files.wordpress.com/2008/03/image-thumb6.png?w=702&h=368" width="400" height="250">
</p>

>Alem de que podemos combinar as bordas.

```css
div {border-style: dotted dashed solid double;}
```

>A ```border-style``` propriedade pode ter de um a quatro valores (para a borda superior, borda direita, borda inferior e borda esquerda).

# Aula 6: Construindo uma base sólida

## 6.1 Aplicando estilo de Reset.css na pagina , resetando estilos padroes de navegadores.

>O navegador possui valores PADRÃO em sua navegação, e variam de um navegador para outro.

>por Exemplo, a margem padrão do body pode ser 10px no Internet Explorer e 8px no Firefox.

>O CSS Reset veio para tentar diminuir estes problemas. O objetivo dele é resetar todas as propriedades das tags htmls. A margem, a largura, etc… sempre vão ser iguais independente do browser que estiver renderizando o site.

>A forma mais interessante de resetar o navegador seria usando o elemento mais facil ```* { }```.

>Exemplo:

```css
    * {
        margin:0;
        padding:0;
    }
```

<p align="center">
<img src="https://images.ctfassets.net/8cb1vflpheox/1XSflhjB20ikEaSmeSawGy/44c37f670a7f8c17ce05edfed20a27a3/css-reset-padding.png" width="400" height="250">
</p>

>Lembrando que existe varios estilo de Reset.CSS free pela internet que vale apena da uma olhada e ultilizar.

## 6.2 Entendendo e atribuindo ordem de estilo, e o que pode afetar.

>Ordem de onde aplicar nossas folhas de estilos são bem interessantes. Devemos ter cuidado e atenção com isso.

>Como por exemplo, sobre o que falamos do ```RESET.CSS```, Se queremos usar o nosso reset como base para nosso css, devemos importá-lo antes do nosso CSS na página:

```html
<head>
    <link rel="stylesheet" href="reset.css">
    <link rel="stylesheet" href="bio.css">
</head>

```

## 6.1 Entendo sobre conflitos no css.

>Quando duas declarações conflitam no CSS, o navegador usa aquela que for declarada por último. Por Exemplo:

```css

h1 {
    font-size: 100%;
    color: red;
}

h1 {
    font-size: 30px;
    font-weight: bold;
}

```
> No exemplo acima, o estilo vai ser aplicado nos ```<h1>```. Então o navegador vai fazer o seguinte:
> 
- Aplicar o ```font-size: 100%```
- Aplicar o ```color: red```
- Aplicar o ```font-size: 30px```, sobrescrevendo o ```font-size: 100%``` anterior.
- Aplicar o ```font-weight: bold```

>Ou seja, o navegador vai simplesmente aplicando todas as regras que ele encontrar para um elemento.

# Aula 7: Um pouquinho de posicionamento

## 7.1 Atribuindo Posicionamento em propriedades da pagina

>Podemos Posicionar alguns elementos do nosso documento HTML usando algumas propriedades como o ```Display```:

## 7.2 atribuindo css display

>**Display**: Propriedade especifica o comportamento de exibição (o tipo de caixa de renderização) de um elemento.

```css
    p {
        display: declaração; 
    }
     conteudo invisivel
```

## 7.3 Display : inline, block , inline-block, none.
>Temos 4 propriedades mais comum do **display**

- ```None``` : Permite você desativar a exibição de um elemento.
 - ```Inline```: Faz com que todos os elementos seja alinhados em uma unica linha.
- ```Block```: Faz com que todos os elementos tenha uma quebra de linha.
- ```Inline-Block```: Permite definir uma largura e altura no elemento. Além disso, com ```display: inline-block;``` , as margens superior / inferior são respeitadas.

>Uma otima imagem que representa isso
<p align="center">
<img src="http://4.bp.blogspot.com/-TiwOixlooJk/U4UyEnv_XpI/AAAAAAAACFs/NuuLz2IvoZ4/s1600/css-display-block-vs-inline-block.png" width="500" height="250">
</p>

# Aula 8: Mais seletores

## 8.1 Atribuindo novas funcionalidades ao css...

>Como vimos ali em cima varios exemplos que eu dei de css usando nomes das proprias TAGS como ```p {}```, ```div {}```, ```main {}``` e etc.

>Podemos da nomes para Cada um desses elementos o que torna bem mais legivel o nosso codigo CSS.

```css
    noticia {
        color: red;
    }
    data-post {
        color: blue;
    }
```

## 8.2 Aplicando novas regras com as Class e Id's e Verificando as diferenças entre os atributos.

>Podemos aplicar essas novas regras, no nosso documento CSS, de ```CLASS``` e ```ID's```.

>Como exemplo abaixo: Temos uma ```CLASS``` e um ```ID```.

```css
    #noticia {
        color: red;
    }
    .data-post {
        color: blue;
    }
```
>### Note que a primeira declaração está com um ```"#"```, e a segunda com um simples ```"."```

> - Como o id é um identificador, um nome para um elemento, ele **não pode se repetir na página**. Quer dizer, se repetirmos um id na página, o CSS e o JavaScript podem deixar de funcionar corretamente.

>### Quando se tem um ```"."``` siginifica que aquela declaração é um ```Class```.

> - Enquanto o **ID não pode ser repetido**, o **CLASS é feito para ser repetido**. Podemos sem nenhum problema usá-lo para agrupar varios estilos na pagina HTML.

## 8.3 Conflito entre classes e id.

>Creio que nao seja uma boa ideia usar id para estilizar, pois o estilo definido dessa forma não é reaproveitável.

>Mas existe um outro problema com o id. Se tivermos um elemento 

```html
  <div id="mensagem" class="centralizado">
        e o seguinte CSS:
  </div>

        <style>

            #mensagem {
                 margin: 0;
                 height: 200px;
            }

            .centralizado {
                 width: 700px;
                 margin: 0 auto;
            }

            div {
                 width: 350px;
                 height: 100px;
            }

        </style>
```
>Este estilo terá um elemento de ```200px de altura, 700px de largura e não centralizado```

>O seletor de id é muito mais específico que o seletor de classe ou de tag. Por isso, o estilo dele prevalece. Sendo assim, o elemento aparecerá com 200 pixels de altura e não centralizado.

>O segundo mais específico no exemplo é o seletor de classe. Ele define a largura de 700 pixels, mas não define a margem automática, pois prevalece a margem definida no id.

>Por fim, o seletor de tag, que define altura e largura, tem suas declarações sobrescritas pelos seletores de id e classe.

>Então o estilo final do elemento é 700 pixels de largura, 200 pixels de altura e não centralizado.


> - ### Outro Exemplo de Conflitos com Classes

```html
    <div class="destaque titulo-principal">

<style>
    .destaque {
        font-size: 40px;
        color: red;
    }
    .titulo-principal {
        background-color: purple;
        color: white;
    }
</style>
```
>Se fizermos um elemento com ambas as classes, o navegador precisa decidir quais propriedades de cada classe usar! O critério de desempate é qual das classes aparece por último no arquivo CSS.

>Exemplo mais facil Abaixo:
```css
div {
    background-color: red;
}
div {
    background-color: blue;
}
```

>Temos um conflito, porém Todos os elementos ```<div>``` terão fundo azul. Assim ultilizando o critério de desempate é qual das classes aparece por último no arquivo CSS

# Aula 9: Nem tudo é o que parece

## 9.1 Atribuindo transformaçoes de texto, ultilizando text-transform.

>Podemos por um tamanho na nossa fonte, com minusculo e maiusculo. Mais nao usando o ```Capslook```, e sim uma atribudo do CSS o ```text-transform```.

>A ```text-transform```: Propriedade CSS especifica como capitalizar o texto de um elemento. Ele pode ser usado para fazer o texto aparecer em maiúsculas ou minúsculas, ou com cada palavra em maiúscula.

```css
    p {
        text-transform: uppercase;
    }
    p {
        text-transform: lowercase;
    }
    p {
        text-transform: capitalize;
    }
```
>```uppercase```: DEFINE AS LETRAS MAIUSCULAS DO TEXTO.

>```lowercase```: define letra minuscula do texto.

>```capitalize```: Define As Iniciais De Cada Texto Maiusculas.

## 9.2 Adicionando Image replacement: Dentro da folha de estilo:

>```Image Replacement```: A substituição de imagem CSS é uma técnica de substituir um elemento de texto (geralmente uma tag de cabeçalho como uma ```<h1>```) por uma imagem (geralmente um logotipo).

>Como exemplo abaixo ao definir uma image do github no lugar da palavra "GitHub".

```css
.github {
    background-image: url(github.png);
}
```

>Ou seja, o browser irá mostrar uma imagem, enquanto no HTML você verá apenas o texto.

## 9.3 Image replacement e ferramentas de buscas...

 >Ferramentas de busca, ao examinarem nossos sites, levam em conta apenas o HTML.

 >Por não examinarem o CSS, as ferramentas de busca não encontrarão e, portanto, não indexarão as imagens referenciadas no CSS. Isso pode ser ou não interessante. Se usamos corretamente a técnica image replacement, apenas imagens secundárias, supérfluas para o conteúdo, serão ignoradas; as imagens mais importantes ficam no HTML e, portanto, são indexadas.

## 9.5 Aplicando e entendendo text-indent.

>O ```text-indent```: Permite regular o recuo da primeira linha de um parágrafo. Como o exemplo Abaixo:

<p align="center">
<img src="http://caelum-online-public.s3.amazonaws.com/intro-html-css/efeito-text-indent.png" width="500" height="250">
</p>

>Quando colocamos um tamanho maior que zero para essa propriedade, a primeira linha começa um pouco depois das linhas seguintes. Se colocamos um tamanho menor que zero, a primeira linha começa um pouco antes.

>Se aumentamos muito o valor do ```text-indent```, o texto pode começar fora da página.

>Se um texto tiver mais que uma palavra apenas so a primeira palavra q vai sair fora da pagina dependendo do valor que voce por no atributo.

>Um Exemplo do codigo, ate mesmo do curso, na qual estou fazendo e que esta disponivel ai no github.

```css
.icones-redes-sociais a {
    background-image: url(github.png);
    width: 40px;
    height: 40px;
    display: block;
    text-indent: -99999px;
}
```

# Aula 10: Posicionamento mais a fundo

## 10.1 Tipos de conteudos flutuantes

>Temos algumas propriedades de posicionamento no css. e uma delas que falaremos aqui é da propriedade ```FLOAT```.

>Há dois valores possíveis para ela (além do ```none```, que é o padrão): temos o ```left``` e ```right```.


## 10.2 Float right e left "Posicionando elementos a direita e esquerda"

>O ```float```: Propriedade CSS especifica que um elemento deve ser colocado ao longo do lado esquerdo ou direito de seu contêiner, permitindo que elementos de texto e sequenciais o envolvam. O elemento é removido do fluxo normal da página da web, embora continue sendo parte do fluxo

>Exemplo abaixo:

<p align="center">
<img src="https://css-tricks.com/wp-content/csstricks-uploads/web-text-wrap.png" width="500" height="250">
</p>

>```float:left``` posiciona a esquerda.

>```float:right``` posiciona a direita.

## 10.3 Propriedade  Clear no CSS.

>O ```clear```: Especifica em quais lados de um elemento elementos flutuantes não podem flutuar.

> E para isso basta apenas especificar no clear qual float queremos eliminar. E para isso existe suas propriedades que são.

- ```none```: Padrão. Permite elementos flutuantes em ambos os lados.
- ```left```: Nenhum elemento flutuante permitido no lado esquerdo.
 - ```right```: Nenhum elemento flutuante permitido no lado direito.
- ```both```: Não há elementos flutuantes permitidos no lado esquerdo ou no lado direito.

>Como exemplo: 
- se colocamos um codigo assim:

```html
<div class="primeiro">
  meu conteudo primeiro
</div>

<div class="segundo">
  meu conteudo segundo
</div>
```
- com um CSS assim :
```css
.primeiro {
    float: left;
}

.segundo {
    float: left;
    clear: left;
}
```

- vamos notar que o conteudo 1 fica acima do conteudo 2. Se removermos o ```clear:left;``` o conteudo 1 e 2 ficarao alinhados.

# Aula 11: Elementos onde queremos

## 11.1 Propriedades Position.

>Para posicionarmos elementos no nosso documento HTML, precisamos da propriedade ```position``` e suas parceiras ```top```, ```left```, ```bottom``` e ```right```. O comportamento dessas quatro últimas propriedades muda bastante de acordo com o valor passado à propriedade ```position```.

- top : Acima do elemento.
- left : A esquerda do elemento. 
- right : A direita do elemento.
- bottom : Abaixo do elemento.

## 11.2 Position > Relative.

>A propriedade ```relative``` do ```position``` a gente consegue mudar a posição do elemento de acordo com a posição original dele.

```css
img {
    position: relative;
    top: 20px;
    left: 20px;
}
```
 - OBS: Mais abaixo tem a imagem de exemplo.
 - 
## 11.3 Position > Absolute.

>A propriedade ```absolute``` do ```position```, com ele, podemos colocar um elemento onde quisermos na página. independentemente do resto do conteúdo.

```css
img {
    position: absolute;
    top: 20px;
    left: 20px;
}
```
>Abaixo temos uma imagem de Exemplo:

<p align="center">
<img src="https://i.stack.imgur.com/gz265.png" width="400" height="300">
</p>

## 11.4 Position > Fixed.

>A propriedade ```fixed``` do ```position```, Ele nos permite deixar um elemento no lugar que quisermos da janela, usando também as propriedades ```top```, ```left```, ```bottom``` e ```right``` para determinar a distância do elemento para esses quatro cantos da janela.

- Exemplo:

```css
footer {
    position: fixed;
    top: 200px;
    left: 100px;
}
```

<p align="center">
<img src="http://ptgmedia.pearsoncmg.com/images/ch21_0321703529/elementLinks/21fig10.jpg" width="400" height="350">
</p>

# Aula 12: Desafios Finais

> E por fim ate o final dessa aula todos os arquivos desenvolvido por mim durante a aula está no git.

- a uma segunda aula no momento em continuação do que estou aprendendo mais ainda do HTML5, CSS3. Provavelmente terá alguns conteudos repetidos. como o Position, vai ter mais explicação sobre ele também.. segue o link da pasta HTMLCSSII no git. <a href="https://github.com/hulkg3x/HTMLCSSII"> HTMLCSSII github</a>
