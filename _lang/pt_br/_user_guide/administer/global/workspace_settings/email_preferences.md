---
nav_title: Preferências de e-mail
article_title: Preferências de e-mail
page_type: reference
page_order: 2
description: "Este artigo de referência aborda as preferências de e-mail no dashboard da Braze, incluindo configurações de envio, pixels de rastreamento de abertura, páginas e rodapés da inscrição, e mais."
tool: Dashboard
channel: email
toc_headers: h2

---

# Preferências de e-mail {#email-preferences}

> Preferências de e-mail é onde você pode definir configurações específicas de e-mail de saída, como rodapés personalizados, páginas personalizadas de opt-in e descadastramento, e mais. Incluir essas opções nos seus e-mails de saída proporciona uma experiência fluida e coesa para seus usuários.

**Preferências de e-mail** pode ser encontrado em **Configurações** no dashboard.

## Configuração de envio {#sending-configuration}

As configurações de e-mail na seção **Configuração de envio** determinam quais detalhes são incluídos nas suas campanhas de e-mail. Em particular, essas configurações estão principalmente relacionadas ao que seu usuário vê quando recebe um e-mail da Braze.

### Configurações de e-mail de saída {#outbound-email-settings}

Ao configurar suas definições de e-mail, as configurações de e-mail de saída identificam quais nomes e endereços de e-mail são usados quando a Braze envia e-mails para seus usuários.

{% tabs local %}
{% tab Display Name Address %}

Nesta seção, você pode adicionar os nomes e endereços de e-mail que podem ser usados quando a Braze envia e-mails para seus usuários. Os nomes de exibição e endereços de e-mail estão disponíveis nas opções de **Sending Info** ao redigir sua Campaign de e-mail. Observe que atualizações feitas nas configurações de e-mail de saída não afetam retroativamente envios existentes.

![Seção "Outbound Email Settings" com campos para diferentes nomes de exibição e domínios.]({% image_buster /assets/img/email_settings/display_name_address.png %})

#### Personalizar com Liquid {#personalize-with-liquid}

Você também pode usar [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) nos campos **From Display Name**, **Local Part** e **Domain** para criar dinamicamente o nome do remetente e o endereço de e-mail com base em atributos personalizados. Para usar Liquid no campo **Domain**, você deve acessar as opções de **Sending Info** de uma Campaign de e-mail e marcar a caixa de seleção **Customize from display name + address**.

![Configurações de envio com campos para personalizar o nome de exibição do remetente, endereço e domínio.]({% image_buster /assets/img/email_settings/email_campaign_domain.png %})

Por exemplo, você pode usar lógica condicional para enviar de diferentes marcas ou regiões:

{% raw %}
```liquid
{% if ${language} == 'en' %}
English Display Name
{% elsif ${language} == 'de' %}
German Display Name
{% else %}
Default to English Display Name
{% endif %}
```
{% endraw %}

{% endtab %}
{% tab Reply-To Address %}

Adicionar um endereço de e-mail nesta seção permite que você o selecione como endereço de resposta para sua Campaign de e-mail. Você também pode tornar um endereço de e-mail o padrão selecionando **Make Default**. Esses endereços de e-mail estarão disponíveis nas opções de **Sending Info** ao redigir sua Campaign de e-mail.

![Seção "Reply-To Address" com campos para inserir múltiplos endereços de resposta.]({% image_buster /assets/img/email_settings/reply_to_address.png %}){: style="max-width:75%;" }

{% alert note %}
Os domínios de envio da Braze não aceitam e-mails de entrada. Se um destinatário responder a um e-mail enviado de um domínio de envio configurado pela Braze, a resposta será rejeitada com um erro `550 5.7.1 relaying denied`. O endereço de resposta não precisa compartilhar o mesmo domínio que o endereço de remetente. Se você precisa receber respostas — por exemplo, para coletar confirmações de convites de calendário — use um subdomínio que não esteja configurado para envio e que tenha uma caixa de entrada configurada para receber e-mails.
{% endalert %}

#### Personalizar com Liquid

Você também pode usar [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) no campo **Reply-To Address** para criar dinamicamente o endereço de resposta com base em atributos personalizados. Por exemplo, você pode usar lógica condicional para enviar respostas para diferentes regiões ou departamentos:

{% raw %}
```liquid
{% if {{custom_attribute.${region}}} == 'US' %}
{% assign address = "us-support@example.com" %}
{% elsif {{custom_attribute.${region}}} == 'EU' %}
{% assign address = "eu-support@example.com" %}
{% else %}
{% assign address = "global-support@example.com" %}{% endif %}{{address}}
```
{% endraw %}

