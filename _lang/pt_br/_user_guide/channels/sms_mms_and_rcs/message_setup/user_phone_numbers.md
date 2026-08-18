---
nav_title: "Números de telefone dos usuários"
article_title: Números de telefone dos usuários de SMS
page_order: 3
description: "Este artigo de referência aborda a formatação de números de telefone para SMS, como importar números de telefone e como adicionar usuários a grupos de inscrições de SMS."
page_type: reference
alias: /user_phone_numbers/
channel:
  - SMS
  - MMS
  - RCS
---

# Números de telefone dos usuários {#user-phone-numbers}

> Este artigo aborda diferentes tópicos relacionados aos números de telefone dos seus usuários ou clientes. Se você está procurando informações sobre seus próprios números, acesse nosso artigo sobre [números de telefone de envio]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sender_setup).

## Formato recomendado {#recommended-format}

Recomendamos importar números de telefone no formato [`E.164`](https://en.wikipedia.org/wiki/e.164) para garantir a precisão caso você esteja enviando para várias regiões com diferentes códigos de país ou de área&#8212;mesmo para números de telefone dos EUA.

- **Números dos EUA:** Todos os números dos EUA devem ser números de telefone válidos de 10 dígitos com um código de área válido. Se algum número de 10 dígitos estiver sem o `+` e o código do país, a Braze o mapeará como número dos EUA. Números de telefone de Porto Rico ainda exigem o `+` e o código do país, mesmo usando o formato de 10 dígitos com códigos de área no estilo dos EUA.
- **Números internacionais:** Todos os números internacionais devem começar com `+`, seguido do código do país e do número de telefone. Por exemplo, `+442071838750`.

![Exemplo de um número de telefone internacional válido no formato E.164.]({% image_buster /assets/img/sms/e164.png %}){: style="max-width:50%;border: 0;"}

Veja alguns exemplos mostrando as diferenças entre o formato local e o formato `E.164`:

| País | Local | Código do país | `E.164` |
|---|---|---|---|
| EUA | `4155552671` | 1 | `+14155552671` |
| Reino Unido | `2071838750` | 44 | `+442071838750` |
| Brasil | `1155256325` | 55 | `+551155256325` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Formato recomendado" }

## Importar números de telefone {#import-phone-numbers}

Ao importar números de telefone, é importante seguir o [formato recomendado](#recommended-format). Para importar números de telefone, use um dos seguintes métodos:

- [Fazer upload de um CSV para a Braze]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#constructing-your-csv)
- [Usar o endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track)

{% alert important %}
Os números de telefone dos usuários aparecem na Braze como uma string de dígitos. Se você importar um número que contenha caracteres não numéricos (como `,`, `-` ou `(`) além do {% raw %}`+`{% endraw %} inicial, os caracteres não numéricos serão removidos quando renderizados na Braze. Por exemplo, importar `+1 (724) 123-4567` aparecerá como `+17241234567`.
{% endalert %}

## Validação de número de telefone {#phone-number-validation}

A Braze usa a biblioteca [libphonenumber](https://github.com/google/libphonenumber) do Google para validar números de telefone. Quando novos prefixos de números de celular são introduzidos, o suporte é adicionado conforme a biblioteca upstream é atualizada. A Braze não mantém uma lista separada de prefixos válidos.

### Tratamento de números de telefone inválidos {#handling-invalid-phone-numbers}

Quando um número de telefone é considerado inválido, a Braze marca o número de telefone do usuário como inválido e não tenta enviar mais comunicações para esse número. Um número de telefone inválido é marcado na **guia Engajamento** do perfil de usuário.

![Exemplo de mensagem de erro para números de telefone inválidos na Braze.]({% image_buster /assets/img/sms/invalid_banner.png %}){: style="max-width:50%;border: 0;"}

Um número de telefone é considerado inválido pelos seguintes motivos:

- **Erro do provedor**: um erro permanente foi recebido do provedor de SMS e RCS. Isso indica que o número de telefone fornecido está formatado incorretamente ou é permanentemente incapaz de receber mensagens SMS ou RCS.
- **Desativado**: o número de telefone foi desativado porque um assinante móvel encerrou seu serviço e liberou o número da operadora (e pode eventualmente ser reciclado e atribuído a um novo usuário). Um número de telefone desativado pode ser marcado como inválido mesmo que você não tenha enviado nenhuma mensagem SMS ou RCS para esse número.

Esses números de telefone inválidos podem ser gerenciados usando [endpoints de SMS e RCS]({{site.baseurl}}/api/endpoints/sms).

{% alert note %}
Se vários perfis de usuário tiverem o mesmo número de telefone e esse número for marcado como inválido, todos os perfis de usuário existentes com esse número serão exibidos como inválidos. Perfis de usuário recém-criados nunca serão inicialmente marcados como inválidos.
{% endalert %}

Você também pode incluir ou excluir usuários com números de telefone inválidos ao [criar um segmento]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment#step-4-add-filters-to-your-segment).

## Excluir envios de SMS rejeitados da segmentação {#exclude-rejected-sms-sends-from-segmentation}

{% alert important %}
As rejeições de SMS podem contar para a sua cota de SMS, dependendo do seu contrato com a Braze e do provedor de SMS. Para informações sobre faturamento, consulte [Relatórios]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/reporting).
{% endalert %}

Para excluir usuários com envios de SMS rejeitados dos seus Segments, use [extensões de segmento SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments) e faça o seguinte:

1. Acesse **Público** > **Extensões de Segmento**.
2. Selecione **Create New Extension** > **Full refresh** ou **Incremental refresh**.
3. Escreva uma consulta SQL que identifique usuários com rejeições de SMS. Por exemplo, você pode consultar o evento `USERS_MESSAGES_SMS_REJECTION_SHARED` para encontrar usuários que receberam rejeições de SMS.
4. Salve sua extensão de segmento.
5. Ao criar seu Segment de SMS, adicione um filtro para excluir os usuários dessa extensão de segmento.

## Adicionar usuários a grupos de inscrições de SMS e RCS {#add-users-to-sms-and-rcs-subscription-groups}

Para que um usuário receba uma mensagem SMS ou RCS, ele precisa ter um número de telefone válido e ter feito a aceitação em um grupo de inscrições. Os grupos de inscrições estão vinculados ao programa de SMS ou RCS que você está executando (certifique-se de seguir os [requisitos legais para SMS, MMS e RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations) e de ter registrado o consentimento de cada cliente). Para saber mais, consulte [Grupos de inscrições de SMS e RCS]({{site.baseurl}}/sms_rcs_subscription_groups).

## Fornecimento e verificação por terceiros {#third-party-sourcing-and-verification}

A Braze utiliza ferramentas de terceiros para identificar números inválidos. A Braze não é responsável por interrupções ou informações incorretas desses serviços. Portanto, essa ferramenta não deve ser utilizada como seu único método de conformidade para verificar números inválidos.

## Captura de número de telefone {#phone-number-capture}

Para capturar números de telefone por meio de mensagens no app, consulte [Captura de número de telefone]({{site.baseurl}}/phone_number_capture).