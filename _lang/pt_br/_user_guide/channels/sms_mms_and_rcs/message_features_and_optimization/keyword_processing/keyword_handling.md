---
nav_title: Tratamento de palavras-chave personalizadas
article_title: Tratamento de palavras-chave personalizadas
page_order: 2
description: "Este artigo de referência aborda como a Braze lida com mensagens bidirecionais de SMS, MMS e RCS e respostas automáticas. Inclui explicações sobre como funciona o acionamento por palavras-chave, bem como categorias de palavras-chave personalizadas e suporte multilíngue."
page_type: reference
channel:
  - SMS
  - MMS
  - RCS

---

# Tratamento de palavras-chave personalizadas {#custom-keyword-handling}

> Este artigo de referência aborda como a Braze lida com mensagens bidirecionais de SMS, MMS e RCS e respostas automáticas. Inclui explicações sobre como funciona o acionamento por palavras-chave, bem como categorias de palavras-chave personalizadas e suporte multilíngue.

## Mensagens bidirecionais (respostas de palavras-chave personalizadas) {#two-way-messaging-custom-keyword-responses}

As mensagens bidirecionais permitem que você envie mensagens e processe as respostas a essas mensagens. Elas exigem que os usuários finais enviem uma palavra-chave para a Braze, e o usuário receberá uma resposta automática. Aplicadas corretamente, as mensagens bidirecionais podem ser uma solução simples, imediata e dinâmica para marketing de clientes, economizando tempo e recursos ao longo do caminho.

## Gerenciamento de palavras-chave e respostas automáticas {#managing-keywords-and-auto-responses}

SMS, MMS e RCS com a Braze oferecem a opção de criar gatilhos de palavras-chave, respostas personalizadas, definir conjuntos de palavras-chave para vários idiomas e estabelecer categorias de palavras-chave personalizadas.

{% alert note %}
A Braze usa seu conjunto completo de palavras-chave de descadastramento ([palavras-chave padrão]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/optin_optout) e [palavras-chave personalizadas]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/keyword_handling)) para tratamento exato de descadastramento e [descadastramento aproximado]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/fuzzy_opt_out).
{% endalert %}

{% tabs %}
{% tab Adicionar gatilhos de palavras-chave %}

### Adicionar gatilhos de palavras-chave {#add-keyword-triggers}

Além das palavras-chave padrão de opt-in e descadastramento, você também pode definir suas próprias palavras-chave para acionar respostas de Opt-In, Descadastramento e Ajuda.

Para definir suas próprias palavras-chave, faça o seguinte:

1. No dashboard da Braze, acesse **Audience** > **Subscription Group Management** e selecione um grupo de inscrições **SMS/MMS/RCS**.
2. Em **Global Keywords**, selecione o ícone de lápis ao lado da categoria de palavra-chave à qual deseja adicionar uma palavra-chave. ![Palavras-chave de opt-in com o ícone de lápis exibido.]({% image_buster /assets/img/sms/sms_keywords.png %})<br><br>
3. Na guia que se abre, adicione uma palavra-chave que deseja acionar essa categoria de palavra-chave. As palavras-chave não diferenciam maiúsculas de minúsculas, e palavras-chave universais como `START`, `YES` e `UNSTOP` não podem ser alteradas. ![Editando palavras-chave para a categoria "Opt-In". As palavras-chave adicionadas são "START", "UNSTOP" e "YES". O campo de mensagem de resposta diz "Sua inscrição para receber mensagens deste número foi cancelada. Responda HELP para ajuda. Responda STOP para cancelar a inscrição. Taxas de mensagem e dados podem ser aplicadas."]({% image_buster /assets/img/sms/keyword_edit2.png %})

As seguintes regras se aplicam a palavras-chave e respostas de palavras-chave:

| Palavras-chave | Respostas de palavras-chave |
| -------- | ----------------- |
| - Caracteres válidos codificados em UTF-8<br>- Máximo de 20 palavras-chave por categoria no total<br>- Comprimento máximo de 34 caracteres<br>- Comprimento mínimo de 1 caractere <br>- Não podem conter espaços<br>- Devem ser insensíveis a maiúsculas/minúsculas e únicas no grupo de inscrições | - Não podem estar em branco<br>- Comprimento máximo de 300 caracteres<br>- Caracteres válidos em UTF-8 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Adicionar gatilhos de palavras-chave" }