{% endtab %}
{% tab BCC Address %}

Esta seção permite que você gerencie endereços BCC que podem ser adicionados a mensagens de e-mail de saída enviadas pela Braze. Adicionar um endereço BCC a uma mensagem de e-mail envia uma cópia idêntica da mensagem que seu usuário recebe para sua caixa de entrada BCC. Essa é uma ferramenta útil para manter cópias de mensagens enviadas aos seus usuários para requisitos de conformidade ou questões de suporte ao cliente. E-mails BCC não são incluídos nos relatórios e na análise de dados de e-mail.

Endereços BCC estão disponíveis para Amazon SES, SendGrid e SparkPost. Como alternativa aos endereços BCC, recomendamos usar o [arquivamento de mensagens]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/message_archiving) para salvar uma cópia das mensagens enviadas aos usuários para fins de arquivamento ou conformidade.

{% multi_lang_include alerts/important_alerts.md alert='BCC address billable emails' %}

Depois de adicionar um endereço, ele estará disponível para seleção ao redigir um e-mail em Campaigns ou etapas do Canvas. Selecione **Make Default** ao lado de um endereço para defini-lo como selecionado por padrão ao lançar uma nova Campaign de e-mail ou componente do Canvas. Para substituir isso no nível da mensagem, você pode selecionar **No BCC** ao configurar sua mensagem.

Se você exigir que todas as mensagens de e-mail enviadas pela Braze incluam um endereço BCC, pode ativar a opção **Require a BCC address for all your email campaigns**. Isso exigirá que você selecione um endereço padrão, que será automaticamente selecionado em novas Campaigns de e-mail ou etapas do Canvas. O endereço padrão também será adicionado automaticamente a todas as mensagens disparadas pela nossa REST API. Não é necessário alterar a solicitação de API existente para incluir o endereço.

#### BCC dinâmico {#dynamic-bcc}

Com o BCC dinâmico, você pode usar Liquid no seu endereço BCC. Observe que esse recurso está disponível apenas em **Preferências de e-mail** e não pode ser definido na própria Campaign. Apenas um endereço BCC por destinatário de e-mail é permitido.

Por exemplo, você pode adicionar {% raw %}`{{custom_attribute.${support_agent}}}`{% endraw %} como endereço BCC para e-mails da sua equipe de suporte.

![Seção de endereço BCC na guia de configurações de e-mail com um endereço BCC usando Liquid.]({% image_buster /assets/img/email_settings/dynamic_bcc.png %}){: style="max-width:90%;" }

{% endtab %}
{% endtabs %}

## Pixel de rastreamento de abertura {#open-tracking-pixel}

