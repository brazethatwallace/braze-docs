---
nav_title: "Números de telefone dos usuários"
article_title: Números de telefone dos usuários do WhatsApp
page_order: 3
description: "Este artigo de referência aborda a formatação de números de telefone do WhatsApp, como importar números de telefone e como adicionar usuários a grupos de inscrições do WhatsApp."
page_type: reference
channel:
  - WhatsApp

---

# Números de telefone dos usuários {#user-phone-numbers}

> Este artigo aborda diferentes tópicos relacionados aos números de telefone dos seus usuários ou clientes.

Os números de telefone são exibidos no perfil de usuário em formatos locais, mas não estarão no formato usado para importar o número (`(724) 123 4567`).

## Importando números de telefone {#importing-phone-numbers}

Você pode importar números de telefone [fazendo upload de um CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#constructing-your-csv) ou [via API]({{site.baseurl}}/api/endpoints/user_data/post_user_track) para criar um usuário.

### Formatação {#formatting}

É importante importar números de fora dos EUA no formato [`E.164`](https://en.wikipedia.org/wiki/e.164), incluindo o "+" e o código do país. Qualquer número de telefone que não for fornecido nesse formato será interpretado como um número dos EUA.

Se um número de telefone for convertido para o formato E.164, mas não passar na validação, a Braze não conseguirá enviar mensagens do WhatsApp para esse número. Qualquer usuário com números de telefone que não puderem ser formatados sairá automaticamente de uma etapa do Canvas que inclua WhatsApp.

Todos os números dos EUA devem ser números de telefone válidos de 10 dígitos com um código de área válido. Eles podem ser inseridos sem o `+` e o código do país, pois a Braze assumirá e mapeará todos os números válidos de 10 dígitos como números dos EUA.

Todos os números internacionais devem começar com `+`, seguido do código do país e do número de telefone. (ex.: `+442071838750`)

![Captura de tela relacionada à formatação.]({% image_buster /assets/img/sms/e164.png %}){: style="max-width:50%;border: 0;"}

No entanto, para garantir a precisão caso você esteja enviando para várias regiões com diferentes códigos de país ou área, é recomendável usar o formato `E.164`, mesmo para números de telefone dos EUA.

Você pode ver as diferenças entre a formatação de número local e a formatação universal `E.164` na tabela a seguir:

| País | Local | Código do país | `E.164` |
|---|---|---|---|
| EUA | `4155552671` | 1 | `+14155552671` |
| Reino Unido | `02071838750` | 44 | `+442071838750` |
| Brasil | `1155256325` | 55 | `+551155256325` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Formatação" }

### Adicionando usuários a um grupo de inscrições do WhatsApp {#adding-users-to-whatsapp-a-subscription-group}

Para que um cliente receba uma mensagem do WhatsApp, ele deve ter um número de telefone válido e ter feito opt-in em um grupo de inscrições. Para saber mais, consulte [Grupos de inscrições do WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups).


### Múltiplos usuários com o mesmo número de telefone {#multiple-users-with-the-same-phone-number}

Se vários usuários tiverem o mesmo número de telefone dentro de um Segment de uma única Campaign ou etapa do Canvas, a Braze fará a deduplicação do envio e enviará apenas uma mensagem para aquele número de telefone.