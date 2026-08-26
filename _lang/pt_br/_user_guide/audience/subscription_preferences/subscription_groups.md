---
nav_title: Grupos de inscrições
article_title: Grupos de inscrições
page_order: 4
description: "Saiba como os grupos de inscrições funcionam nos canais da Braze, como criá-los e gerenciá-los, e o comportamento específico de cada canal para e-mail, WhatsApp, SMS, MMS, RCS e LINE."
---

# Grupos de inscrições {#subscription-groups}

> Saiba como os grupos de inscrições funcionam nos canais da Braze, como criá-los e gerenciá-los no dashboard, e onde as regras específicas de cada canal se aplicam.

Os grupos de inscrições controlam quais usuários podem receber mensagens de um conjunto específico de recursos de envio dentro de um canal.

Para e-mail, os grupos de inscrições são filtros opcionais de categoria sobre o estado de inscrição global. Para SMS, WhatsApp e LINE, os grupos de inscrições são filtros de público obrigatórios para cada envio. Eles permitem oferecer opções granulares de aceitação e cancelamento — como newsletters versus promoções, ou SMS transacional versus marketing — sem alterar o estado de inscrição global do canal de um usuário, quando existe.

Use os [endpoints de grupos de inscrições]({{site.baseurl}}/api/endpoints/subscription_groups) para gerenciar programaticamente os grupos de inscrições armazenados no seu espaço de trabalho da Braze.

{% multi_lang_include alerts/note_alerts.md alert='subscription group limit' %}

## Estado de inscrição global versus grupos de inscrições {#global-subscription-state-versus-subscription-groups}

Alguns canais têm tanto um estado de inscrição global quanto grupos de inscrições:

| Canal | Estado de inscrição global | Grupos de inscrições |
| --- | --- | --- |
| E-mail | Aceitação, inscrito ou cancelou inscrição para todos os e-mails | Categorias opcionais (por exemplo, newsletters ou promoções) dentro do e-mail |
| SMS, MMS e RCS | Sem estado global de SMS; a inscrição é por grupo | Obrigatório para cada envio; cada grupo contém números de telefone de envio ou remetentes RCS |
| WhatsApp | Sem estado global do WhatsApp; a inscrição é por grupo | Criado quando você integra o WhatsApp; cada grupo é mapeado para um número de telefone de envio |
| LINE | Sem estado global do LINE; a inscrição é por grupo | Criado por integração de canal LINE; seguir ou deixar de seguir no app LINE determina o estado |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Estado de inscrição global versus grupos de inscrições" }

Um usuário pode estar inscrito globalmente para e-mail e ao mesmo tempo ter cancelado a inscrição de um grupo de inscrições de e-mail específico. Para SMS, um usuário pode estar inscrito em um grupo transacional e ter cancelado a inscrição de um grupo promocional ao mesmo tempo.

## Criar um grupo de inscrições {#create-a-subscription-group}

A forma de obter um grupo de inscrições depende do canal. Grupos de e-mail são criados no dashboard; grupos de SMS, MMS e RCS são provisionados durante a integração; grupos de WhatsApp e LINE são criados durante a integração do canal. Para detalhes de provisionamento específicos de cada canal, consulte [Comportamento específico do canal](#channel-specific-behavior).

### E-mail {#email}

1. Acesse **Público** > **Gerenciamento de grupos de inscrições**.
2. Selecione **Criar grupo de inscrições de e-mail**.
3. Insira um nome e uma descrição. Cada grupo de inscrições no seu espaço de trabalho deve ter um nome único. Se você inserir um nome que já existe, o dashboard exibirá um erro e não salvará o grupo.
4. Selecione **Salvar**.

![Campos para criar um grupo de inscrições.]({% image_buster /assets/img/sub_group_create.png %}){: style="max-width:75%"}

## Segmentar com grupos de inscrições {#segment-with-subscription-groups}

Ao criar um segmento, adicione um filtro de grupo de inscrições para direcionar usuários que aceitaram receber mensagens daquele grupo. Isso é útil para newsletters mensais, programas de cupons, níveis de associação e outros envios baseados em categorias.

![Exemplo de direcionamento de usuários no segmento "Lapsed Users" com o filtro para usuários no grupo de inscrições "Weekly Emails".]({% image_buster /assets/img/segment_sub_group.png %}){: style="max-width:90%"}

## Arquivar grupos de inscrições {#archive-subscription-groups}

Grupos de inscrições arquivados não podem ser editados e não aparecem mais em filtros de segmento ou centrais de preferências. Se você arquivar um grupo usado como filtro de segmento em uma Campaign, Canvas ou segmento ativo, receberá um erro até remover essas referências.

Para arquivar um grupo em **Gerenciamento de grupos de inscrições**, encontre o grupo e selecione **Arquivar** no menu <i class="fa-solid fa-ellipsis-vertical" aria-label="Mais opções"></i>.

A Braze bloqueia o envio de mensagens para grupos arquivados, então você não pode usar um grupo de inscrições arquivado em envios novos ou ativos.

Alguns canais têm regras adicionais de arquivamento. Consulte [Grupos de inscrições LINE](#line-subscription-groups) para o comportamento de espaço de trabalho e reintegração.

## Verificar os grupos de inscrições de um usuário {#check-a-users-subscription-groups}

- **Perfil de usuário:** Abra um perfil em [Pesquisar usuários]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles#access-profiles). Na guia **Engajamento**, veja os grupos de inscrições e o status para e-mail, SMS, WhatsApp e canais relacionados.
- **REST API:** Use os endpoints [Listar grupos de inscrições do usuário]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups) ou [Listar status do grupo de inscrições do usuário]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status).

