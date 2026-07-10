---
nav_title: Mixpanel
article_title: Mixpanel
alias: /partners/mixpanel/
description: "Este artigo de referência descreve a parceria entre a Braze e o Mixpanel, uma plataforma de análise de dados, permitindo a importação de coortes do Mixpanel para a Braze para criar segmentos da Braze que podem ser usados para direcionamento de usuários em futuras Campaigns ou Canvas da Braze."
page_type: partner
search_tag: Partner
tool: Currents

---

# [![Curso do Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/mixpanel-integration-with-braze/339085/scorm/2u7y2e6qrldh2){: style="float:right;width:120px;border:0;" class="noimgborder"}Mixpanel {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecommixpanel-integration-with-braze339085scorm2u7y2e6qrldh2-stylefloatrightwidth120pxborder0-classnoimgbordermixpanel}

> O [Mixpanel](https://mixpanel.com/) é uma plataforma de análise de dados que permite exportar eventos do Mixpanel para outras plataformas para realizar análises mais profundas. Os dados coletados podem então ser usados para criar relatórios personalizados e medir o engajamento e a retenção de usuários.

A integração entre a Braze e o Mixpanel permite a [importação de coortes do Mixpanel para a Braze]({{site.baseurl}}/partners/data_and_analytics/analytics/mixpanel/mixpanel_cohort_import) para criar segmentos da Braze que podem direcionar usuários em futuras Campaigns ou Canvas da Braze. A sincronização de coortes atualiza a associação de coortes na Braze e não importa eventos ou propriedades de usuários do Mixpanel. Para mais detalhes, consulte [Importação de coorte do Mixpanel]({{site.baseurl}}/partners/data_and_analytics/analytics/mixpanel/mixpanel_cohort_import#data-import-integration).

Você também pode usar o Braze Currents para [exportar seus eventos da Braze para o Mixpanel](#data-export-integration) e gerar análises mais detalhadas sobre conversões, retenção e uso do produto.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
|---|---|
| Conta Mixpanel | É necessário ter uma [conta Mixpanel](https://mixpanel.com/) para aproveitar essa parceria. |
| Currents | Para exportar dados de volta para o Mixpanel, você precisa ter o [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents#access-currents) configurado na sua conta. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integração de exportação de dados {#data-export-integration}

Uma lista completa dos eventos que podem ser exportados da Braze para o Mixpanel pode ser encontrada nesta seção. Todos os eventos enviados ao Mixpanel incluem o `external_user_id` do usuário como Mixpanel Distinct ID. No momento, a Braze não envia dados de eventos de usuários que não possuem `external_user_id` definido.

Você pode exportar dois tipos de eventos para o Mixpanel: [Eventos de engajamento com mensagem](#supported-currents-events), que consistem nos eventos da Braze diretamente relacionados ao envio de mensagens, e [Eventos de comportamento do cliente](#supported-currents-events), incluindo outras atividades do app ou do site, como sessões, eventos personalizados e compras rastreadas pela plataforma. Todos os eventos personalizados são prefixados com `[Braze Custom Event]`. As propriedades de eventos personalizados e as propriedades de eventos de compra são prefixadas com `[Custom event property]` e `[Purchase property]`, respectivamente.

Entre em contato com o gerente da sua conta ou abra um [ticket de suporte]({{site.baseurl}}/braze_support) se precisar de acesso a direitos de eventos adicionais.

### Etapa 1: Obter credenciais do Mixpanel {#step-1-get-mixpanel-credentials}

No dashboard do Mixpanel, clique em **Project Settings** em um projeto novo ou existente. Lá você encontrará o segredo da API do Mixpanel e o token do Mixpanel. Essas credenciais serão usadas na próxima etapa para criar sua conexão com o Currents.

### Etapa 2: Criar o Braze Current {#step-2-create-braze-current}

1. Na Braze, acesse **Currents** > **+ Create Current** > **Create Mixpanel Export**.
2. Forneça um nome de integração, e-mail de contato, segredo da API do Mixpanel e token do Mixpanel nos campos listados.
3. Selecione os eventos que deseja rastrear; uma lista dos eventos disponíveis é fornecida.
4. Selecione **Launch Current**.

![A página Braze Mixpanel Currents. Essa página inclui campos para nome da integração, e-mail de contato, segredo da API e token de exportação do Mixpanel. A metade inferior da página Currents lista os eventos Currents disponíveis que você pode enviar.]({% image_buster /assets/img_archive/mixpanel4.png %}){: style="max-width:80%;"}

{% tab note %}
Consulte a [documentação de integração](https://help.mixpanel.com/hc/en-us/articles/360001243663) do Mixpanel para saber mais.
{% endtab %}

## Eventos Currents compatíveis {#supported-currents-events}

A Braze oferece suporte à exportação dos seguintes eventos para o Mixpanel:

- [Eventos de engajamento com mensagem]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events)
- [Eventos de comportamento do cliente]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events)

Para a estrutura da carga útil de cada evento, selecione a guia **Mixpanel** no [glossário de eventos de engajamento com mensagem]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) e no [glossário de eventos de comportamento do cliente]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events).

## Solução de problemas {#troubleshooting}

### Verificar a chave de API do Mixpanel e o ID externo da Braze {#verify-mixpanel-api-key-and-braze-external-id}

Confirme que sua chave de API do Mixpanel e os valores de `braze_external_id` correspondem ao esperado tanto na Braze quanto no Mixpanel. A API de sincronização de coortes compartilha grupos de usuários entre os produtos, e a sincronização não funcionará corretamente se o `external_id` na Braze e o identificador enviado pelo Mixpanel não estiverem alinhados. As sincronizações de coortes do Mixpanel seguem o cronograma do Mixpanel — por exemplo, uma vez ou aproximadamente a cada duas horas — então aguarde um tempo entre as verificações.

### Verificar o status da implementação {#check-implementation-status}

Confirme que o `braze_external_id` está implementado no Mixpanel.

### Definir a propriedade do usuário diretamente {#set-the-user-property-directly}

Para reduzir ambiguidades, defina o `braze_external_id` diretamente no Mixpanel.

### Definição automática de propriedade (SDKs) {#automatic-property-setting-sdks}

O SDK do Mixpanel pode definir o `braze_external_id` automaticamente quando o SDK da Braze está integrado no mesmo aplicativo. Se você implementar o Mixpanel e a Braze juntos, normalmente não será necessária nenhuma configuração adicional além da instalação de ambos os SDKs.

{% alert note %}
O `braze_external_id` não é definido quando `changeUser()` é chamado na Braze; ele é definido quando o Mixpanel inicializa ou inicia uma sessão (durante o "init" ou "start session").
{% endalert %}