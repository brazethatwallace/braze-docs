---
nav_title: Campanhas disparadas por API e baseadas em ação
article_title: Testar campanhas disparadas por API e baseadas em ação
page_order: 2
page_type: reference
description: "Este artigo de referência explica como testar campanhas disparadas por API e baseadas em ação."

---

# Campanhas disparadas por API e baseadas em ação {#api-triggered-and-action-based-campaigns}

> Ao configurar campanhas, é sempre uma boa prática testar suas mensagens antes do lançamento. Este artigo de referência aborda a criação de um segmento de usuários teste que permitirá inspecionar solicitações de API, cargas úteis e visualizar registros de entregabilidade.

## Etapa 1: Criar um segmento de usuários teste {#step-1-create-a-test-user-segment}

A única forma de testar o disparo de uma campanha com a API ou evento personalizado é colocar a campanha no ar. Como parte do lançamento de uma nova campanha, recomendamos fortemente adicionar um segmento de usuários teste às campanhas ao testar a entregabilidade dos disparos. Isso funcionará como uma rede de segurança, garantindo que, mesmo que uma campanha seja enviada acidentalmente, ela será direcionada apenas para usuários internos.

1. **Importar usuários teste**<br>Usuários teste podem ser importados para a Braze por meio de um CSV ou de uma solicitação em lote única pelo [Postman]({{site.baseurl}}/api/postman_collection). Ao importar esses usuários, recomendamos definir um atributo personalizado em seus perfis (como `internal_test_user: true`) que possa ser usado para criar um segmento de grupo de teste. <br><br>
2. **Adicionar usuários teste como usuários teste reconhecidos pela Braze**<br>[Marcar seus usuários teste como usuários teste reconhecidos pela Braze]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups) no dashboard dá acesso a registros detalhados para cada usuário, permitindo inspecionar solicitações de API, suas cargas úteis e visualizar registros de entregabilidade. Esses registros podem ajudar a determinar se houve algum problema na entrega de campanhas aos usuários finais. <br><br>
3. **Criar segmento**<br>Para criar um segmento de usuários teste, crie um segmento de usuários com o atributo personalizado `internal_test_user` definido como `true`. Esse segmento pode ser removido quando a campanha entrar no ar.

## Etapa 2: Testar envios {#step-2-testing-sends}

Em seguida, você pode fazer um envio de teste a partir do dashboard da Braze ou usar o Inbox Vision (apenas para e-mail) para ver como a disposição ficará enquanto a campanha ainda estiver em modo de rascunho. Depois, envie a campanha para o seu segmento de usuários teste para verificar se está funcionando conforme esperado. Independentemente de a campanha ser disparada por API ou baseada em ação, use o Postman para enviar uma solicitação única à API da Braze, disparando a campanha.

## Etapa 3: Usar os registros da Braze para inspecionar os resultados recebidos {#step-3-use-braze-logging-to-inspect-inbound-results}

Use os registros da Braze para solucionar problemas de disparo, envio e eventos.
- O [registro de usuários de eventos]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/event_user_log) mostrará a carga útil bruta da solicitação de disparo por API, o evento personalizado que disparou a campanha e quaisquer propriedades de gatilho ou evento associadas.
- O [registro de atividades de envio de mensagem]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log) registrará quaisquer erros e ajudará a entender por que uma determinada mensagem pode não ter sido entregue.

## Etapa 4: Remover o segmento de teste e lançar a campanha {#step-4-remove-the-test-segment-and-roll-out-the-campaign}

Quando a mensagem estiver disparando e renderizando corretamente, com todos os links clicados sendo registrados, você pode remover o segmento e atualizar a campanha. Se preferir iniciar a campanha do zero para que as poucas impressões dos usuários teste não sejam incluídas, você pode duplicar a campanha e reiniciá-la sem o segmento de usuários teste.