### Atualizar o status do grupo de inscrições {#update-subscription-group-status}

Você pode atualizar a associação de um usuário a um grupo de inscrições por meio da REST API, SDK, importação de usuário, perfil de usuário, Central de Preferências de e-mail, etapa de atualização de usuário em um Canvas e outros fluxos específicos do canal. Os métodos exatos dependem do canal — consulte cada [seção do canal](#channel-specific-behavior) e [Grupos de inscrições de SMS, MMS e RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups#set-a-users-state) para orientações de tempo específicas de SMS.

## Centrais de preferências {#preference-centers}

Grupos de inscrições de e-mail podem aparecer em uma [Central de Preferências de e-mail]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center) para que os usuários gerenciem as aceitações de e-mail por categoria em um só lugar. Os grupos de inscrições de e-mail ativos ficam disponíveis para adição quando você cria uma Central de Preferências; centrais de preferências legadas listam automaticamente todos os grupos de e-mail ativos.

Para SMS e WhatsApp, gerencie o estado de inscrição por meio da REST API, fluxos de aceitação, palavras-chave (SMS), perfil de usuário e outros métodos específicos do canal em cada [seção do canal](#channel-specific-behavior).

## Comportamento específico do canal {#channel-specific-behavior}

### Grupos de inscrições de e-mail {#email-subscription-groups}

Os grupos de inscrições de e-mail ficam sobre os [estados de inscrição global de e-mail]({{site.baseurl}}/user_guide/channels/email/subscriptions#subscription-states) (aceitação, inscrito e cancelou inscrição). Usuários no estado global `unsubscribed` não recebem e-mail, independentemente da associação ao grupo de inscrições.

Detalhes específicos de e-mail:

- **Central de Preferências:** Cada grupo de inscrições de e-mail criado fica disponível para adição a uma Central de Preferências.
- **Análise de dados de Campaign:** Na página **Email Message Performance** de uma Campaign, abra **Subscription Groups** para ver as contagens agregadas de inscrições e cancelamentos de inscrição daquele envio.

#### Visualizar tamanhos dos grupos de inscrições {#viewing-subscription-group-sizes}

Em **Gerenciamento de grupos de inscrições**, gráficos de séries temporais reportam:

- **Tamanho do grupo de inscrições:** usuários inscritos naquele grupo em uma data específica
- **Tamanho de cancelamentos do grupo de inscrições:** usuários que cancelaram a inscrição daquele grupo em uma data específica

Essas contagens refletem a associação àquele grupo, não o estado de inscrição global de e-mail. Elas podem diferir de um segmento que usa **Email Subscription Status is Unsubscribed**, que reflete o [estado de inscrição global de e-mail]({{site.baseurl}}/user_guide/channels/email/subscriptions#subscription-states).

O tamanho do grupo de inscrições de hoje não é calculado por padrão. Se o seu intervalo de datas incluir hoje, selecione **Calculate today's statistics** para adicionar o valor de hoje à série temporal. Para espaços de trabalho muito grandes, a Braze pode exibir contagens estimadas em vez de contagens exatas.

Para rodapés, páginas de cancelamento de inscrição e gerenciamento de inscrição global de e-mail, consulte [Inscrições de e-mail]({{site.baseurl}}/user_guide/channels/email/subscriptions).

### Grupos de inscrições do WhatsApp {#whatsapp-subscription-groups}

Os grupos de inscrições do WhatsApp são criados quando você [integra o WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup) com seu espaço de trabalho por meio do Technology Partner Portal.

| Estado | Definição |
| --- | --- |
| Inscrito | O usuário confirmou explicitamente que deseja receber mensagens do WhatsApp da sua empresa. Os usuários podem ser inscritos por meio da API de inscrição da Braze ou do seu fluxo de aceitação. |
| Cancelou inscrição | O usuário não aceitou ou foi removido do grupo. Usuários que cancelaram a inscrição não recebem mensagens do WhatsApp dos números de telefone daquele grupo. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Estados de inscrição do WhatsApp" }

O WhatsApp exige uma aceitação explícita. Palavras-chave de aceitação não são suportadas neste canal — você mantém o consentimento e o estado de inscrição. Para fluxos de aceitação e cancelamento, consulte [Aceitações e cancelamentos do WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/opt_ins_and_opt_outs).

Para etapas de arquivamento, atualizações de Canvas e exemplos de REST API, consulte [Grupos de inscrições do WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups).

### Grupos de inscrições de SMS, MMS e RCS {#sms-mms-and-rcs-subscription-groups}

Os grupos de inscrições de SMS, MMS e RCS são a base para o envio nesses canais. Cada grupo é uma coleção de [entidades de envio]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sender_setup) — como códigos curtos, códigos longos, IDs de remetente alfanuméricos ou remetentes verificados por RCS — para uma finalidade de envio de mensagens específica (por exemplo, transacional versus promocional).

| Estado | Definição |
| --- | --- |
| Inscrito | O usuário está inscrito para receber mensagens daquele grupo de inscrições, por meio da API de inscrição, palavras-chave de aceitação ou outros fluxos suportados. Com a [aceitação dupla]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/double_opt_in) ativada, os usuários devem confirmar antes que o status seja atualizado para inscrito. |
| Cancelou inscrição | O usuário cancelou por meio de uma palavra-chave ou atualização de API. Usuários que cancelaram a inscrição não recebem SMS, MMS ou RCS dos remetentes daquele grupo. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Estados de inscrição de SMS e RCS" }

Ao lançar uma mensagem SMS ou RCS, você seleciona um grupo de inscrições no criador. A Braze adiciona um filtro de público para que apenas usuários inscritos sejam direcionados. A Braze não envia SMS ou RCS para usuários que não estejam inscritos no grupo selecionado. Para receber uma mensagem de teste de SMS, o destinatário deve pertencer ao grupo de inscrições que você selecionar para o teste. Para mais detalhes, consulte [Perguntas frequentes sobre SMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/faqs#does-a-user-need-to-be-part-of-an-sms-subscription-group-to-receive-sms-test-messages).

Os grupos de inscrições para SMS são provisionados durante a integração. Para tags de MMS, configuração de remetente RCS, permissões geográficas, migração RCS e tratamento avançado de cancelamento, consulte [Grupos de inscrições de SMS, MMS e RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups).

### Grupos de inscrições LINE {#line-subscription-groups}

Cada grupo de inscrições LINE está conectado a uma integração de canal LINE.

| Estado | Definição |
| --- | --- |
| Inscrito | O usuário seguiu o canal LINE no app LINE. Após a integração, a Braze inscreve os usuários quando eles seguem o canal. |
| Cancelou inscrição | O usuário não seguiu o canal ou deixou de segui-lo. Usuários que cancelaram a inscrição não recebem mensagens LINE daquele grupo. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Estados de inscrição LINE" }

O LINE é a fonte de verdade para o status de inscrição. A Braze processa os eventos de seguir e deixar de seguir para atualizar os perfis.

Os grupos de inscrições LINE não podem ser movidos entre espaços de trabalho. Se você arquivar um grupo e reintegrar o canal em outro espaço de trabalho, a Braze cria um novo grupo de inscrições no espaço de trabalho de destino.

Para comportamento de arquivamento, reconciliação de usuários e etapas de integração, consulte [Grupos de inscrições LINE]({{site.baseurl}}/user_guide/channels/line/message_users/subscription_groups) e [Configuração do LINE]({{site.baseurl}}/user_guide/channels/line/line_setup).