[![Curso do Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/email-open-tracking-pixel/){: style="float:right;width:120px;border:0;" class="noimgborder"}

O pixel de rastreamento de abertura de e-mail é uma imagem invisível de 1 x 1&nbsp;px que é automaticamente inserida no HTML do seu e-mail. Esse pixel ajuda a Braze a detectar se seus usuários abriram seu e-mail. Quando o cliente de e-mail de um usuário faz uma solicitação ao nosso pixel de rastreamento, a solicitação pode conter informações como endereço IP, user agent e timestamp. As informações de abertura de e-mail podem ser muito úteis, ajudando você a determinar estratégias de marketing eficazes ao entender as taxas de abertura correspondentes.

### Posicionamento {#placement}

O comportamento padrão na Braze é adicionar o pixel de rastreamento na parte inferior do seu e-mail, geralmente em uma tag `<body>`. Para a maioria dos usuários, esse é o local ideal para colocar o pixel.

Embora o pixel já esteja estilizado para causar o mínimo de alterações visuais possível, quaisquer alterações visuais não intencionais seriam menos visíveis na parte inferior de um e-mail. Esse também é o padrão para provedores de e-mail como SendGrid e SparkPost.

Para reduzir comportamentos inesperados, mantenha o Liquid dentro de tags `<html>`. Tags de nível de documento aninhadas ou duplicadas podem alterar como o e-mail é analisado e onde o pixel é posicionado, o que pode afetar o rastreamento de abertura e o layout. Para saber mais, consulte [Usando Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid).

### Atualizar o posicionamento {#update-the-placement}

A Braze atualmente suporta a substituição do local padrão do pixel de rastreamento de abertura do ESP (a última tag no `<body>` de um e-mail) para movê-lo para a primeira tag no `<body>`.

![Seção "Open Tracking Pixel" com as opções para mover para SendGrid, SparkPost ou Amazon SES.]({% image_buster /assets/img/open_pixel.png %}){: style="max-width:80%;" }

Para alterar o local:

1. Na Braze, acesse **Configurações** > **Preferências de e-mail**.
2. Selecione uma das seguintes opções: **Move for SendGrid**, **Move for SparkPost** ou **Move for Amazon SES**
3. Selecione **Save**.

Após salvar, a Braze envia instruções especiais ao ESP para posicionar o pixel de rastreamento de abertura no topo de todos os e-mails HTML.

{% alert important %}
A ativação de SSL envolve a URL do pixel de rastreamento com HTTPS em vez de HTTP. Se seu SSL estiver configurado incorretamente, isso pode afetar a eficácia do pixel de rastreamento.
{% endalert %}

{% alert important %}
O rastreamento de cliques se aplica apenas a links que começam com `http://` ou `https://`. Links `mailto:` (por exemplo `mailto:support@example.com`) não são reescritos para rastreamento.
{% endalert %}

## Cabeçalho list-unsubscribe {#list-unsubscribe}

{% alert note %}
Desde 15 de fevereiro de 2024, novas empresas têm o cabeçalho list-unsubscribe (com cancelamento de inscrição com um clique) ativado por padrão.
{% endalert %}

Usar um cabeçalho list-unsubscribe permite que seus destinatários cancelem facilmente a inscrição de e-mails de marketing exibindo um botão **Unsubscribe** na interface da caixa de e-mail, e não no corpo da mensagem.

Envios de teste normalmente **não** incluem cabeçalhos list-unsubscribe. A exibição do cabeçalho em produção depende do provedor de caixa de e-mail e é baseada na reputação — uma reputação do remetente mais forte geralmente melhora a visibilidade.

![Interface da caixa de e-mail com a opção Unsubscribe ao lado da mensagem, onde o list-unsubscribe aparece fora do corpo da mensagem.]({% image_buster /assets/img_archive/list_unsub_img1.png %}){: style="float:right;max-width:60%;margin-left:15px;"}

Quando um destinatário seleciona **Unsubscribe**, o provedor de caixa de e-mail envia a solicitação de cancelamento de inscrição para o destino definido no cabeçalho do e-mail.

Ativar o list-unsubscribe é uma prática recomendada de entregabilidade e um requisito em alguns dos principais provedores de caixa de e-mail. Isso incentiva os usuários finais a se removerem com segurança de mensagens indesejadas, em vez de clicar no botão de spam em um cliente de e-mail, o que é prejudicial para a reputação do remetente e a entregabilidade de e-mail.

Ao [gerenciar suas inscrições no Gmail](https://support.google.com/mail/answer/15621070?sjid=2292320204527911296-NC), o Gmail também pode usar o link de cancelamento de inscrição do corpo da mensagem, mas prioriza o list-unsubscribe se estiver presente no cabeçalho.

### Desativar o cabeçalho list-unsubscribe remove o botão Unsubscribe do Gmail? {#does-turning-off-the-list-unsubscribe-header-remove-the-gmail-unsubscribe-button}

Não. Desativar a configuração de cabeçalho list-unsubscribe da Braze remove o cabeçalho `List-Unsubscribe` das mensagens que a Braze envia, mas não controla se o Gmail exibe uma opção **Unsubscribe** na interface da caixa de e-mail. Conforme mencionado acima, o Gmail ainda pode exibir uma opção de cancelamento de inscrição a partir de links no corpo da mensagem ou usar outra lógica do provedor. A presença do cabeçalho na mensagem bruta é separada da exibição de uma opção de cancelamento de inscrição pelo Gmail para os destinatários. Para saber mais, consulte o [FAQ das diretrizes de remetente de e-mail do Gmail](https://support.google.com/a/answer/14229414).

### Suporte de provedores de caixa de e-mail {#mailbox-provider-support}

A tabela a seguir resume o suporte dos provedores de caixa de e-mail para cabeçalho "mailto:", URL de list-unsubscribe e cancelamento de inscrição com um clique ([RFC 8058](https://datatracker.ietf.org/doc/html/rfc8058)).

| Cabeçalho list-unsubscribe | Cabeçalho mailto: | URL de list-unsubscribe | Cancelamento de inscrição com um clique (RFC 8058) |
| ----- | --- | --- | --- |
| Gmail | Suportado* | Suportado | Suportado |
| Gmail Mobile | Não suportado | Não suportado | Não suportado |
| Apple Mail | Suportado | Não suportado | Não suportado |
| Outlook.com | Suportado | Não suportado | Não suportado |
| Yahoo! Mail | Suportado* | Não suportado | Suportado |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Suporte de provedores de caixa de e-mail" }

_*Yahoo e Gmail estão descontinuando gradualmente o cabeçalho "mailto:" e suportarão apenas o cancelamento com um clique._

A exibição do cabeçalho é determinada em última instância pelo provedor de caixa de e-mail. Para verificar se o cabeçalho list-unsubscribe está incluído no e-mail bruto (texto) para o destinatário no Gmail, faça o seguinte:

1. Selecione **Show Original** no e-mail. Isso abre uma nova aba com a versão bruta do e-mail e seus cabeçalhos.
2. Pesquise por "List-Unsubscribe". Para o cancelamento de inscrição com um clique, muitos provedores também incluem um cabeçalho "List-Unsubscribe-Post". Confirme que ambos aparecem na mensagem bruta quando você espera que o cancelamento com um clique esteja disponível.

Se o cabeçalho estiver na versão bruta do e-mail mas não for exibido, o provedor de caixa de e-mail decidiu não mostrar a opção de cancelamento de inscrição, o que significa que não temos mais informações sobre por que o provedor não está exibindo o cabeçalho. A exibição do cabeçalho list-unsubscribe é baseada na reputação. Na maioria dos casos, quanto melhor sua reputação do remetente com o provedor de caixa de e-mail, mais provável é que o cabeçalho list-unsubscribe apareça.

### Cabeçalho de cancelamento de inscrição de e-mail em espaços de trabalho {#email-unsubscribe-header-in-workspaces}

![Selecionando "users who are subscribed or opted in" para quais usuários enviar.]({% image_buster /assets/img/email_settings/email_unsub_header_workspaces.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

Quando o recurso de cabeçalho de cancelamento de inscrição de e-mail está ativado, essa configuração se aplica a todo o espaço de trabalho, não ao nível da empresa. Ela é adicionada a Campaigns e Canvas que estão configurados para enviar a usuários inscritos ou com opt-in, ou apenas usuários com opt-in, na etapa **Público-alvo** dos construtores de Campaign e Canvas.

Ao usar o "padrão do espaço de trabalho", a Braze não adiciona o cabeçalho de cancelamento de inscrição com um clique para Campaigns consideradas transacionais, que são configuradas para "enviar a todos os usuários, incluindo usuários cancelados". Para substituir isso e adicionar o cabeçalho de cancelamento de inscrição com um clique ao enviar para usuários cancelados, você pode selecionar **Unsubscribe globally from all emails** nas configurações de list-unsubscribe com um clique no nível da mensagem.

### Cabeçalho list-unsubscribe padrão {#default-list-unsubscribe-header}

{% alert important %}
O Gmail pretende que os remetentes implementem o cancelamento de inscrição com um clique para todas as suas mensagens comerciais e promocionais de saída a partir de 1º de junho de 2024. Para saber mais, consulte as [diretrizes de remetente do Gmail](https://support.google.com/mail/answer/81126?hl=en#subscriptions&zippy=%2Crequirements-for-sending-or-more-messages-per-day:~:text=Make%20it%20easy%20to%20unsubscribe) e o [FAQ das diretrizes de remetente de e-mail do Gmail](https://support.google.com/a/answer/14229414#zippy=%2Cwhat-time-range-or-duration-is-used-when-calculating-spam-rate%2Cif-the-list-header-is-missing-is-the-message-body-checked-for-a-one-click-unsubscribe-link%2Cif-unsubscribe-links-are-temporarily-unavailable-due-to-maintenance-or-other-reasons-are-messages-flagged-as-spam%2Ccan-a-one-click-unsubscribe-link-to-a-landing-or-preferences-page%2Cwhat-is-a-bulk-sender%2Chow-can-bulk-senders-make-sure-theyre-meeting-the-sender-guidelines%2Cdo-the-sender-guidelines-apply-to-messages-sent-to-google-workspace-accounts%2Cdo-the-sender-guidelines-apply-to-messages-sent-from-google-workspace-accounts%2Cwhat-happens-if-senders-dont-meet-the-requirements-in-the-sender-guidelines%2Cif-messages-are-rejected-because-they-dont-meet-the-sender-guidelines-do-you-send-an-error-message-or-other-alert%2Cwhat-happens-when-sender-spam-rate-exceeds-the-maximum-spam-rate-allowed-by-the-guidelines%2Cwhat-is-the-dmarc-alignment-requirement-for-bulk-senders%2Cif-messages-fail-dmarc-authentication-can-they-be-delivered-using-ip-allow-lists-or-spam-bypass-lists-or-will-these-messages-be-quarantined%2Ccan-bulk-senders-get-technical-support-for-email-delivery-issues%2Cdo-all-messages-require-one-click-unsubscribe:~:text=for%20mitigations.-,Unsubscribe%20links,-Do%20all%20messages). O Yahoo anunciou um cronograma para o início de 2024 para a atualização dos requisitos. Para saber mais, consulte [Mais seguro, menos spam: aplicando padrões de e-mail para uma experiência melhor](https://blog.postmaster.yahooinc.com/).
{% endalert %}

Para usar o recurso de cancelamento de inscrição da Braze para processar cancelamentos diretamente, selecione **Include a one-click list-unsubscribe (mailto and HTTP) email header for emails sent to subscribed or opted-in users** e selecione **Braze default** como a URL padrão da Braze e mail-to.

![Opção para incluir automaticamente um cabeçalho list-unsubscribe para e-mails enviados a usuários inscritos ou com opt-in.]({% image_buster /assets/img/email_settings/email_unsubscribe_header.png %})

A Braze suporta as seguintes versões do cabeçalho list-unsubscribe:

| Versão do list-unsubscribe | Descrição |
| ----- | --- |
| Um clique (RFC 8058) | Oferece uma maneira direta para os destinatários cancelarem a inscrição de e-mails com um único clique. Este é um requisito do Yahoo e Gmail para remetentes em massa. |
| URL de list-unsubscribe ou HTTPS | Fornece aos destinatários um link que os direciona a uma página web onde podem cancelar a inscrição. |
| Mailto | Especifica um endereço de e-mail como destino para a mensagem de solicitação de cancelamento de inscrição a ser enviada do destinatário para a marca. <br><br> _Para processar solicitações de cancelamento de inscrição via mailto list-unsubscribe, essas solicitações precisam incluir o endereço de e-mail conforme armazenado na Braze para o usuário final que está cancelando a inscrição. Isso pode ser fornecido pelo "from-address" do e-mail de onde o usuário final está cancelando a inscrição, pelo assunto codificado ou pelo corpo codificado do e-mail recebido pelo usuário final do qual está cancelando a inscrição. Em casos muito limitados, alguns provedores de caixa de entrada não aderem ao protocolo [RFC 2368](https://datatracker.ietf.org/doc/html/rfc2368), resultando no endereço de e-mail não sendo passado corretamente. Isso pode fazer com que uma solicitação de cancelamento de inscrição não possa ser processada na Braze._ |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Cabeçalho list-unsubscribe padrão" }

Quando a Braze recebe uma solicitação de list-unsubscribe de um usuário por qualquer um dos métodos acima, o estado global de inscrição de e-mail desse usuário é definido como cancelado. Se não houver correspondência, a Braze não processa essa solicitação.

### Cancelamento de inscrição com um clique {#one-click-unsubscribe}

Usar o cancelamento de inscrição com um clique para o cabeçalho list-unsubscribe ([RFC 8058](https://datatracker.ietf.org/doc/html/rfc8058)) foca em fornecer uma maneira fácil para os destinatários cancelarem a inscrição de e-mails.

### List-unsubscribe com um clique no nível da mensagem {#message-level-one-click-list-unsubscribe}

A configuração de list-unsubscribe com um clique no nível da mensagem substitui o recurso de cabeçalho de cancelamento de inscrição de e-mail definido para espaços de trabalho. Aplique o comportamento de cancelamento de inscrição com um clique por Campaign ou etapa do Canvas para os seguintes usos:

- Adicionar um cancelamento de inscrição com um clique da Braze para um grupo de inscrições específico, para suportar múltiplas marcas/listas dentro de um espaço de trabalho
- Alternar entre o cancelamento de inscrição padrão da Braze ou URL personalizada
- Adicionar sua URL personalizada de cancelamento de inscrição com um clique
- Omitir o cancelamento de inscrição com um clique nesta mensagem

{% alert note %}
A configuração de list-unsubscribe com um clique no nível da mensagem está disponível apenas ao usar o editor de arrastar e soltar e o editor de HTML atualizado. Se você estiver usando o editor de HTML anterior, mude para o editor de HTML atualizado para usar esse recurso.
{% endalert %}

No seu editor de e-mail, acesse **Sending Settings** > **Sending Info**. Selecione uma das seguintes opções:

- **Use workspace default**: Usa as configurações de **Email Unsubscribe Header** definidas em **Preferências de e-mail**. Quaisquer alterações feitas nessa configuração se aplicam a todas as mensagens.
- **Unsubscribe globally from all emails**: Usa o cabeçalho padrão de cancelamento de inscrição com um clique da Braze. Usuários que clicam no botão de cancelamento de inscrição têm seu estado global de inscrição de e-mail definido como "Unsubscribed".
- **Unsubscribe from specific subscription group**: Usa o grupo de inscrições especificado. A Braze cancela a inscrição dos usuários que clicam no botão de cancelamento de inscrição do grupo de inscrições selecionado.
    - Ao selecionar um grupo de inscrições, adicione o filtro **Subscription Group** em **Target Audiences** para direcionar apenas usuários que estão inscritos nesse grupo específico. O grupo de inscrições selecionado para o cancelamento de inscrição com um clique deve corresponder ao grupo de inscrições que você está direcionando. Se houver uma incompatibilidade no grupo de inscrições, você pode correr o risco de enviar para um usuário que está tentando cancelar a inscrição de um grupo de inscrições do qual já está cancelado.

{% alert important %}
A configuração **Unsubscribe from specific subscription group** se aplica apenas ao cabeçalho list-unsubscribe com um clique. O cabeçalho mailto list-unsubscribe não é afetado ao selecionar essa opção. Isso significa que um destinatário que cancela a inscrição usando esse método registra um cancelamento global, não um cancelamento do grupo de inscrições específico. Para excluir o cabeçalho mailto list-unsubscribe do cancelamento global de inscrição dos usuários ao selecionar essa configuração, entre em contato com o [Suporte]({{site.baseurl}}/support_contact).
{% endalert %}

- **Custom**: Adiciona sua URL personalizada de cancelamento de inscrição com um clique para você processar cancelamentos diretamente.
- **Exclude unsubscribe**

{% alert important %}
Excluir o cancelamento de inscrição com um clique ou qualquer mecanismo de cancelamento de inscrição deve ser feito apenas para mensagens transacionais, como redefinições de senha, recibos e e-mails de confirmação.
{% endalert %}

Ajustar essa configuração substitui o comportamento padrão para list-unsubscribe com um clique neste e-mail.

![Configurações de envio no editor de e-mail com opções de list-unsubscribe com um clique no nível da mensagem, incluindo padrão do espaço de trabalho e URL personalizada.]({% image_buster /assets/img/email_settings/one_click_list_unsubscribe_message_level.png %}){: style="max-width:70%;"}

#### Requisitos {#requirements}

Se você está enviando e-mails usando sua própria funcionalidade personalizada de cancelamento de inscrição, deve atender aos seguintes requisitos para garantir que a URL de cancelamento de inscrição com um clique que você configurou esteja em conformidade com a RFC 8058:

* A URL deve ser capaz de processar solicitações POST de cancelamento de inscrição.
* A URL deve começar com `https://`.
* A URL não deve retornar um redirecionamento HTTPS ou um corpo. Links de cancelamento de inscrição com um clique que direcionam para uma landing page ou outro tipo de página web não estão em conformidade com a RFC 8058.
* Solicitações POST não devem definir cookies.

Selecione **Custom list-unsubscribe header** para adicionar seu próprio endpoint de cancelamento de inscrição com um clique configurado e um "mailto:" opcional. A Braze requer uma entrada para URL para suportar um cabeçalho list-unsubscribe personalizado porque o cancelamento de inscrição com um clique via HTTP é um requisito do Yahoo e Gmail para remetentes em massa.

![Preferências de e-mail com campos de cabeçalho list-unsubscribe personalizado para uma URL de cancelamento de inscrição com um clique e mailto opcional.]({% image_buster /assets/img/email_settings/email_unsubscribe_header_custom.png %}){: style="max-width:80%;"}

## Adicionar prefixo às linhas de assunto de e-mail {#append-email-subject-lines}

Use a opção para incluir "[TEST]" e "[SEED]" nas linhas de assunto dos seus e-mails de teste e seed. Isso pode ajudar a identificar quaisquer campanhas de e-mail enviadas como testes.

![Opção de preferência de e-mail do espaço de trabalho que adiciona prefixos TEST e SEED às linhas de assunto de e-mails de teste e seed.]({% image_buster /assets/img/email_settings/test_and_seed_email_subject_line.png %}){: style="max-width:70%;"}

## CSS inline em novos e-mails por padrão {#inline-css-on-new-emails-by-default}

CSS inline é uma técnica que automaticamente aplica estilos CSS inline para seus e-mails e novos e-mails. Para alguns clientes de e-mail, isso pode melhorar a forma como seus e-mails são renderizados.

Alterar essa configuração não afeta nenhuma das suas mensagens de e-mail ou modelos existentes. Você pode substituir esse padrão a qualquer momento ao redigir mensagens ou modelos. Para saber mais, consulte [CSS inline]({{site.baseurl}}/user_guide/channels/email/html_editor/css_inline).

## Reinscrever usuários quando o e-mail muda {#resubscribe-users-when-their-email-changes}

Você pode reinscrever automaticamente os usuários quando eles alteram seu endereço de e-mail. Por exemplo, se um usuário do espaço de trabalho que cancelou a inscrição anteriormente alterar seu endereço de e-mail para um que não está na lista de cancelamento de inscrição da Braze, ele será automaticamente reinscrito.

![Configuração do espaço de trabalho que reinscreve automaticamente os usuários quando seu endereço de e-mail muda.]({% image_buster /assets/img/email_settings/resubscribe_users.png %}){: style="max-width:90%;" }

## Páginas e rodapés da inscrição {#subscription-pages-and-footers}

{% tabs local %}
{% tab Rodapé personalizado %}

Para e-mails comerciais, a [Lei CAN-SPAM](https://en.wikipedia.org/wiki/CAN-SPAM_Act_of_2003) exige que todos os e-mails comerciais incluam uma opção de cancelamento de inscrição. Com as configurações de rodapé personalizado, você pode permanecer em conformidade com a CAN-SPAM enquanto também personaliza seu rodapé de descadastramento de e-mail. Para permanecer em conformidade, você deve adicionar seu rodapé personalizado a todos os e-mails enviados como parte de Campaigns para este espaço de trabalho.

Observe os seguintes requisitos ao criar um rodapé personalizado para suas mensagens de e-mail:
- Deve incluir uma URL de cancelamento de inscrição e endereço postal físico.
- Deve ter menos de 100 KB.

![Editor de rodapé personalizado de e-mail com campos de link de cancelamento de inscrição e endereço postal para conformidade com a CAN-SPAM.]({% image_buster /assets/img/email_settings/custom_footer.png %})

Para saber mais sobre a modelagem Liquid de rodapé personalizado, consulte [Rodapés personalizados]({{site.baseurl}}/user_guide/channels/email/subscriptions#changing-email-subscriptions).

{% endtab %}
{% tab Página de cancelamento de inscrição personalizada %}

A Braze permite que você defina uma **Página de cancelamento de inscrição personalizada** com seu próprio HTML. Esta página aparece depois que um usuário seleciona cancelar a inscrição na parte inferior de um e-mail. Observe que esta página deve ter menos de 750 KB.

![Editor de HTML e pré-visualização da página de cancelamento de inscrição personalizada exibida após o usuário cancelar a inscrição de e-mail.]({% image_buster /assets/img/email_settings/custom_unsubscribe.png %})

Saiba mais sobre as práticas recomendadas para gerenciamento de listas de e-mail em [Gerenciando inscrições de e-mail]({{site.baseurl}}/user_guide/channels/email/faq#unsubscribed-email-addresses).

{% endtab %}
{% tab Página de opt-in personalizada %}

Você pode criar uma página personalizada de opt-in usando seu próprio HTML. Incluir isso nos seus e-mails pode ser especialmente benéfico se você quiser que sua marca e mensagem permaneçam consistentes ao longo do ciclo de vida do usuário. Observe que esta página deve ter menos de 750 KB.

![Editor de HTML e pré-visualização da página de opt-in personalizada para confirmação de inscrição de e-mail com a marca.]({% image_buster /assets/img/email_settings/custom_opt_in.png %})

Saiba mais sobre as práticas recomendadas para gerenciamento de listas de e-mail em [Gerenciando inscrições de e-mail]({{site.baseurl}}/user_guide/channels/email/faq#unsubscribed-email-addresses).

{% endtab %}
{% endtabs %}

{% alert tip %}
Quando estiver na seção **Pré-visualização** de uma página de inscrição ou rodapé, selecione **Copy preview link** para gerar e copiar um link de pré-visualização compartilhável que mostra como o rodapé do e-mail, a página de cancelamento de inscrição ou a página de opt-in aparece para um usuário aleatório. O link dura sete dias antes de precisar ser regenerado.
{% endalert %}

## Perguntas frequentes {#frequently-asked-questions}

### Cancelamento de inscrição com um clique

{% details A URL de cancelamento de inscrição com um clique (via cabeçalho list-unsubscribe) pode direcionar para uma Central de Preferências? %}
Não, isso não está em conformidade com a RFC 8058, o que significa que você não estará em conformidade com o requisito de cancelamento de inscrição com um clique do Yahoo e Gmail.
{% enddetails %}

{% details Por que recebo a mensagem de erro "Your email body does not include an unsubscribe link" ao redigir minha Central de Preferências? %}
Uma Central de Preferências não é considerada um link de cancelamento de inscrição. Seus destinatários de e-mail devem ter a opção de cancelar a inscrição de quaisquer e-mails comerciais para permanecer em conformidade com a CAN-SPAM.
{% enddetails %}

{% details Preciso editar Campaigns de e-mail e Canvas anteriores para aplicar a configuração de cancelamento de inscrição com um clique após ativá-la? %}
Se você não tem nenhum dos casos de uso para a configuração de list-unsubscribe com um clique no nível da mensagem, não há ação necessária desde que a configuração esteja ativada em **Preferências de e-mail**. A Braze adiciona automaticamente os cabeçalhos de cancelamento de inscrição com um clique a todas as mensagens de marketing e promocionais de saída. No entanto, se você precisar configurar o comportamento de cancelamento de inscrição com um clique no nível da mensagem, deve atualizar as Campaigns de e-mail e etapas do Canvas anteriores adequadamente.
{% enddetails %}

{% details Posso ver o cabeçalho list-unsubscribe e de cancelamento de inscrição com um clique na mensagem original ou nos dados brutos, mas por que não vejo o botão Unsubscribe no Gmail ou Yahoo? %}
O Gmail e o Yahoo decidem em última instância se exibem ou não o cabeçalho list-unsubscribe ou de cancelamento de inscrição com um clique. Para novos remetentes ou remetentes com baixa reputação do remetente, isso pode ocasionalmente fazer com que o botão de cancelamento de inscrição não seja exibido.
{% enddetails %}

{% details O cabeçalho personalizado de cancelamento de inscrição com um clique suporta Liquid? %}
Sim, Liquid e lógica condicional são suportados para permitir URLs dinâmicas de cancelamento de inscrição com um clique para o cabeçalho.
{% enddetails %}

{% alert tip %}
Se você estiver adicionando lógica condicional, evite ter valores de saída que adicionem espaços em branco à sua URL, pois a Braze não remove esses espaços.
{% endalert %}

### List-unsubscribe com um clique no nível da mensagem

{% details Se eu adicionar os cabeçalhos de e-mail para cancelamento com um clique manualmente, e tiver o cabeçalho de cancelamento de inscrição de e-mail ativado, qual é o comportamento esperado? %}
Os cabeçalhos de e-mail adicionados para list-unsubscribe com um clique se aplicam a todos os envios futuros desta Campaign.
{% enddetails %}

{% details Por que os grupos de inscrições precisam corresponder entre as variantes da mensagem para lançar? %}
Para uma Campaign com testes A/B, a Braze envia aleatoriamente uma das variantes para o usuário. Se você tiver dois grupos de inscrições diferentes definidos na mesma Campaign (a Variante A está definida para o Grupo de inscrições A e a Variante B está definida para o Grupo de inscrições B), não podemos garantir que os usuários inscritos apenas no Grupo de inscrições B recebam a Variante B. Pode haver um cenário em que os usuários estão cancelando a inscrição de um grupo de inscrições do qual já cancelaram.
{% enddetails %}

{% details A configuração de cabeçalho de cancelamento de inscrição de e-mail está desativada em Preferências de e-mail, mas nas informações de envio da minha Campaign, a configuração de list-unsubscribe com um clique está definida como "Use workspace default". Isso é um bug? %}
Não. Se a configuração do espaço de trabalho estiver desativada e a configuração da mensagem estiver definida como **Use workspace default**, a Braze segue o que está configurado em **Preferências de e-mail**. Isso significa que não adicionamos o cabeçalho de cancelamento de inscrição com um clique para a Campaign.
{% enddetails %}

{% details O que acontece se um grupo de inscrições for arquivado? Isso quebra o cancelamento de inscrição com um clique em e-mails enviados? %}
Se um grupo de inscrições referenciado em **Sending Info** para cancelamento com um clique for arquivado, a Braze ainda processa os cancelamentos de inscrição do cancelamento com um clique. O grupo de inscrições não aparece mais no dashboard (filtro de Segment, perfil de usuário e áreas similares).
{% enddetails %}

{% details A configuração de cancelamento de inscrição com um clique está disponível para modelos de e-mail? %}
Não, atualmente não temos planos de adicionar isso para modelos de e-mail, pois esses modelos não são atribuídos a um domínio de envio. Se você tem interesse nesse recurso para modelos de e-mail, envie um [feedback de produto]({{site.baseurl}}/user_guide/administer/personal/product_portal).
{% enddetails %}

{% details Esse recurso verifica se a URL de cancelamento de inscrição com um clique adicionada à opção personalizada é válida? %}
Não, não verificamos ou validamos nenhum link no dashboard da Braze. Certifique-se de testar adequadamente sua URL antes do lançamento.
{% enddetails %}