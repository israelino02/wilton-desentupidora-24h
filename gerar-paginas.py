# -*- coding: utf-8 -*-
"""Gera uma página por serviço, reaproveitando rastreamento, cabeçalho, faixa de confiança e rodapé do index."""
import io, re, os
from urllib.parse import quote

BASE = os.path.dirname(os.path.abspath(__file__))
idx = io.open(os.path.join(BASE, "index.html"), encoding="utf-8").read()

def pedaco(ini, fim):
    a = idx.index(ini); b = idx.index(fim, a) + len(fim)
    trecho = idx[a:b]
    assert len(trecho) > 50, "pedaco vazio: " + ini
    return trecho

RASTREIO = pedaco('<!-- Google Tag Manager -->', "gtag('config', 'AW-18033664704');\n</script>")
NOSCRIPT = pedaco('<!-- Google Tag Manager (noscript) -->', '<!-- End Google Tag Manager (noscript) -->')
HEADER  = pedaco('<header class="header">', '</header>')
NUMEROS = pedaco('<div class="numeros">', '</div>\n      </div>')
TRUST   = pedaco('<section class="trust"', '</section>')
FOOTER  = pedaco('<footer class="footer">', '</footer>')
def pedaco_flutuante():
    i = idx.index('class="float-wa"')
    a = idx.rindex('<a ', 0, i)
    return idx[a:idx.index('</a>', a) + 4]

FLOAT   = pedaco_flutuante()
SCRIPT  = pedaco('<script>\n(function(){', '})();\n</script>')

# nas páginas internas as âncoras do menu apontam para a home
def para_home(html):
    return re.sub(r'href="#(?!conteudo)([a-z-]+)"', r'href="index.html#\1"', html)

HEADER, FOOTER, FLOAT = para_home(HEADER), para_home(FOOTER), para_home(FLOAT)

NOME = "SOS Desentupidora"
DOMINIO = "https://sosdesentupidorasalvador.com.br"
WA = "5571996289969"
TEL = "+5571996289969"
TEL_TXT = "(71) 99628-9969"

ICONE_WA = '<svg viewBox="0 0 32 32" width="19" height="19" fill="currentColor" aria-hidden="true"><path d="M16 3C8.8 3 3 8.8 3 16c0 2.3.6 4.5 1.8 6.4L3 29l6.8-1.8c1.9 1 4 1.6 6.2 1.6 7.2 0 13-5.8 13-13S23.2 3 16 3zm0 23.6c-2 0-3.9-.5-5.5-1.5l-.4-.2-4 1.1 1.1-3.9-.3-.4a10.5 10.5 0 1 1 9.1 4.9zm5.9-7.9c-.3-.2-1.9-.9-2.2-1-.3-.1-.5-.2-.7.2s-.8 1-1 1.2c-.2.2-.4.2-.7.1a8.6 8.6 0 0 1-4.3-3.7c-.3-.6.3-.5.9-1.7.1-.2 0-.4 0-.6s-.7-1.7-1-2.3c-.2-.6-.5-.5-.7-.5h-.6c-.2 0-.6.1-.9.4-.3.4-1.2 1.2-1.2 2.8s1.2 3.2 1.4 3.5c.2.2 2.4 3.7 5.9 5.1 2.2.9 3 1 4.1.8.7-.1 2-.8 2.2-1.6.3-.8.3-1.5.2-1.6-.1-.2-.3-.3-.6-.4z"/></svg>'
ICONE_TEL = '<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.2a2 2 0 0 1 2.1-.5c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/></svg>'
SETA = '<svg viewBox="0 0 24 24" aria-hidden="true" stroke-linecap="round" stroke-linejoin="round"><path d="M15 6l-6 6 6 6"/></svg>'

DICA_SODA = "Soda cáustica é corrosiva, pode causar queimadura e, junto com água quente, danificar o cano. Se o entupimento volta mesmo depois dela, o problema costuma estar mais à frente na tubulação, e aí só o equipamento resolve."

