---
nav_title: Setembro
page_order: 5
noindex: true
page_type: update
description: "Este artigo contém notas de versão de setembro de 2018."
---
# Setembro de 2018 {#september-2018}

## Grupos de notificação do iOS 12: Recursos adicionais {#ios-12-notification-groups-additional-abilities}

Agora você pode acessar [os recursos de Grupo de Notificação da Apple]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#notification-groups) usando a Braze! É possível adicionar argumentos e grupos resumidos, utilizar alertas críticos, filtrar usuários autenticados provisoriamente e visualizar o status de autenticação provisória nos perfis de usuário.

## Horário de silêncio {#quiet-time}

Os clientes agora podem especificar o [horário de silêncio]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-5-select-your-send-settings) (o período durante o qual suas mensagens não serão enviadas) para o Canvas. Basta acessar as **Configurações de envio do Canvas** e marcar a opção "Ativar horário de silêncio". Em seguida, selecione o horário de silêncio no horário local do usuário e a ação a ser seguida se a mensagem for disparada dentro desse horário de silêncio.

As Campaigns agora também usam o horário de silêncio em vez de "enviar esta mensagem durante uma parte específica do dia".

## Clientes do Adjust {#adjust-customers}

Os clientes da Braze que usam o [Adjust]({{site.baseurl}}/partners/message_orchestration/attribution/adjust/) agora podem ver sua chave de API da Braze e a URL da instância da Braze, que serão usadas na plataforma Adjust para integração.

## Filtro "não está no Segment" {#not-in-segment-filter}

Os clientes agora podem criar um Segment a partir de usuários que [não estão incluídos em um determinado Segment]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#retargeting).

## Exportações CSV de destinatários do Canvas {#canvas-recipient-csv-exports}

Os clientes agora podem [exportar dados]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_canvas_data/) dos usuários que entraram em um Canvas. O CSV gerado será semelhante ao CSV de Campaign.

## Filtro de Segment do iOS 12 autorizado provisoriamente {#provisionally-authorized-ios-12-segment-filter}

Foi adicionado um [filtro de Segment]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#other) que permite encontrar usuários que estão autorizados provisoriamente no iOS 12 para um determinado app.

## Upload de imagens para mensagens no app {#in-app-message-image-uploader}

O uploader de imagens para mensagens no app foi transferido do painel de design para o painel de composição.

## Permissões somente leitura na página Perfil do usuário {#read-only-permissions-on-user-profile-page}

Antes desta versão, os clientes podiam alterar o status da inscrição e o endereço de e-mail no perfil do usuário com [permissões somente de leitura]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#available-limited-and-team-role-permissions). Renomeamos a permissão `import_user` para `import_and_update_user` e restringimos o acesso de edição ao status da inscrição e ao endereço de e-mail. Agora, quando um desenvolvedor está em modo somente leitura ou não tem essa permissão, ele não pode alterar o status da inscrição ou o endereço de e-mail.