{% alert tip %}
Quer saber como essas palavras-chave podem ser usadas em suas Campaigns e Canvas para redirecionar e acionar mensagens? Acesse [Redirecionamento de usuários]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/user_retargeting) para saber mais.
{% endalert %}
{% endtab %}

{% tab Gerenciar respostas %}

### Gerenciar respostas {#manage-responses}

Você pode gerenciar suas próprias respostas que são enviadas aos usuários depois que eles enviam uma palavra-chave para uma categoria de palavra-chave específica.

1. No dashboard da Braze, acesse **Audience** > **Subscription Group Management** e selecione um grupo de inscrições **SMS/MMS/RCS**. <br><br>
2. Em **Global Keywords**, selecione uma categoria de palavra-chave para editar uma resposta selecionando o ícone de lápis. ![Palavras-chave de opt-in com o ícone de lápis exibido.]({% image_buster /assets/img/sms/sms_keywords.png %})<br><br>
3. Na guia que se abre, edite sua resposta. Tenha em mente nossas [seis regras para garantir a conformidade]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations#the-six-rules-to-get-compliance-right) ao criar sua resposta, e leia as regras a seguir que se aplicam a palavras-chave e respostas de palavras-chave.<br><br>
4. Para encurtar automaticamente URLs estáticas em sua resposta, selecione o botão **Link Shortening**. O contador de caracteres será atualizado para mostrar o comprimento esperado da URL encurtada. ![Um GIF mostrando o contador de caracteres sendo atualizado quando o botão "Link Shortening" está ativado.]({% image_buster /assets/img/sms/link_shortening.gif %}){: style="max-width:60%;"}

#### Considerações {#considerations}

| Palavras-chave | Respostas de palavras-chave |
| -------- | ----------------- |
| - Caracteres válidos codificados em UTF-8<br>- Máximo de 20 palavras-chave por categoria no total<br>- Comprimento máximo de 34 caracteres<br>- Comprimento mínimo de 1 caractere <br>- Não podem conter espaços<br>- Devem ser insensíveis a maiúsculas/minúsculas e únicas no grupo de inscrições | - Não podem estar em branco<br>- Comprimento máximo de 300 caracteres<br>- Caracteres válidos em UTF-8 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Considerações" }

{% endtab %}
{% endtabs %}

{% alert tip %}
Se um Canvas baseado em ação for acionado por uma mensagem SMS, MMS ou RCS recebida, você pode referenciar propriedades de SMS, MMS ou RCS na primeira [etapa de mensagem]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step) do Canvas.
{% endalert %}

## Suporte multilíngue {#multi-language-support}

Ao enviar para determinados países, pode ser necessário que o remetente ofereça suporte a palavras-chave de entrada e respostas de saída em um idioma local. Para isso, a Braze permite que você crie uma configuração de palavras-chave específica por idioma. Quando criada, a configuração de palavras-chave específica por idioma será aplicada a todos os números de envio dentro do grupo de inscrições.
![Menu suspenso exibindo idiomas para adicionar como configuração de palavras-chave.]({% image_buster /assets/img/sms/multi-language.png %}){: style="float:right;max-width:50%;margin-left:10px;"}

### Criando palavras-chave específicas por idioma {#creating-language-specific-keywords}

Selecione **Add a Language** e escolha o idioma desejado ou pesquise um idioma no menu suspenso.

{% alert important %}
Idiomas que não sejam o inglês não vêm com palavras-chave e respostas predefinidas, então os remetentes precisarão trabalhar com suas equipes de marketing e jurídico para adicionar as palavras-chave necessárias a esse conjunto. Caso contrário, a Braze não processará mensagens recebidas localizadas para esses idiomas.
{% endalert %}

Se você precisar excluir um idioma, selecione o botão **Delete Language** no canto inferior direito.

![Página de palavras-chave globais com a guia "Italiano" selecionada. Guias adicionais existem para cada idioma adicionado.]({% image_buster /assets/img/sms/multi-language2.png %})

## Categorias de palavras-chave personalizadas {#custom-keyword-categories}

Além das três categorias de palavras-chave padrão (Opt-in, Descadastramento e Ajuda), você também pode criar até 25 categorias de palavras-chave próprias. Isso permite identificar palavras-chave arbitrárias e configurar respostas específicas para o seu negócio. Um exemplo de categoria pode ser "PROMO" ou "DESCONTO", que pode acionar uma resposta sobre promoções que estão acontecendo neste mês.