SERVICOS = [
{
 "arq": "desentupimento-de-pia", "slug": "pia",
 "foto": "servico-pia", "alt": "Técnico desentupindo pia de cozinha com máquina",
 "titulo": "Desentupimento de Pia em Salvador 24h | " + NOME,
 "desc": "Desentupimento de pia de cozinha e de banheiro em Salvador e Região Metropolitana, 24 horas. Chegamos em 30 minutos, orçamento gratuito e garantia de 3 meses.",
 "h1": "Desentupimento de pia em Salvador",
 "sub": "Pia da cozinha ou do banheiro com água parada ou escoando devagar? A equipe vai até você com equipamento de alta pressão e passa o orçamento antes de começar.",
 "sinais_t": "Sinais de que a pia está entupindo",
 "sinais": ["Água parada na cuba",
            "Pia que demora para escoar",
            "Cheiro ruim subindo pelo ralo da pia",
            "Barulho de borbulha quando a água desce",
            "Tanque ou saída da máquina de lavar transbordando"],
 "inclui": ["Localização do ponto do entupimento",
            "Desentupimento com equipamento de alta pressão",
            "Pia de cozinha e de banheiro",
            "Tanque e saída da máquina de lavar",
            "Teste com água corrente antes da equipe sair"],
 "dica_t": "Antes de jogar soda cáustica",
 "dica": DICA_SODA,
 "msg": "Olá! Quero um orçamento de desentupimento de pia.",
},
{
 "arq": "desentupimento-de-vaso-sanitario", "slug": "vaso",
 "foto": "servico-vaso", "alt": "Técnico desentupindo vaso sanitário",
 "titulo": "Desentupimento de Vaso Sanitário em Salvador 24h | " + NOME,
 "desc": "Desentupimento de vaso sanitário em Salvador e Região Metropolitana, 24 horas, sem danificar o vaso. Chegamos em 30 minutos, com garantia de 3 meses.",
 "h1": "Desentupimento de vaso sanitário em Salvador",
 "sub": "Descarga que não desce, água subindo ou vaso que entope toda semana. Solução rápida e eficaz, sem danificar o seu vaso sanitário.",
 "sinais_t": "Quando chamar",
 "sinais": ["Água subindo quando dá a descarga",
            "Descarga que desce devagar",
            "Objeto que caiu dentro do vaso",
            "Vaso que volta a entupir com frequência",
            "Cheiro de esgoto no banheiro"],
 "inclui": ["Avaliação do vaso e da tubulação",
            "Desentupimento sem danificar o vaso",
            "Retirada de objeto caído no vaso",
            "Verificação da ligação com a rede de esgoto",
            "Teste com descarga antes da equipe sair"],
 "dica_t": "Enquanto a equipe não chega",
 "dica": "Pare de dar descarga: se a água está subindo, cada nova descarga pode transbordar. Feche o registro da caixa acoplada, que fica atrás ou do lado do vaso, e não jogue produto químico, que pode espirrar em quem for desentupir.",
 "msg": "Olá! Quero um orçamento de desentupimento de vaso sanitário.",
},
{
 "arq": "desentupimento-de-ralo", "slug": "ralo",
 "foto": "servico-ralo", "alt": "Técnico desentupindo ralo com cabo de aço",
 "titulo": "Desentupimento de Ralo em Salvador 24h | " + NOME,
 "desc": "Desentupimento de ralo de box, banheiro, área de serviço e quintal em Salvador e Região Metropolitana, 24 horas, com limpeza profunda e garantia de 3 meses.",
 "h1": "Desentupimento de ralo em Salvador",
 "sub": "Ralo do box devolvendo água no banho, cheiro ruim ou água parada no quintal. Limpeza profunda de ralos e do sistema de drenagem.",
 "sinais_t": "Sinais de ralo entupido",
 "sinais": ["Água acumulando no box durante o banho",
            "Ralo devolvendo água",
            "Cheiro de esgoto subindo pelo ralo",
            "Água parada na área de serviço ou no quintal",
            "Ralo que volta a entupir pouco tempo depois de limpo"],
 "inclui": ["Desentupimento do ralo e do cano ligado a ele",
            "Ralo de box e de banheiro",
            "Ralo de área de serviço e quintal",
            "Limpeza profunda da drenagem",
            "Teste com água corrente antes da equipe sair"],
 "dica_t": "O que mais entope ralo",
 "dica": "Cabelo, sabão e a sujeira que desce do chão. Uma tela no ralo do box segura boa parte do cabelo. Se a água volta por mais de um ralo ao mesmo tempo, o problema está na rede: conta isso na mensagem.",
 "msg": "Olá! Quero um orçamento de desentupimento de ralo.",
},
{
 "arq": "limpeza-de-caixa-de-gordura", "slug": "gordura",
 "foto": "servico-gordura", "alt": "Técnico limpando caixa de gordura",
 "titulo": "Limpeza de Caixa de Gordura em Salvador | " + NOME,
 "desc": "Limpeza completa de caixa de gordura em Salvador e Região Metropolitana, para casa, restaurante e condomínio, com equipamentos profissionais e garantia de 3 meses.",
 "h1": "Limpeza de caixa de gordura em Salvador",
 "sub": "Pia da cozinha lenta, cheiro forte no quintal e gordura voltando pelo ralo. Limpeza completa da caixa com equipamentos profissionais.",
 "sinais_t": "Sinais de caixa de gordura cheia",
 "sinais": ["Pia da cozinha escoando devagar",
            "Cheiro de gordura podre perto da caixa",
            "Gordura voltando pelo ralo da cozinha",
            "Tampa da caixa com água ou gordura por cima"],
 "inclui": ["Limpeza completa da caixa de gordura",
            "Desentupimento da ligação entre a pia e a caixa",
            "Retirada dos resíduos",
            "Atendimento para casa, restaurante e condomínio"],
 "dica_t": "De quanto em quanto tempo limpar",
 "dica": "Depende do uso. Em casa, costuma ser a cada seis meses; em restaurante, lanchonete e condomínio grande, bem mais vezes. E óleo de fritura nunca vai na pia: guarde numa garrafa e leve a um ponto de coleta.",
 "msg": "Olá! Quero um orçamento de limpeza de caixa de gordura.",
},
{
 "arq": "hidrojateamento", "slug": "hidrojato",
 "foto": "servico-hidrojato", "alt": "Hidrojateamento de alta pressão em tubulação",
 "titulo": "Hidrojateamento em Salvador | " + NOME,
 "desc": "Hidrojateamento de alta pressão para desobstrução de tubulações e rede de esgoto em Salvador e Região Metropolitana, para casa, empresa e condomínio. Atendimento 24h.",
 "h1": "Hidrojateamento em Salvador",
 "sub": "Água em alta pressão para desobstruir a tubulação e a rede de esgoto de ponta a ponta, em casa, empresa e condomínio.",
 "sinais_t": "Quando o hidrojateamento resolve",
 "sinais": ["Caixa de inspeção transbordando",
            "Água voltando por mais de um ralo ao mesmo tempo",
            "Rede de esgoto que entope com frequência",
            "Gordura e sujeira acumuladas dentro do cano",
            "Água de chuva voltando pelos ralos"],
 "inclui": ["Localização do ponto do entupimento na rede",
            "Hidrojateamento de alta pressão",
            "Rede de esgoto e tubulação",
            "Caixa de inspeção e caixa de passagem",
            "Rede de água de chuva"],
 "dica_t": "Por que alta pressão",
 "dica": "A máquina comum abre caminho no meio do entupimento. O jato de alta pressão lava a parede do cano por dentro e tira a gordura e a sujeira grudadas, por isso o entupimento demora mais a voltar.",
 "msg": "Olá! Quero um orçamento de hidrojateamento.",
},
{
 "arq": "limpa-fossa", "slug": "fossa",
 "foto": "servico-fossa", "alt": "Caminhão sugador fazendo limpeza de fossa",
 "titulo": "Limpa Fossa em Salvador e Região Metropolitana | " + NOME,
 "desc": "Limpeza completa de fossa séptica com caminhão sugador em Salvador, Lauro de Freitas, Camaçari e Simões Filho. Atendimento 24h e garantia de 3 meses.",
 "h1": "Limpa fossa em Salvador e Região Metropolitana",
 "sub": "Fossa cheia, vaso descendo devagar e mau cheiro no quintal. Limpeza completa da fossa séptica com caminhão sugador.",
 "sinais_t": "Sinais de fossa cheia",
 "sinais": ["Mau cheiro no quintal ou perto da tampa da fossa",
            "Vaso e ralos descendo devagar na casa toda",
            "Ralo borbulhando quando a água desce",
            "Terreno úmido perto da fossa",
            "Esgoto voltando depois de chuva forte"],
 "inclui": ["Limpeza completa da fossa séptica",
            "Esvaziamento com caminhão sugador",
            "Desentupimento da ligação da casa com a fossa",
            "Atendimento para casa, empresa e condomínio"],
 "dica_t": "Antes da equipe chegar",
 "dica": "Deixe a tampa da fossa à vista e avise se o caminhão consegue parar perto. Se a fossa fica nos fundos do terreno, conta na mensagem a distância até a rua, para a equipe levar a mangueira do tamanho certo.",
 "msg": "Olá! Quero um orçamento de limpa fossa.",
},
{
 "arq": "desentupimento-industrial", "slug": "industrial",
 "foto": "servico-industrial", "alt": "Desentupimento industrial em rede de esgoto",
 "titulo": "Desentupimento Industrial em Salvador | " + NOME,
 "desc": "Desentupimento industrial para empresas, indústrias, fábricas e condomínios em Salvador e Região Metropolitana: rede de esgoto, hidrojateamento, caixa de gordura e limpa fossa, 24h.",
 "h1": "Desentupimento industrial em Salvador",
 "sub": "Atendimento especializado para empresas, indústrias, fábricas e condomínios, 24 horas por dia.",
 "sinais_t": "Problemas mais comuns",
 "sinais": ["Rede de esgoto da empresa ou do prédio entupida",
            "Caixa de gordura de cozinha industrial transbordando",
            "Retorno de esgoto na garagem, no pátio ou na área comum",
            "Fossa cheia em galpão ou condomínio",
            "Mau cheiro em corredor, banheiro coletivo ou cozinha"],
 "inclui": ["Visita técnica no local",
            "Desentupimento da rede de esgoto",
            "Hidrojateamento de alta pressão",
            "Limpeza de caixa de gordura",
            "Limpa fossa com caminhão sugador"],
 "dica_t": "Como o orçamento é montado",
 "dica": "A equipe vai até o local, avalia a rede, as caixas e o histórico de entupimento, e passa o orçamento gratuito antes de começar. Como o atendimento é 24 horas, dá para fazer o serviço fora do horário de funcionamento, se for preciso.",
 "msg": "Olá! Quero uma visita técnica para a minha empresa ou condomínio.",
},
]

