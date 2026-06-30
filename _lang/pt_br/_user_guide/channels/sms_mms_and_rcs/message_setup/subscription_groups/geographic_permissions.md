---
nav_title: "Permissões geográficas"
article_title: "Permissões geográficas"
description: "Este artigo aborda a lista de permissões de países para permissões geográficas, que permite escolher para quais países SMS, MMS e RCS podem ser entregues."
page_order: 0
page_type: reference
channel:
  - SMS
  - MMS
  - RCS
alias: /geographic_permissions/

---

# Permissões geográficas {#geographic-permissions}

> As permissões geográficas aumentam a segurança e protegem contra tráfego fraudulento de SMS, MMS e RCS, aplicando controles sobre os países para os quais você pode enviar mensagens. Você pode especificar uma lista de permissões de países para garantir que mensagens SMS, MMS e RCS sejam enviadas apenas para regiões aprovadas. As mensagens são enviadas somente para números de telefone com os códigos de discagem desses países.<br><br> Somente administradores podem fazer alterações na lista de permissões de países. Usuários não administradores têm acesso a uma versão somente leitura da lista de permissões, que indica para quais países um grupo de inscrições pode enviar mensagens.

Se você é administrador, pode configurar os países que estão na lista de permissões. A lista de permissões de países é configurada no nível do [grupo de inscrições]({{site.baseurl}}/sms_rcs_subscription_groups). Você pode acessá-la em **Público** > **Gerenciamento de grupos de inscrições** e selecionando um grupo de inscrições de SMS, MMS ou RCS. A lista de permissões está em **Geographic Permissions**.

![A seção editável de permissões geográficas para um administrador, com vários países selecionados na "Country allowlist".]({% image_buster /assets/img/sms/sms_geographic_permissions.png %}){: style="max-width:80%;"}

## Selecionando países {#selecting-countries}

Adicione países à lista de permissões usando o menu suspenso. Os países mais comuns para SMS, MMS e RCS aparecem no topo, com os demais exibidos abaixo. Você também pode pesquisar países digitando no campo de texto.

![O menu suspenso "Country allowlist" com os países mais comuns exibidos no topo.]({% image_buster /assets/img/sms/allowlist_dropdown.png %}){: style="max-width:80%;"}

Remova países previamente selecionados desmarcando as respectivas caixas ao lado deles.

### Salvando suas alterações {#saving-your-changes}

As alterações entrarão em vigor após você salvar. Remover países da sua lista de permissões impedirá que todas as mensagens SMS, MMS e RCS sejam enviadas para números de telefone com os códigos de discagem desses países.

![Modal de aviso confirmando os países que serão removidos da lista de permissões.]({% image_buster /assets/img/sms/delete_allowlist_warning.png %}){: style="max-width:70%;"}

## Países com alto risco de fraude {#high-fraud-risk-countries}

Certos países apresentam um risco maior de tráfego inflado de SMS, MMS e RCS. Esses países são indicados por uma tag **High Fraud Risk** no menu suspenso de países.

![O menu suspenso de países com o Azerbaijão exibindo uma tag "High Fraud Risk".]({% image_buster /assets/img/sms/high_risk.png %}){: style="max-width:80%;"}

Se você permitir o envio para esses países, primeiro deverá reconhecer o risco antes que o país seja adicionado à sua lista de permissões.

{% alert note %}
Limite os países na sua lista de permissões apenas àqueles necessários para atender às necessidades do seu negócio. Isso minimizará o potencial de tráfego fraudulento. Para mais orientações sobre como prevenir o tráfego inflado de SMS, MMS e RCS, consulte as [Perguntas frequentes sobre fraude de tráfego inflado de SMS]({{site.baseurl}}/sms_traffic_pumping_fraud).
{% endalert %}

## Visibilidade de envios fora da lista de permissões {#visibility-of-sends-outside-the-allowlist}