Essas palavras-chave personalizadas operam em uma capacidade "sempre ativa", o que significa que qualquer usuário inscrito no seu serviço de mensagens pode enviar palavras-chave e receber uma resposta a qualquer momento. Além desse comportamento, você também tem a opção de definir palavras-chave específicas que só podem ser enviadas em [determinados momentos](#lifecycle-specific-keywords) do ciclo de vida do usuário.

![Palavras-chave para uma categoria "Promo". Se um usuário enviar "YO", ele recebe a mensagem com um código promocional.]({% image_buster /assets/img/sms/sms_custom_keyword.png %})

### Criando uma categoria personalizada {#creating-a-custom-category}

Para criar uma categoria de palavra-chave personalizada, faça o seguinte:

1. Edite o grupo de inscrições apropriado.
2. Selecione **Add custom keyword**. ![Campos para adicionar novas palavras-chave.]({% image_buster /assets/img/sms/sms_custom_step.png %}){: style="max-width:90%;"}
3. Forneça um nome para a categoria de palavra-chave e defina quais palavras-chave um usuário pode enviar para receber a mensagem de resposta.

Depois que essa categoria de palavra-chave for criada, ela estará disponível para [filtrar e acionar]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/user_retargeting) em suas Campaigns e Canvas.

As palavras-chave criadas em categorias de palavras-chave personalizadas seguem todas as regras e validações para a criação de novas palavras-chave.

### Palavras-chave específicas do ciclo de vida {#lifecycle-specific-keywords}

Se você tem um caso de uso em que deseja limitar quando um cliente pode enviar uma palavra-chave específica durante seu ciclo de vida (por exemplo, durante a integração inicial) para receber uma resposta, pode usar o gatilho **Sent inbound SMS to subscription group within keyword category OTHER** em sua Campaign ou Canvas e definir palavras-chave que seus usuários podem enviar em um determinado momento.

Esse gatilho suporta filtragem na mensagem de entrada específica usando comparações de "é" ou "não é" da mensagem, bem como regras de regex de "corresponde" ou "não corresponde" para validar a entrada do usuário.

#### Canvas

![Etapa de Canvas baseada em ação com o gatilho Enviou SMS de entrada para o grupo de inscrições "Serviço de Mensagens" dentro da categoria de palavra-chave "Outra" onde o corpo da mensagem corresponde à expressão regular "símbolo de circunflexo skip."]({% image_buster /assets/img/sms/canvas_trigger.png %}){: style="max-width:90%;"}

#### Campaign

![Campaign baseada em ação com o gatilho Enviou SMS de entrada para o grupo de inscrições "Serviço de Mensagens de Marketing A" dentro da categoria de palavra-chave "Outra" onde o corpo da mensagem é "Keyword1" ou é "Keyword2" ou não é "Keyword A".]({% image_buster /assets/img/sms/campaign_trigger.png %}){: style="max-width:90%;"}

### Lidando com palavras-chave desconhecidas {#dealing-with-unknown-keywords}

Recomendamos fortemente configurar uma resposta automática quando usuários inscritos enviam algo que não corresponde a nenhuma das suas palavras-chave definidas (tratado na categoria de palavra-chave **OTHER**).

Para enviar uma resposta padrão — por exemplo, "Desculpe! Não reconhecemos essa palavra-chave." — faça o seguinte:

1. Crie uma [Campaign de SMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/create).
2. Para **Público-alvo**, escolha **Todos os usuários** (o gatilho ainda limita quem recebe a mensagem).
3. Para **Programar**, escolha **Entrega baseada em ação**.
4. Defina o gatilho como **Send inbound SMS** para o grupo de inscrições apropriado **within keyword category OTHER**.
5. Na etapa **Messaging**, insira o corpo da resposta que deseja que os usuários recebam.

Para saber como a Braze lida com mensagens recebidas de números de telefone **desconhecidos** (antes de um perfil existir), consulte [Lidar com números de telefone desconhecidos]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/unknown_phone_numbers).

{% alert tip %}
Quer saber como essas palavras-chave e categorias de palavras-chave podem ser usadas em suas Campaigns e Canvas para redirecionar e acionar mensagens? Acesse [Redirecionamento de usuários]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/user_retargeting) para saber mais.
{% endalert %}