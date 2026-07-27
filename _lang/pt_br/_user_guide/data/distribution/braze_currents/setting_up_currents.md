---
nav_title: Configurar Currents
article_title: Configurar Currents
page_order: 1
page_type: tutorial
description: "Este artigo de instruções explica o processo de integração e configuração do Braze Currents."
tool: Currents
search_rank: 8
---

# [![Curso do Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/currents-the-basics-2/){: style="float:right;width:120px;border:0;" class="noimgborder"}Configurar Currents {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomcurrents-the-basics-2-stylefloatrightwidth120pxborder0-classnoimgborderset-up-currents}

> Esta página descreve o processo genérico de integração e configuração do Braze Currents.

{% alert important %}
O Currents está incluído em determinados pacotes da Braze. Entre em contato com seu representante da Braze se tiver alguma dúvida ou quiser obter acesso.
{% endalert %}

## Solução de problemas {#troubleshooting}

### Não é possível adicionar uma nova integração de Currents {#cannot-add-a-new-currents-integration}

Se você vir a mensagem "Você não tem mais integrações de Currents disponíveis" ao adicionar uma nova integração, ou se o botão para adicionar um novo conector de Currents estiver desativado, as causas mais comuns são:

- Nenhuma permissão de Currents foi adquirida para este espaço de trabalho.
- A permissão de Currents está disponível em um espaço de trabalho diferente na sua empresa.

Para resolver isso, verifique outros espaços de trabalho na sua empresa. Um espaço de trabalho diferente pode mostrar uma permissão de Currents disponível. Se você precisar solicitar uma permissão ou ajustar sua configuração, entre em contato com seu gerente de conta da Braze.

## Requisitos {#requirements}

O uso do Currents com qualquer um de nossos parceiros requer os mesmos parâmetros básicos e a mesma metodologia de conexão.

Cada parceiro exige que a Braze tenha permissão para gravar e enviar arquivos de dados para eles, e a Braze solicita o local em que esses arquivos devem ser gravados, especificamente nomes de buckets ou chaves.

Os requisitos a seguir são os requisitos básicos e mínimos para a integração com a maioria de nossos parceiros. Alguns parceiros exigirão parâmetros adicionais, que estão listados em suas respectivas [documentações de parceiros]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/available_partners), juntamente com quaisquer nuances associadas a esses requisitos básicos.

| Requisito | Origin | Acesso | Descrição
|---|---|---|---|
| Conta com parceiro | Crie uma conta com esse parceiro ou entre em contato com seu gerente de conta da Braze para sugestões. | Verifique o site desse parceiro ou entre em contato para se inscrever. | A Braze não enviará dados a um parceiro se você não tiver acesso a esses dados por meio da conta da sua empresa.
| Chave de API ou token do parceiro | Normalmente, o dashboard do parceiro. | Copie e cole no campo designado da Braze. | A Braze tem um campo designado para isso na página de integrações para esse parceiro. Precisamos disso para mapear para onde enviamos seus dados. **Mantenha suas chaves ou tokens de parceiro atualizados; credenciais inválidas podem desativar seu conector e descartar eventos.**
| Código/chave de autenticação, chave secreta, arquivo de certificado | Entre em contato com um representante da sua conta com esse parceiro. Também pode existir no dashboard do parceiro. | Copie e cole as chaves no campo designado da Braze. Gere e faça upload de arquivos `.json` ou outros arquivos de certificado no local apropriado na Braze. | A Braze tem um campo designado para isso na página de integrações para esse parceiro. Isso fornece credenciais à Braze e nos autoriza a gravar arquivos na sua conta de parceiro. **É importante manter suas informações de autenticação atualizadas; credenciais inválidas podem resultar na desativação do conector e no descarte de eventos.**
| Bucket, caminho da pasta | Alguns parceiros organizam e classificam os dados por buckets. Isso pode ser encontrado no dashboard do parceiro. | Se isso for necessário, copie o nome do bucket ou o caminho do arquivo exatamente no espaço designado na Braze. | Embora isso seja necessário para alguns parceiros, é importante acertar quando você precisar. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Requisitos" }

{% alert important %}
É importante manter suas chaves/tokens de parceiro e informações de autenticação atualizados. Se as credenciais do conector expirarem, o conector deixará de enviar eventos. Se isso persistir por mais de **5 dias**, os eventos do conector serão descartados e os dados serão perdidos permanentemente.
{% endalert %}

## Configuração do Currents {#setting-up-currents}

### Etapa 1: Escolha seu parceiro {#step-1-choose-your-partner}

O Braze Currents permite a integração por meio do armazenamento de dados usando arquivos simples ou com nossos parceiros de análise comportamental e dados de cliente usando cargas úteis JSON em lote para um endpoint designado.

