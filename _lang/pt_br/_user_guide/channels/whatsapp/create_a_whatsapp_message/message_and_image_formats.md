---
nav_title: Formatos de mensagem e imagem
article_title: Formatos de mensagem e imagem do WhatsApp
description: "Este artigo de referência aborda a estrutura de mensagens, limites de componentes e requisitos de ativos de mídia para criar mensagens e modelos do WhatsApp."
alias: /whatsapp_media_formats/
page_order: 9
channel:
  - WhatsApp
---

# Formatos de mensagem e imagem do WhatsApp {#whatsapp-message-and-image-formats}

> Aqui estão os requisitos de estrutura de mensagem, componentes e ativos de mídia para criar mensagens e modelos do WhatsApp.

Existem dois tipos de mensagens do WhatsApp na Braze: [mensagens de modelo](#template-messages) e [mensagens de resposta](#response-messages).

| Tipo de mensagem | Quando é usado | Aprovação da Meta |
|---|---|---|
| Mensagens de modelo | Comunicação iniciada pela empresa; enviada a qualquer momento | Obrigatória; os modelos devem ser enviados à Meta e aprovados antes do envio. |
| Mensagens de resposta | Respostas a mensagens iniciadas pelo usuário; apenas dentro da janela de conversa de 24 horas | Não obrigatória |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Formatos de mensagem e imagem do WhatsApp" }

As mensagens de modelo devem ser enviadas à Meta para aprovação, o que pode levar até 24 horas. Após a aprovação, elas podem ser enviadas a qualquer momento. As mensagens de resposta (chamadas de "mensagens de sessão" na documentação da Meta) só podem ser enviadas enquanto uma janela de conversa ativa estiver aberta — dentro de 24 horas da última mensagem recebida do usuário.

## Mensagens de modelo {#template-messages}

As mensagens de modelo do WhatsApp são formatos de mensagem pré-aprovados usados para comunicação iniciada pela empresa. Na Braze, elas são construídas a partir de componentes que você define antes de enviar à Meta. Todas as mensagens de modelo são baseadas em categorias: marketing, utilidade ou autenticação.

### Modelos de marketing {#marketing-templates}

Os modelos de marketing são o tipo mais comum usado na Braze. Eles consistem em até quatro componentes:

| Componente | Obrigatório | Notas |
|---|---|---|
| Cabeçalho | Não | Suporta texto, imagem, vídeo, documento ou localização. Consulte [Especificações de mídia](#media-specifications) para requisitos de tipo de arquivo, tamanho e dimensões. |
| Corpo | Sim | O conteúdo principal da mensagem |
| Rodapé | Não | Texto complementar exibido abaixo do corpo |
| Botões | Não | Inclua até 10 botões (todos os tipos de botão são suportados) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Modelos de marketing" }

#### Comprimento de caracteres {#character-length}

| Componente | Comprimento máximo de caracteres |
|---|---|
| Corpo | 1.024 caracteres |
| Rodapé | 60 caracteres |
| Rótulo do botão (URL, telefone, resposta rápida) | 25 caracteres |
| Número de telefone (no botão de telefone) | 20 caracteres |
| Nome do modelo | 512 caracteres (apenas letras minúsculas, alfanuméricos e underscores) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Comprimento de caracteres" }

#### Tipos de botão {#button-types}

| Tipo de botão | Comportamento | Notas |
|---|---|---|
| Resposta rápida | Envia o texto do rótulo do botão como resposta na conversa | |
| URL | Abre uma URL no navegador padrão do usuário; suporta 1 variável adicionada ao final da URL (máximo de 2.000 caracteres) | |
| Número de telefone | Inicia uma chamada para o número de telefone especificado | |
| Copiar código de cupom | Copia um código de cupom para a área de transferência do usuário | Sempre requer aprovação da Meta |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Tipos de botão" }

#### Formatação de parâmetros {#parameter-formatting}

As variáveis de modelo podem usar parâmetros nomeados (como {% raw %}`{{first_name}}`{% endraw %}) ou parâmetros posicionais (como {% raw %}`{{1}}`{% endraw %}). Na Braze, as variáveis podem ser substituídas por Liquid ou texto simples. Sempre inclua valores padrão para variáveis Liquid; mensagens com valores de variáveis ausentes não serão enviadas.

### Modelos de oferta por tempo limitado {#limited-time-offer-templates}

Os modelos de oferta por tempo limitado exibem uma oferta promocional com prazo definido, com uma contagem regressiva opcional conforme a oferta se aproxima do vencimento. Use esse layout para promoções com prazo determinado, como vendas sazonais ou ofertas personalizadas com base em um atributo do usuário.

| Componente | Obrigatório | Notas |
|---|---|---|
| Cabeçalho | Não | Selecione **Nenhum** ou adicione mídia (imagem ou vídeo). Consulte [Especificações de mídia](#media-specifications) para requisitos de tipo de arquivo, tamanho e dimensões. |
| Detalhes da oferta | Sim | Título da oferta, código da oferta e um vencimento opcional. |
| Corpo | Sim | O conteúdo principal da mensagem. Suporta Liquid. |
| Rodapé | Não | Texto complementar exibido após o corpo. |
| Botões | Sim | **Copiar código da oferta** é incluído automaticamente. Você pode adicionar um botão **Visitar website**; nenhum outro tipo de botão é suportado para esse tipo de modelo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Modelos de oferta por tempo limitado" }

#### Detalhes da oferta {#offer-details}

| Campo | Obrigatório | Notas |
|---|---|---|
| Título | Sim | Uma linha curta descrevendo a oferta. |
| Código | Sim | O código da oferta que os destinatários irão copiar. Isso preenche o botão **Copiar código da oferta** automaticamente. |
| Vencimento | Não | Defina uma data e hora fixas (por exemplo, uma data de término para uma promoção de verão) ou personalize com base em um atributo do usuário (por exemplo, o aniversário de cada usuário). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Detalhes da oferta" }

Se você definir um vencimento, os destinatários verão uma contagem regressiva na mensagem que é atualizada conforme a oferta se aproxima do fim. Por exemplo, a mensagem pode inicialmente mostrar a data de término e depois mudar para algo como "Faltam 5 dias" quando a data de término estiver mais próxima. Se você não definir um vencimento, a oferta será exibida sem contagem regressiva. A Braze impede o envio de mensagens quando o vencimento já passou (por exemplo, se o vencimento for 1º de novembro de 2026, mas o horário de envio for 15 de novembro de 2026).

#### Tipos de botão

| Tipo de botão | Notas |
|---|---|
| Copiar código da oferta | Incluído automaticamente. O texto do botão é "Copy offer code" e não pode ser editado. |
| Visitar website | O único outro botão que você pode adicionar. Máximo de 1. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Tipos de botão de oferta por tempo limitado" }

### Modelos de carrossel de cartões de mídia {#media-card-carousel-templates}

Os modelos de carrossel exibem um corpo de mensagem seguido de 2 a 10 cartões de produto roláveis horizontalmente, cada um com seu próprio ativo de mídia e botões. Eles estão disponíveis apenas para mensagens de modelo de marketing.

#### Mensagem de nível superior {#top-level-message}

| Componente | Obrigatório | Propriedades máximas | Notas |
|---|---|---|---|
| Texto do corpo | Sim | 1.024 caracteres | Suporta variáveis |
| Cartões | Sim | 2-10 cartões | A quantidade de cartões é fixa na criação do modelo. Um modelo de carrossel aprovado só pode ser enviado com o número exato de cartões definido durante a criação. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Mensagem de nível superior" }

#### Especificações por cartão {#per-card-specifications}

| Componente | Obrigatório | Notas |
|---|---|---|
| Cabeçalho (imagem ou vídeo) | Sim | Todos os cartões devem usar o mesmo formato (todos imagem ou todos vídeo). Isso inclui a mesma estrutura de componente; você não pode misturar cartões com e sem texto do corpo ou botões.<br><br> Os ativos de cabeçalho dos cartões são automaticamente cortados para uma proporção larga com base no dispositivo do usuário. |
| Texto do corpo | Não | Se qualquer cartão incluir texto do corpo, todos os cartões devem incluir texto do corpo |
| Botões | Não | Máximo de 2 botões por cartão |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Especificações por cartão" }

#### Comprimento de caracteres por cartão {#per-card-character-lengths}

| Componente | Comprimento máximo de caracteres | Notas |
|---|---|---|
| Texto do corpo do cartão | 160 caracteres | |
| Rótulo do botão | 25 caracteres | |
| Número de telefone (no botão de telefone) | 20 caracteres | |
| URL (no botão de URL) | 2.000 caracteres; suporta 1 variável adicionada ao final | Botões de URL abrem no navegador padrão do usuário, fora do WhatsApp. Nenhum webhook de pedido ou conversão é disparado a partir desse ponto. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Comprimento de caracteres por cartão" }

## Mensagens de resposta {#response-messages}

As mensagens de resposta (também chamadas de "mensagens de sessão" pela Meta) só podem ser enviadas dentro da janela de conversa de 24 horas. Elas são abertas e redefinidas quando um usuário envia uma mensagem para a sua empresa.

As mensagens de resposta compostas diretamente no editor de Campaign ou Canvas da Braze não requerem aprovação da Meta.

A Braze suporta sete layouts de mensagem de resposta:

| Layout de mensagem | Descrição |
|---|---|
| Texto | Texto simples do corpo da mensagem |
| Mídia | Mensagem com anexo de imagem, vídeo, áudio ou documento |
| Resposta rápida | Mensagem com até 3 botões de resposta tocáveis |
| Botão de chamada para ação (CTA) | Mensagem com um botão de URL ou botão de número de telefone |
| Mensagem de lista | Mensagem com uma lista estruturada e rolável de opções selecionáveis |
| Mensagem de fluxo | Mensagem que solicita aos usuários que preencham um formulário ou tarefa interativa no WhatsApp, com o resultado retornando para a Braze |
| Mensagem de produto Meta | Mensagem que destaca um único produto, múltiplos produtos ou um catálogo inteiro de um catálogo Meta conectado |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Mensagens de resposta" }

### Componentes de mensagem de lista {#list-message-components}

| Componente | Propriedades máximas |
|---|---|
| Texto do corpo | 4.096 caracteres |
| Rótulo do botão (para abrir a lista) | 20 caracteres |
| Número de seções | Até 10 |
| Número de linhas por seção | Até 10 |
| Título da seção | 24 caracteres |
| Título da linha | 24 caracteres |
| Descrição da linha | 72 caracteres |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Componentes de mensagem de lista" }

### Componentes de resposta rápida {#quick-reply-components}

| Componente | Propriedades máximas |
| --- | --- |
| Botão | Até 3 |
| Rótulo do botão | 20 caracteres por botão |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Componentes de resposta rápida" }

## Especificações de mídia {#media-specifications}

As especificações a seguir se aplicam a todas as mídias em cabeçalhos de modelos do WhatsApp, mensagens de resposta ou mensagens de mídia independentes.

{% multi_lang_include alerts/important_alerts.md alert='WhatsApp audio and documents' %}

### Imagens {#images}

{% multi_lang_include channels/image_specs.md variable_name='WhatsApp images' %}

### Vídeo {#video}

{% multi_lang_include channels/image_specs.md variable_name='WhatsApp videos' %}

#### Compatibilidade com Android {#android-compatibility}

O perfil H.264 "High" codificado com B-frames não é suportado em clientes WhatsApp para Android. Use o perfil H.264 "Main" sem B-frames ou o perfil "Baseline" para a maior compatibilidade. Se estiver recodificando com ffmpeg, use a flag `-movflags faststart` para posicionar os boxes `moov` antes dos boxes `mdat`.

### Áudio {#audio}

As especificações a seguir se aplicam a mensagens de mídia de resposta e mensagens de áudio, e são baseadas no tipo de áudio: mensagem de voz ou mensagem de áudio básica.

#### Mensagem de voz {#voice-message}

Uma mensagem de voz funciona como uma nota de voz gravada, com controles de reprodução e suporte a transcrição.

| Propriedade | Especificações |
|---|---|
| Formato obrigatório | Apenas OGG |
| Codec obrigatório | Apenas OPUS (entrada mono) |
| Tamanho do arquivo | Máximo de 16 MB |
| Ícone de reprodução | Este ícone só aparece se o arquivo tiver 512 KB ou menos; arquivos maiores exibem um ícone de download |
| Transcrição | Exibida automaticamente se o usuário tiver ativado as transcrições de voz do WhatsApp |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Mensagem de voz" }

#### Mensagem de áudio básica {#basic-audio-message}

As especificações a seguir se aplicam ao compartilhamento padrão de arquivos de áudio (clipes de música, anúncios em áudio e arquivos de som).

| Formato | Extensão | Tamanho máximo do arquivo | Notas |
|---|---|---|---|
| AAC | .aac | 16 MB | |
| AMR | .amr | 16 MB | |
| MP3 | .mp3 | 16 MB | |
| MP4 Audio | .m4a | 16 MB | |
| OGG (codec OPUS) | .ogg | 16 MB | Arquivos OGG devem usar o codec OPUS. O formato base `audio/ogg` sem OPUS não é suportado.<br><br> Arquivos OGG/OPUS enviados como mensagens de áudio básicas exibirão um ícone de microfone (igual às mensagens de voz) em vez de um ícone de música. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Mensagem de áudio básica" }

#### Considerações {#considerations}

{% multi_lang_include alerts/important_alerts.md alert='WhatsApp audio and documents' %}

- Não há suporte a legendas para mensagens de áudio.
- Um erro comum é a incompatibilidade de tipos MIME. Verifique se o tipo MIME do seu arquivo corresponde à sua extensão antes de enviar.

### Documentos {#documents}

As especificações a seguir se aplicam a cabeçalhos de modelos (formato de documento), mensagens de mídia de resposta e mensagens de documento.

| Tipo de documento | Tipos de arquivo | Tamanho máximo do arquivo |
|---|---|---|
| PDF | PDF | 100 MB |
| Microsoft Word | DOC, DOCX | 100 MB |
| Microsoft Excel | XLS, XLSX | 100 MB |
| Microsoft PowerPoint | PPT, PPTX | 100 MB |
| Texto simples | TXT | 100 MB |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Documentos" }

#### Considerações

{% multi_lang_include alerts/important_alerts.md alert='WhatsApp audio and documents' %}

- Legendas são opcionais e podem ter no máximo 1.024 caracteres.
- O nome do arquivo é opcional. O WhatsApp usa a extensão do arquivo para determinar qual ícone de documento exibir na conversa.
- Apenas os formatos listados são oficialmente suportados. Outros tipos de arquivo podem ser enviados, mas não há garantia de que serão renderizados corretamente no WhatsApp.

## Referência rápida: especificações de mídia do WhatsApp {#quick-reference-whatsapp-media-specifications}

| Tipo de mídia | Tipos de arquivo | Tamanho máximo do arquivo | Disponibilidade de legenda |
|---|---|---|---|
| Imagem | JPEG, PNG | 5 MB | Sim (máximo de 1.024 caracteres) |
| Vídeo | MP4, 3GPP | 16 MB | Sim (máximo de 1.024 caracteres) |
| Áudio (voz) | OGG (OPUS) | 16 MB | Não |
| Áudio (básico) | AAC, AMR, MP3, M4A, OGG | 16 MB | Não |
| Documento | PDF, DOC, DOCX, XLS, XLSX, PPT, PPTX, TXT | 100 MB | Sim (máximo de 1.024 caracteres) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Referência rápida: especificações de mídia do WhatsApp" }