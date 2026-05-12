{% if include.alert == "Shopify deprecation" %}

{% alert important %}
Uma [nova versão da integração do Shopify]({{site.baseurl}}/partners/shopify/#new-shopify-integration) será lançada em fases a partir de abril de 2025. As fases serão baseadas no tipo de loja Shopify e no ID externo usado para configurar a integração inicial. <br><br>**A versão antiga da integração não estará mais disponível após 28 de agosto de 2025. Atualize para a nova versão antes dessa data para continuar usando a integração sem problemas.**
{% endalert %}

{% endif %}

{% if include.alert == 'Web push private browsing' %}

{% alert important %}
Janelas de navegação privada não oferecem suporte a push para a web.
{% endalert %}

{% endif %}

{% if include.alert == 'BCC address billable emails' %}

{% alert important %}
Adicionar um endereço BCC à sua Campaign ou Canvas resulta na duplicação dos seus e-mails faturáveis para a Campaign ou componente do Canvas, já que a Braze envia uma mensagem para o seu usuário e uma para o seu endereço BCC.
{% endalert %}

{% endif %}

{% if include.alert == 'Android notification priority' %}

{% alert important %}
A configuração de Prioridade de Exibição de Notificações não é mais usada em dispositivos com Android O ou posterior. Nesses dispositivos, defina a prioridade por meio da [configuração do canal de notificações](https://developer.android.com/training/notify-user/channels#importance).
{% endalert %}

{% endif %}

{% if include.alert == "Email via SMS" %}

{% alert important %}
Não envie e-mails de transação legalmente exigidos para gateways de SMS, pois há uma grande probabilidade de que esses e-mails não sejam entregues.
<br><br>
Embora os e-mails que você envia usando um número de telefone e o domínio de gateway do provedor (conhecido como MM3) possam resultar no recebimento do e-mail como uma mensagem SMS (texto), alguns dos nossos provedores de e-mail não oferecem suporte a esse comportamento. Por exemplo, se você enviar um e-mail para um número de telefone da T-Mobile (como "9999999999@tmomail.net"), sua mensagem SMS será enviada para o proprietário desse número de telefone na rede T-Mobile.
<br><br>
Lembre-se de que, embora esses e-mails possam não ser entregues ao gateway de SMS, eles ainda contarão para a sua fatura de e-mail. Para evitar o envio de e-mails para gateways sem suporte, consulte a [lista de nomes de domínio de gateway sem suporte](https://www.fcc.gov/consumer-governmental-affairs/about-bureau/consumer-policy-division/can-spam/domain-name-downloads).
{% endalert %}

{% endif %}

{% if include.alert == 'SDK auth' %}

{% alert important %}
Para maior segurança, recomendamos adicionar nosso recurso de [Autenticação do SDK]({{site.baseurl}}/developer_guide/authentication/) para evitar a simulação de usuários.
{% endalert %}

{% endif %}

{% if include.alert == 'Preference Center warning' %}

{% alert important %}
Existem certos navegadores, como os apps Naver para Android e iOS, que não oferecem suporte à Central de Preferências da Braze. Caso preveja que alguns dos seus usuários usem esses navegadores, considere fornecer métodos alternativos para que eles gerenciem suas preferências de e-mail.
{% endalert %}

{% endif %}

{% if include.alert == 'Purchase event deprecation' %}

{% alert important %}
O evento de compra legado está entrando em modo de manutenção. Clientes existentes da Braze podem continuar usando eventos de compra legados. Eles continuarão funcionando como esperado, mas novas funcionalidades serão desenvolvidas com base nos eventos recomendados de eCommerce daqui em diante. A Braze fornecerá aviso prévio bem antes de qualquer data de fim de vida ser definida. Novos clientes da Braze devem usar os [eventos recomendados de eCommerce]({{site.baseurl}}/user_guide/data/activation/custom_data/recommended_events/ecommerce_events/), pois os eventos de compra legados não estarão disponíveis.
{% endalert %}

{% endif %}

{% if include.alert == 'Purchase event deprecation for eCommerce filters' %}

{% alert important %}
O evento de compra legado entrará em estado de descontinuação (modo de manutenção). Os eventos de compra continuarão funcionando como esperado, mas nenhuma nova funcionalidade será desenvolvida sobre eles, em favor dos [eventos recomendados de eCommerce]({{site.baseurl}}/user_guide/data/activation/custom_data/recommended_events/ecommerce_events/). Quando isso acontecer, os filtros de segmento não serão mais preenchidos sob o comportamento de compra.<br><br> Se você está usando eventos de compra atualmente, receberá um aviso prévio sobre os planos de descontinuação. Por enquanto, você pode continuar usando eventos de compra até a data oficial de descontinuação. Para saber mais, consulte a [visão geral de eventos recomendados]({{site.baseurl}}/user_guide/data/activation/custom_data/recommended_events/).
{% endalert %}

{% endif %}

{% if include.alert == 'S3 file bucket export' %}

{% alert important %}
Os arquivos exportados armazenados em buckets S3 são automaticamente excluídos após o link de download expirar (quatro horas a partir do envio do e-mail de exportação, a menos que indicado de outra forma).
{% endalert %}

{% endif %}

{% if include.alert == 'Shopify customer create' %}

{% alert important %}
A integração do Shopify oferece suporte a webhooks de criação e atualização de clientes do Shopify, que estão localizados nas suas configurações de dados. Quando um perfil de usuário é criado ou atualizado no Shopify, um perfil de usuário correspondente na Braze será criado ou atualizado. <br><br>Essas ações não disparam eventos personalizados na Braze e são usadas exclusivamente para [sincronizar dados de usuários do Shopify com a Braze]({{site.baseurl}}/partners/ecommerce/shopify/shopify_overview/#how-the-integration-works). Os dados sincronizados incluem [atributos personalizados]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features/#supported-shopify-custom-attributes), [atributos padrão]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features/#supported-shopify-standard-attributes) e, se ativado na sua configuração, [estados de grupo de inscrições]({{site.baseurl}}/partners/ecommerce/shopify/shopify_overview/#syncing-shopify-email-and-sms-marketing-opt-ins).
{% endalert %}

{% endif %}

{% if include.alert == 'context variable' %}

{% alert important %}
As propriedades de entrada do Canvas fazem parte das variáveis de contexto do Canvas. Isso significa que `canvas_entry_properties` é referenciado como `context`. Cada variável `context` inclui um nome, tipo de dado e um valor que pode incluir Liquid. Atualmente, `canvas_entry_properties` são compatíveis com versões anteriores. Para mais detalhes, consulte [Contexto]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context/#how-it-works) e [objeto de contexto do Canvas]({{site.baseurl}}/api/objects_filters/context_object/).
{% endalert %}

{% endif %}

{% if include.alert == 'Braze Agents' %}

{% alert important %}
Este parceiro aparece na sua página **Parceiros de tecnologia** apenas se você tiver os [Braze Agents]({{site.baseurl}}/user_guide/brazeai/agents/) ativados. Para ajuda para começar, entre em contato com seu gerente de sucesso do cliente.
{% endalert %}

{% endif %}

{% if include.alert == 'time filter types' %}

{% alert important %}
**Escolhendo entre os tipos de filtro "Day of year" e "Time"**: Ao filtrar variáveis de contexto que contêm datas, escolha o tipo de comparação correto com base em se a data se repete a cada ano:

- **Use "Day of year"** quando a data se repete a cada ano (por exemplo, aniversários, datas comemorativas ou feriados como o Natal). Esse tipo de comparação calcula com base no dia do ano (1-365/366), ignorando o componente do ano.
- **Use "Time"** quando a data for uma data absoluta que não se repete (por exemplo, datas de término de contrato, datas de compromissos ou datas de renovação de inscrição). Esse tipo de comparação calcula com base no timestamp completo, incluindo o ano.

Usar "Day of year" para datas absolutas pode produzir resultados incorretos ou inesperados porque o cálculo ignora o componente do ano. Por exemplo, se você estiver comparando uma data futura de término de contrato em abril para determinar se está dentro de 63 dias, usar "Day of year" pode corresponder incorretamente às datas porque compara apenas os números dos dias (119 vs 359) sem considerar que abril está na verdade a 188 dias de distância.

**Diretriz geral**: A data se repete a cada ano? **Sim** → Use "Day of year". **Não** → Use "Time".
{% endalert %}

{% endif %}

{% if include.alert == 'granular permissions ea' %}

{% alert important %}
As permissões granulares estão em acesso antecipado. Quando a migração for planejada para a sua empresa, os administradores da Braze receberão e-mails e banners no dashboard notificando-os sobre a [migração de permissões granulares]({{site.baseurl}}/granular_permissions_migration/).
{% endalert %}

{% endif %}

{% if include.alert == 'WhatsApp audio and documents' %}

{% alert note %}
A [Biblioteca de mídia da Braze]({{site.baseurl}}/media_library/) oferece suporte apenas a imagens e vídeos. Arquivos de áudio e documentos devem ser referenciados por meio de uma URL hospedada.
{% endalert %}

{% endif %}

{% if include.alert == 'Meta MP4 video issue' %}

{% alert important %}
A Meta tem um problema conhecido que pode impedir a reprodução de alguns vídeos MP4 em dispositivos Android devido a configurações específicas de codificação ou contêiner. Até que uma correção permanente esteja disponível, reformatar o arquivo MP4 resolve o problema para a maioria dos remetentes. Teste todos os vídeos em dispositivos Android para confirmar a entregabilidade correta. <br><br>Você pode reformatar o arquivo MP4 usando uma ferramenta online, como o [CloudConvert](https://cloudconvert.com/mp4-converter). Faça upload do seu arquivo MP4 na ferramenta, converta-o para MP4 novamente e depois baixe o arquivo convertido.
{% endalert %}

{% endif %}

{% if include.alert == 'Shopify cart token alias' %}

{% alert important %}
Para esta integração, o alias de usuário deve usar o seguinte formato para que a Braze possa associar os webhooks ao perfil de usuário correto:<br><br>
- `alias_label`: `shopify_cart_${cartToken}`
- `alias_name`: `shopify_cart_token`
{% endalert %}

{% endif %}

{% if include.alert == 'network dependency' %}

{% alert important %}
Content Cards, mensagens no app, Banners e Feature Flags dependem da conectividade do dispositivo para sincronizar com os servidores da Braze. Como as condições de rede podem variar, existe a possibilidade de que o conteúdo ou as atualizações não sejam sincronizados, exibidos ou removidos imediatamente (por exemplo, se o usuário estiver offline). Recomendamos evitar esses canais para atualizações críticas e urgentes.
{% endalert %}

{% endif %}

{% if include.alert == 'dynamic image URL' %}

{% alert important %}
Se você está carregando imagens com [Conteúdo conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/) ou [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/), certifique-se de que a URL da imagem comece com `https://`. Usar `http://` pode causar falha no seu app.
{% endalert %}

{% endif %}