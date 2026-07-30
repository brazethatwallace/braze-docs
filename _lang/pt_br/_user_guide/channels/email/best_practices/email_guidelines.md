---
nav_title: "Diretrizes de e-mail"
article_title: "Diretrizes de e-mail"
page_order: 1
page_type: reference
description: "Este artigo aborda dicas gerais e boas práticas para ter em mente ao criar campanhas de e-mail para diversos casos de uso e tópicos."
channel: email

---

# Diretrizes de e-mail {#email-guidelines}

> Ao criar sua campanha de e-mail, é importante considerar como suas mensagens são recebidas pelos seus diversos usuários e provedores de e-mail (ESPs).

## Geral {#general}

Aqui estão algumas dicas rápidas para ter em mente ao criar seu conteúdo:

- Ao formatar seu e-mail, use folhas de estilo inline como CSS.
- Para usar um único modelo de e-mail para versões mobile e desktop, mantenha a largura abaixo de 500 pixels.
- As imagens devem ter menos de 5&nbsp;MB. Recomendamos usar PNG, JPEG ou GIF para máxima compatibilidade. Evite SVG e WebP, pois muitos dos principais clientes de e-mail ainda não oferecem suporte a esses formatos.
- Não defina alturas e larguras para imagens, pois isso pode causar espaços em branco desnecessários em um e-mail degradado.
- Tags `div` não devem ser usadas, pois a maioria dos clientes de e-mail não oferece suporte ao seu uso. Em vez disso, use tabelas aninhadas.
- Evite usar JavaScript porque ele não funciona com nenhum provedor de serviços de e-mail.
- Evite `position: absolute` e `position: relative` em CSS nos modelos de e-mail. A maioria dos clientes de e-mail não oferece suporte a posicionamento CSS, causando discrepâncias de layout entre a prévia da Braze e os e-mails entregues. Use layouts baseados em tabelas para obter efeitos de camadas ou sobreposição.
- A Braze melhora os tempos de carregamento usando uma rede de distribuição de conteúdo (CDN) global para hospedar todas as imagens de e-mail.
- No mobile, as colunas de imagem são estreitas (~100px cada), então linhas com múltiplas imagens ainda cabem (por exemplo, quatro imagens ≈ quatro colunas utilizáveis).

## Texto alternativo {#alternative-text}

Como os filtros de spam verificam tanto a versão HTML quanto a versão em texto simples de uma mensagem, utilizar alternativas em texto simples é uma ótima maneira de reduzir sua pontuação de spam. Além disso, o texto alternativo `(alt="")` pode servir para complementar e, em alguns casos, substituir imagens incluídas no corpo do seu e-mail que podem ter sido filtradas pelo provedor de e-mail do usuário. Leitores de tela anunciam o texto alternativo para explicar imagens, então essa é uma oportunidade de usar linguagem simples para fornecer informações importantes sobre uma imagem.

{% alert note %}
Se o seu texto alternativo contiver aspas, use aspas simples (`'`) em vez de aspas duplas (`"`). Aspas duplas podem fazer com que o HTML feche o atributo prematuramente, cortando o texto. Por exemplo, `alt="Product 'Premium' Edition"` funciona corretamente, mas `alt="Product "Premium" Edition"` é truncado.
{% endalert %}

## Validação de e-mail {#email-validation}

{% alert important %}
A validação é usada para endereços de e-mail do dashboard, endereços de e-mail de usuários finais (seus clientes) e endereços de remetente e de resposta de uma mensagem de e-mail.
{% endalert %}

A validação de e-mail acontece quando o endereço de e-mail de um usuário é atualizado ou importado para a Braze pela API, upload de CSV, SDK, ou modificado no dashboard. Note que seus endereços de e-mail não podem incluir espaços em branco e, se enviados pela API, espaços em branco podem resultar em um erro `400`.