Antes de iniciar sua integração, é melhor decidir qual integração é a mais adequada para seus objetivos. Por exemplo, se você já utiliza o mParticle e o Segment e gostaria que os dados da Braze fossem enviados para lá, seria melhor usar uma carga útil JSON em lote. Se preferir manipular os dados por conta própria ou tiver um sistema mais complexo de análise de dados, talvez seja melhor usar o armazenamento de dados ([a Braze usa esse método]({{site.baseurl}}/user_guide/data/distribution/braze_currents/use_cases/how_braze_uses_currents)!)

### Etapa 2: Abra o Currents {#step-2-open-currents}

Para começar, acesse **Integrações de parceiros** > **Currents**. Você será levado à página de gerenciamento de integração do Currents.

![Página do Currents no dashboard da Braze]({% image_buster /assets/img_archive/currents-main-page.png %})

### Etapa 3: Adicione seu parceiro {#step-3-add-your-partner}

Adicione um parceiro, às vezes chamado de "conector de Currents", selecionando o menu suspenso na parte superior da tela.

Cada parceiro requer um conjunto diferente de etapas de configuração. Para ativar cada integração, consulte nossa lista de [parceiros disponíveis]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/available_partners) e siga as instruções em suas respectivas páginas.

### Etapa 4: Configure seus eventos {#step-4-configure-your-events}

Escolha os eventos que você deseja enviar para esse parceiro marcando as opções disponíveis. Você pode encontrar listas desses eventos em nossas bibliotecas de [Eventos de comportamento do cliente]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events) e [Eventos de engajamento com mensagem]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events).

![Página de configuração do Currents com eventos de parceiro selecionados para exportação.]({% image_buster /assets/img/current4.png %})

Se necessário, você pode saber mais sobre nossos eventos no artigo sobre [semântica de entrega de eventos]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/event_delivery_semantics).

### Etapa 5: Configure transformações de campo {#step-5-set-up-field-transformations}

Você pode usar as transformações de campo do Currents para remover ou aplicar hash em um campo de string.

- **Remover:** Substitui o campo de string por `[REDACTED]`. Isso é útil se o seu parceiro rejeitar eventos com campos ausentes ou vazios.
- **Hash:** Aplica um algoritmo de hash SHA-256 ao campo de string.

Selecionar um campo para uma dessas transformações aplicará essa transformação a todos os eventos em que esse campo aparecer. Por exemplo, ao selecionar `email_address` para hash, o campo `email_address` será submetido a hash nos eventos de envio de e-mail, abertura de e-mail, bounce de e-mail e alteração de estado do grupo de inscrições.

![Adicionando transformações de campo]({% image_buster /assets/img/current3.png %})

### Etapa 6: Teste sua integração {#step-6-test-your-integration}

{% alert important %}
O Currents descartará eventos com cargas úteis excessivamente grandes, superiores a 900&nbsp;KB.
{% endalert %}

Antes de testar, considere conferir nossos [dados de exemplo do Currents no GitHub](https://github.com/Appboy/currents-examples). Quando estiver pronto para testar, escolha uma opção na seção a seguir:

#### Enviando eventos de teste {#sending-test-events}

Para testar sua integração, você pode selecionar **Enviar eventos de teste** para enviar um evento de cada um dos seus tipos de evento selecionados para este Current. Para informações detalhadas sobre cada tipo de evento, consulte nossas bibliotecas de [Eventos de comportamento do cliente]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events) e [Eventos de engajamento com mensagem]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events).

![A página "Teste de Currents" no dashboard da Braze.]({% image_buster /assets/img/currents/current_test_events.png %}){: style="max-width:70%;"}

#### Teste de conectores de Currents {#testing-currents-connectors}

Os conectores de teste de Currents são versões gratuitas de nossos conectores existentes que podem ser usados para testar e experimentar diferentes destinos. Os Currents de teste têm:

- Até 10 conectores de teste de Currents por espaço de trabalho.
- Um máximo agregado de 1.500 eventos por período fixo de 24 horas, reiniciando à meia-noite UTC. Esse total de eventos é atualizado de hora em hora no dashboard.

Após seus conectores de teste de Currents atingirem o limite de envio, seu conector não enviará eventos até o dia seguinte (à meia-noite UTC).

Para fazer upgrade do seu conector de teste de Currents, edite a integração no dashboard e selecione **Upgrade Test Integration**.

## Atualização do Currents {#updating-currents}

{% multi_lang_include currents/updating_currents.md %}

## Lista de permissões de IP {#ip-allowlisting}

A Braze enviará dados do Currents a partir dos IPs listados:

{% multi_lang_include administer/data_centers.md datacenters='ips' %}