MODELO = '''<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">

{rastreio}

<title>{titulo}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="index, follow">
<link rel="canonical" href="{dominio}/{arq}">
<meta name="theme-color" content="#0A2230">
<link rel="icon" href="assets/favicon.png" type="image/png">
<link rel="apple-touch-icon" href="assets/icone-180.png">
<meta property="og:type" content="website">
<meta property="og:locale" content="pt_BR">
<meta property="og:site_name" content="{nome}">
<meta property="og:url" content="{dominio}/{arq}">
<meta property="og:title" content="{titulo}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{dominio}/assets/{foto}.webp">
<link rel="stylesheet" href="assets/estilo.css">
</head>
<body>
{noscript}

<a class="sr-only" href="#conteudo">Ir para o conteúdo</a>

{header}

<main id="conteudo">

<section class="page-hero">
  <div class="wrap">
    <a class="voltar" href="index.html#servicos">{seta} Todos os serviços</a>
    <h1>{h1}</h1>
    <p class="hero-sub">{sub}</p>
    <div class="hero-actions">
      <a data-cta="contato_whatsapp" data-origem="pagina_topo" data-servico="{slug}" class="btn btn-primary" href="https://wa.me/{wa}?text={msg}" target="_blank" rel="noopener">{ico_wa} Chamar no WhatsApp</a>
      <a data-cta="contato_telefone" data-origem="pagina_topo" data-servico="{slug}" class="btn btn-light" href="tel:{tel}">{ico_tel} Ligar: {tel_txt}</a>
    </div>
    {numeros}
  </div>
</section>

<section class="section section--tint">
  <div class="wrap page-grid">
    <div class="page-sinais">
      <img class="page-foto" src="assets/{foto}.webp" width="900" height="600" alt="{alt}">
      <div class="page-sinais-corpo">
        <h2>{sinais_t}</h2>
        <ul class="list">
{sinais}
        </ul>
        <p>Reconheceu algum? Manda no WhatsApp o que está acontecendo e o bairro, com foto ou vídeo se puder.</p>
      </div>
    </div>
    <div>
      <div class="page-box">
        <h2>O que está incluído</h2>
        <ul class="list">
{itens}
        </ul>
        {cta_box}
      </div>
      <div class="page-box">
        <h2>{dica_t}</h2>
        <p style="margin:0;font-size:.92rem">{dica}</p>
      </div>
    </div>
  </div>
</section>

{trust}

<section class="section section--navy">
  <div class="wrap">
    <p class="eyebrow">Onde atendemos</p>
    <h2>Salvador e Região Metropolitana</h2>
    <p>A equipe atende 24 horas, todos os dias, em toda Salvador, Lauro de Freitas, Camaçari e Simões Filho. Ficou na dúvida se atendemos o seu endereço? Chama no WhatsApp que a gente confirma.</p>
    <a data-cta="contato_whatsapp" data-origem="pagina_rodape" data-servico="{slug}" class="btn btn-primary" href="https://wa.me/{wa}?text={msg}" target="_blank" rel="noopener">{ico_wa} Chamar no WhatsApp</a>
  </div>
</section>

</main>

{footer}
{float}
{script}
</body>
</html>
'''