Os endereços de e-mail direcionados pelos servidores da Braze devem ser validados de acordo com os padrões [RFC 2822](https://datatracker.ietf.org/doc/html/rfc2822). A Braze não aceita determinados caracteres e os reconhece como inválidos. Se um e-mail sofrer bounce, a Braze marca o e-mail como inválido e o status de inscrição não é alterado.

Para informações sobre caracteres não permitidos e regras de validação de e-mail, consulte [Validação de e-mail]({{site.baseurl}}/user_guide/channels/email/email_setup/email_validation#how-it-works).

## Endereços de remetente e de resposta {#from-and-reply-to-addresses}

Ao configurar seus endereços de remetente, verifique se o domínio do e-mail de remetente corresponde ao seu domínio de envio (como `marketing.yourdomain.com`). Não fazer isso pode resultar em desalinhamento de SPF e DKIM. Todos os e-mails de resposta podem ser configurados para o seu domínio raiz.

{% alert note %}
A codificação Unicode não é compatível com endereços de remetente.
{% endalert %}

## Anexos em e-mail {#attachments}

Ao adicionar anexos a mensagens de e-mail, siga estas boas práticas de entregabilidade:

- Filtros de spam verificam anexos e podem sinalizar sua mensagem
- Provedores de e-mail às vezes demoram mais para aceitar mensagens que incluem anexos
- Fora de mensagens individuais, anexos podem fazer sua mensagem parecer arriscada na caixa de entrada.
- Mantenha cada anexo abaixo de 2&nbsp;MB.
- Não envie informações sensíveis como anexo. Em vez disso, direcione os usuários ao seu portal seguro para visualizá-las lá.

## Layout (arrastar e soltar e HTML personalizado) {#layout-drag-and-drop-and-custom-html}

O layout pode quebrar quando o HTML/CSS gerado pela Braze entra em conflito com HTML personalizado. Se isso acontecer, faça o seguinte:

- Remova o HTML/CSS personalizado primeiro
- Valide se as fontes personalizadas carregam corretamente na prévia
- Verifique o preenchimento (padding) de linhas e colunas
- Prefira layouts baseados em tabelas e mantenha-se dentro da largura do editor.

Content Blocks que importam HTML de fora do editor também podem quebrar o layout.

## Parâmetros UTM em URLs de e-mail {#utm-parameters-in-email-urls}

Os parâmetros UTM marcam URLs para análise de dados. Você pode criá-los com Liquid e atributos personalizados.

- Use apenas um ponto de interrogação `?` na URL final (caracteres `?` adicionais podem quebrar as requisições).
- Evite espaços e caracteres especiais nos valores (use `_` ou `-`).
- Confirme se sua ferramenta de análise de dados processa UTMs. Remova espaços extras dentro dos blocos `capture` do Liquid. Os UTMs diferenciam maiúsculas de minúsculas.

### Verifique os detalhes do HTML {#check-html-details}

Tenha em mente que algumas tags e atributos HTML não são permitidos, pois podem permitir a execução de código malicioso no navegador.

Confira as listas a seguir para ver as tags e atributos HTML que não são permitidos nos seus e-mails:
{% details Expandir para ver as tags HTML não permitidas %}
- `<!doctype>`
- `<applet>`
- `<bgsound>`
- `<embed>`
- `<frameset>`
- `iframe`
- `<ilayer>`
- `<layer>`
- `<link>`
- `<meta>`
- `<object>`
- `<script>`
- `<title>`
- `<xml>`
- `<svg>`
{% enddetails %}

{% details Expandir para ver os atributos HTML não permitidos %}
- `<animationend>`
- `<animationiteration>`
- `<animationstart>`
- `<data-bind>`
- `<fscommand>`
- `<onabort>`
- `<onabort>`
- `<onactivate>`
- `<onafterprint>`
- `<onafterupdate>`
- `<onbeforeactivate>`
- `<onbeforecopy>`
- `<onbeforecut>`
- `<onbeforedeactivate>`
- `<onbeforeeditfocus>`
- `<onbeforepaste>`
- `<onbeforeprint>`
- `<onbeforeunload>`
- `<onbeforeupdate>`
- `<onbegin>`
- `<onblur>`
- `<onbounce>`
- `<oncanplay>`
- `<oncanplaythrough>`
- `<oncellchange>`
- `<onchange>`
- `<onclick>`
- `<oncontextmenu>`
- `<oncontrolselect>`
- `<oncopy>`
- `<oncut>`
- `<ondataavailable>`
- `<ondatasetchanged>`
- `<ondatasetcomplete>`
- `<ondblclick>`
- `<ondeactivate>`
- `<ondrag>`
- `<ondragdrop>`
- `<ondragend>`
- `<ondragenter>`
- `<ondragleave>`
- `<ondragover>`
- `<ondragstart>`
- `<ondrop>`
- `<ondurationchange>`
- `<onemptied>`
- `<onend>`
- `<onended>`
- `<onerror>`
- `<onerror>`
- `<onerrorupdate>`
- `<onfilterchange>`
- `<onfinish>`
- `<onfocus>`
- `<onfocusin>`
- `<onfocusout>`
- `<onhashchange>`
- `<onhelp>`
- `<oninput>`
- `<oninvalid>`
- `<onkeydown>`
- `<onkeypress>`
- `<onkeyup>`
- `<onlayoutcomplete>`
- `<onload>`
- `<onloadeddata>`
- `<onloadedmetadata>`
- `<onloadstart>`
- `<onlosecapture>`
- `<onmediacomplete>`
- `<onmediaerror>`
- `<onmessage>`
- `<onmousedown>`
- `<onmouseenter>`
- `<onmouseleave>`
- `<onmousemove>`
- `<onmouseout>`
- `<onmouseover>`
- `<onmouseup>`
- `<onmousewheel>`
- `<onmove>`
- `<onmoveend>`
- `<onmovestart>`
- `<onoffline>`
- `<ononline>`
- `<onopen>`
- `<onoutofsync>`
- `<onpagehide>`
- `<onpageshow>`
- `<onpaste>`
- `<onpause>`
- `<onplay>`
- `<onplaying>`
- `<onpopstate>`
- `<onprogress>`
- `<onpropertychange>`
- `<onratechange>`
- `<onreadystatechange>`
- `<onredo>`
- `<onrepeat>`
- `<onreset>`
- `<onresize>`
- `<onresizeend>`
- `<onresizestart>`
- `<onresume>`
- `<onreverse>`
- `<onrowdelete>`
- `<onrowexit>`
- `<onrowinserted>`
- `<onrowsenter>`
- `<onscroll>`
- `<onsearch>`
- `<onseek>`
- `<onseeked>`
- `<onseeking>`
- `<onselect>`
- `<onselectionchange>`
- `<onselectstart>`
- `<onshow>`
- `<onstalled>`
- `<onstart>`
- `<onstop>`
- `<onstorage>`
- `<onsubmit>`
- `<onsuspend>`
- `<onsyncrestored>`
- `<ontimeerror>`
- `<ontimeupdate>`
- `<ontoggle>`
- `<ontouchcancel>`
- `<ontouchend>`
- `<ontouchmove>`
- `<ontouchstart>`
- `<ontrackchange>`
- `<onundo>`
- `<onunload>`
- `<onurlflip>`
- `<onvolumechange>`
- `<onwaiting>`
- `<onwheel>`
- `<seeksegmenttime>`
- `<transitionend>`
{% enddetails %}