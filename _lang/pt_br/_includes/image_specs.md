{% if include.variable_name == "image behavior" %}


| Disposição | Comportamento |
| --- | --- |
| Imagem e texto | Imagens altas ou estreitas serão reduzidas e centralizadas horizontalmente. Imagens largas serão cortadas nas bordas esquerda e direita. |
| Somente imagem | A mensagem será redimensionada para se ajustar a imagens com a maioria das proporções. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Table" }

{% endif %}

{% if include.variable_name == "payload size" %}

Recomendamos os seguintes tamanhos de carga útil:

| Sistema de envio de mensagens | Carga útil recomendada |
| --- | --- |
| iOS (pré-iOS 8) | 0,256 KB |
| iOS (pós-iOS 8) | 2 KB |
| Android (FCM) | 4 KB |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Table" }

{% endif %}

{% if include.variable_name == "in-app messages" %}

As mensagens modais no app são projetadas para se ajustarem ao dispositivo nas melhores e mais preenchidas proporções possíveis, mantendo-se fiéis ao tamanho e às proporções da imagem ou do texto escolhido para a mensagem.

Embora não haja limites para o número de caracteres de texto que você pode incluir em uma mensagem no app (assim como botões, título, corpo principal e outros), recomendamos moderação na quantidade de texto. O excesso de texto exigirá que os usuários expandam e rolem a mensagem.

Todas as mensagens no app têm um tamanho de imagem recomendado de 500 KB, tamanho máximo de imagem de 5 MB e suportam os tipos de arquivo PNG, JPEG e GIF. Imagens WebP não são suportadas em todos os dispositivos ou navegadores; sugerimos converter imagens WebP para PNG ou JPEG antes de adicioná-las às mensagens no app.

{% tabs %}
{% tab Portrait %}

| Tipo | Proporção | Qualidade da imagem | Notas |
| --- | --- | --- | --- |
| Retrato em tela inteira com texto | 6:5 | Alta resolução 1200 x 1000 px <br>Resolução mínima 600 x 500 px | O corte pode ocorrer em todos os lados, mas a imagem sempre preencherá os 50% superiores da janela de visualização. |
| Retrato em tela inteira (somente imagem, com ou sem botões) | 3:5 | Alta resolução 1200 x 2000 px <br> Resolução mínima 600 x 1000 px | O corte pode ocorrer nas bordas esquerda e direita em dispositivos mais altos. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Table" }

{% endtab %}
{% tab Landscape %}

| Tipo | Proporção | Qualidade da imagem | Notas |
| --- | --- | --- | --- |
| Paisagem em tela inteira com texto | 10:3 | Alta resolução 2000 x 600 px <br>Resolução mínima 1000 x 300 px | O corte pode ocorrer em todos os lados, mas a imagem sempre preencherá os 50% superiores da janela de visualização. |
| Paisagem em tela inteira (somente imagem, com ou sem botões) | 5:3 | Alta resolução 2000 x 600 px <br> Resolução mínima 1000 x 600 px | O corte pode ocorrer nas bordas esquerda e direita em dispositivos mais altos. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Table" }

{% endtab %}
{% tab Slideup %}

| Tipo | Proporção | Qualidade da imagem | Notas |
| --- | --- | --- | --- |
| Slideup | 1:1 | Alta resolução 150 x 150 px <br> Resolução mínima 50 x 50 px | Imagens de várias proporções caberão em um contêiner de imagem quadrado, sem corte. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Table" }

{% endtab %}
{% tab Modal %}

| Tipo | Proporção | Qualidade da imagem | Notas |
| --- | --- | --- | --- |
| Modal (somente imagem) | 1:1 | Resolução máxima recomendada: 1200 x 2000 px <br> Resolução mínima: 600 x 600 px | A mensagem será redimensionada para se ajustar a imagens com a maioria das proporções. A resolução máxima recomendada tem uma proporção de 3:5, o que pode não fornecer resultados ideais. Embora imagens maiores sejam utilizáveis, elas podem levar a tempos de carregamento mais longos. <br> A proporção ideal para imagens é 1:1. Não atender a essa proporção pode disparar um aviso durante o upload. Esse aviso é uma sugestão para melhores resultados e não impede o upload de imagens maiores. |
| Modal com texto | 29:10 | Alta resolução 1450 x 500 px <br> Resolução mínima 600 x 205 px | Imagens altas serão reduzidas e centralizadas horizontalmente. Imagens largas serão cortadas nas bordas esquerda e direita. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Table" }

{% endtab %}
{% endtabs %}

{% endif %}

{% if include.variable_name == "push notifications" %}

| Tipo de mensagem | Comprimento máximo da mensagem | Comprimento máximo do título |
| --- | --- | --- |
| Tela de bloqueio do iOS | 175 caracteres | 43 caracteres |
| Notificação do iOS | 175 caracteres | 43 caracteres |
| Alerta de banner do iOS | 85 caracteres | 43 caracteres |
| Tela de bloqueio do Android | 49 caracteres | 43 caracteres |
| Gaveta de notificação do Android | 597 caracteres | 43 caracteres |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Table" }

O tamanho de imagem recomendado para todas as imagens push é de 500 KB.

<style>
table td {
    word-break: break-word;
}
</style>