def lista(itens, recuo='          '):
    return "\n".join('{}<li>{}</li>'.format(recuo, i) for i in itens)

for sv in SERVICOS:
    msg = quote(sv["msg"], safe="!")
    cta_box = '<a data-cta="contato_whatsapp" data-origem="pagina_caixa" data-servico="{sv}" class="btn btn-primary btn-block" href="https://wa.me/{wa}?text={m}" target="_blank" rel="noopener">{i} Pedir orçamento</a>'.format(wa=WA, m=msg, i=ICONE_WA, sv=sv["slug"])
    html = MODELO.format(titulo=sv["titulo"], desc=sv["desc"], h1=sv["h1"], sub=sv["sub"], msg=msg, arq=sv["arq"],
                         foto=sv["foto"], alt=sv["alt"],
                         sinais_t=sv["sinais_t"], sinais=lista(sv["sinais"]), itens=lista(sv["inclui"]),
                         dica_t=sv["dica_t"], dica=sv["dica"], cta_box=cta_box, slug=sv["slug"],
                         nome=NOME, dominio=DOMINIO, wa=WA, tel=TEL, tel_txt=TEL_TXT,
                         rastreio=RASTREIO, noscript=NOSCRIPT, header=HEADER, numeros=NUMEROS, trust=TRUST,
                         footer=FOOTER, float=FLOAT, script=SCRIPT, ico_wa=ICONE_WA, ico_tel=ICONE_TEL, seta=SETA)
    caminho = os.path.join(BASE, sv["arq"] + ".html")
    io.open(caminho, "w", encoding="utf-8").write(html)
    print("gerada:", sv["arq"] + ".html", len(html), "bytes")