Tentativas de envio para países que não estão na sua lista de permissões serão abortadas. As mensagens abortadas serão registradas no [Registro de atividades de envio de mensagem]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log) e no [evento de engajamento com mensagem SMS abortada]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events).

As mensagens abortadas para destinatários em países que não estão na sua lista de permissões aparecem como **Aborted Message Errors** e exibem a mensagem "The recipient's phone number is in a blocked country".

![Registro de abortos mostrando vários envios de SMS, MMS e RCS abortados porque o país do número de telefone não está na lista de permissões.]({% image_buster /assets/img/sms/abort_log.png %}){: style="max-width:80%;"}

## Aviso importante sobre países com alto risco de fraude e fraude de tráfego inflado {#important-notice-for-high-fraud-risk-countries-and-traffic-pumping-fraud}

### O que é tráfego inflado de SMS, MMS e RCS? {#what-is-sms-mms-and-rcs-traffic-pumping}

O tráfego inflado de SMS, MMS e RCS (também conhecido como tráfego artificialmente inflado) é um esquema de fraude crescente que pode resultar em exposição financeira significativa para os clientes. Fraudadores podem explorar formulários web públicos desprotegidos, fluxos de autenticação ou endpoints de API para disparar grandes volumes de envios de SMS, MMS e RCS (como confirmações de opt-in, senhas de uso único ou notificações) para números de telefone que eles controlam ou influenciam. Os invasores então recebem uma parcela da receita de redes móveis cúmplices ou desavisadas por gerar esse tráfego artificial. O impacto resultante introduz uma exposição financeira significativa.

### O que são países com alto risco de fraude? {#what-are-high-fraud-risk-countries}

Um país ou território é designado como de alto risco de fraude se possuir uma densidade incomumente alta de pequenas operadoras locais de roaming com tarifas premium ou se não tiver supervisão regulatória rigorosa. Agentes mal-intencionados visam sistematicamente essas redes de operadoras com tarifas altas porque elas maximizam o pagamento de participação na receita por mensagem gerada.

Além disso, as restrições de roteamento do sistema são aplicadas com base nos códigos de país de destino, e não na localização física real do destinatário. Isso significa que, se você tem clientes que viajam com frequência, não precisa adicionar os locais de viagem deles à sua lista de permissões de países, pois o envio de mensagens será roteado com base no código de país de destino original, e não na localização física atual. Por exemplo, territórios que compartilham um código de país com regiões de menor risco (como Jersey ou Guernsey, que compartilham o código de país +44 com o Reino Unido) ainda apresentam alta exposição a tarifas de operadoras e são gerenciados sob as mesmas condições de alto risco de fraude.

### Responsabilidade do cliente e responsabilidade financeira {#customer-responsibility-and-financial-liability}

O cliente é responsável e será faturado por todas as mensagens móveis enviadas por meio dos serviços em seu nome, incluindo quaisquer mensagens resultantes de tráfego inflado de SMS, MMS e RCS. As proteções da plataforma, como a lista de permissões de países, ajudarão você a restringir a entrega a regiões confiáveis. No entanto, em última análise, proteger seus endpoints externos e prevenir danos financeiros devastadores é de responsabilidade exclusiva do cliente.

### Como prevenir o tráfego inflado {#how-to-prevent-traffic-pumping}

Não limitar a distribuição de mensagens estritamente às regiões geográficas onde seus clientes reais residem cria vulnerabilidade imediata a fraudes e danos financeiros graves. Para proteger sua empresa, você deve restringir proativamente suas regiões de entrega usando a lista de permissões de países. Além disso, e mais importante, você deve proteger qualquer formulário online de solicitação de número de telefone ou endpoint de API que dispare envios de SMS, MMS e RCS de acordo com as melhores práticas do setor, conforme descrito em [Entendendo e prevenindo fraude de tráfego inflado de SMS, MMS e RCS]({{site.baseurl}}/sms_traffic_pumping_fraud).