<table aria-label="Table">
  <thead>
    <tr>
      <th>Tipo de imagem</th>
      <th>Proporção</th>
      <th>Pixels máximos</th>
      <th>Tamanho máximo da imagem</th>
      <th>Tipos de arquivo</th>
      <th>Notas</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>iOS</td>
      <td>2:1 (recomendado)</td>
      <td>1038 x 1038</td>
      <td>5 MB</td>
      <td>PNG, JPEG, GIF</td>
      <td>A partir de janeiro de 2020, as notificações Rich push do iOS podem lidar com imagens de 1038 x 1038 px, desde que tenham menos de 10 MB, mas recomendamos usar o menor tamanho de arquivo possível. Na prática, o envio de arquivos grandes pode causar estresse desnecessário na rede e tornar os tempos limite de download mais comuns.<br><br>Para saber mais, consulte <a href="{{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/">notificações Rich do iOS</a>.</td>
    </tr>
    <tr>
      <td>Ícone push do Android</td>
      <td>1:1</td>
      <td>N/D</td>
      <td>500 KB</td>
      <td>PNG, JPEG</td>
      <td></td>
    </tr>
    <tr>
      <td>Imagem de notificação expandida do Android</td>
      <td>2:1</td>
      <td><b>Pequeno:</b><br>512 x 256<br><br><b>Médio:</b><br>1024 x 512<br><br><b>Grande:</b><br>2048 x 1024</td>
      <td>500 KB</td>
      <td>PNG, JPEG</td>
      <td>Usado em <a href="{{site.baseurl}}/user_guide/message_building_by_channel/push/android/rich_notifications/">notificações Rich do Android</a>.</td>
    </tr>
    <tr>
      <td>Imagem inline do Android</td>
      <td>3:2</td>
      <td>N/D</td>
      <td>N/D</td>
      <td>PNG, JPEG</td>
      <td>Para mais detalhes, consulte <a href="{{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/inline_image_push/">push de imagem inline para Android</a>.</td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4  .reset-td-br-5 .reset-td-br-6 aria-label="Table" }

{% endif %}

{% if include.variable_name == "email" %}

| Tipo de e-mail | Propriedades máximas recomendadas |
| --- | --- |
| Somente texto | 25 KB |
| Texto com imagens | 60 KB |
| Largura do e-mail | 600 px |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Table" }

| Especificações da imagem | Propriedades máximas recomendadas |
| --- | --- |
| Tamanho | 5 MB |
| Largura | Cabeçalho: 600 px<br>Corpo: 480 px |
| Tipos de arquivo | PNG, JPEG, GIF<br><br> O suporte a imagens WebP varia entre os clientes de e-mail. Para uma renderização confiável, converta imagens WebP para PNG ou JPEG antes de adicioná-las às mensagens de e-mail. |
{: .reset-td-br_1 .reset-td-br-2 aria-label="Table" }

| Especificações de texto | Propriedades máximas recomendadas |
| --- | --- |
| Comprimento da linha de assunto | 35 caracteres<br>6 a 10 palavras |
| Comprimento do `"From: Name"` | 25 caracteres |
| Comprimento do pré-cabeçalho | 85 caracteres |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Table" }

{% endif %}

{% if include.variable_name == "content cards" %}

| Tipo de cartão | Proporção     | Qualidade da imagem       |
| --------- | ---------------- | ------------------- |
| Clássico   | Proporção 1:1 | 60 x 60&nbsp;px        |
| Com legenda | Proporção 4:3 | Largura mínima de 600&nbsp;px |
| Banner    | Qualquer proporção | Largura mínima de 600&nbsp;px |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Table" }

Para saber mais, consulte os [detalhes de criação dos Content Cards]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details/).

{% endif %}

{% if include.variable_name == "WhatsApp images" %}

Essas especificações se aplicam a cabeçalhos de modelo, mensagens de mídia de resposta e mensagens de imagem.

| Propriedade | Especificações | Notas |
|---|---|---|
| Formatos suportados | JPEG, PNG | A Meta oficialmente suporta apenas JPEG e PNG para mensagens de imagem. WebP é suportado apenas para stickers (não para mensagens de imagem padrão). |
| Tamanho máximo do arquivo | 5 MB | |
| Modo de cor | 8 bits, RGB ou RGBA | |
| Legenda (somente mensagens de imagem) | Opcional; máximo de 1.024 caracteres | |
| Dimensões recomendadas | 1.125 × 600 px | Recomendamos usar imagens JPEG ou PNG com 1.125×600 px (1.91:1) para uma renderização consistente entre dispositivos e conformidade com os requisitos da Meta. |
| Proporção recomendada | 1.91:1 (largo) | Formatos quadrado (1:1) e largo (16:9) são aceitos, mas as imagens podem ser cortadas ou ampliadas dependendo do dispositivo do usuário.<br><br> Para cartões de carrossel, as imagens de cabeçalho são automaticamente cortadas para uma proporção larga pelo WhatsApp, a menos que não haja texto no corpo. Nesse caso, a imagem é renderizada como quadrada.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Table" }

{% endif %}

{% if include.variable_name == "WhatsApp videos" %}

As especificações a seguir se aplicam a cabeçalhos de modelo, mensagens de mídia de resposta, mensagens de vídeo e cabeçalhos de cartões de carrossel.

| Propriedade | Especificações |
|---|---|
| Formatos suportados | MP4, 3GPP |
| Tamanho do arquivo | Máximo de 16 MB |
| Codec de vídeo | Somente H.264 |
| Codec de áudio | Somente AAC |
| Faixas de áudio | Uma única faixa de áudio ou sem faixa de áudio |
| Legenda (somente mensagens de vídeo) | Opcional; máximo de 1.024 caracteres |
| Proporção recomendada | 1.91:1 (largo) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Table" }

{% multi_lang_include alerts/important_alerts.md alert='Meta MP4 video issue' %}

{% endif %}