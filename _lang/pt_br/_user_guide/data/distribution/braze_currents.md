---
page_order: 1
nav_title: Currents
article_title: Currents

layout: dev_guide

page_type: landing
description: "Saiba como configurar o Braze Currents, conheça os parceiros de dados, a semântica de entrega e os glossários de eventos para exportação de dados de engajamento."
tool: currents
search_rank: 9
guide_top_header: "Braze Currents"
guide_top_text: "Compreender o impacto da sua estratégia de engajamento é fundamental para orientar a iteração e a otimização das suas comunicações com os usuários. Para integrar de forma eficaz esses valiosos dados de engajamento com o restante de suas operações e ajudar a amplificar seu investimento em ciência de dados, a plataforma Braze rastreia uma ampla gama de dados de eventos da sua integração para análise de dados, redirecionamento e outros casos de uso em seus próprios sistemas. <br> <br>A ferramenta Currents é um fluxo de dados em tempo real dos seus eventos de engajamento — a exportação mais robusta e granular da plataforma Braze. Ela fornece dados em um tipo de arquivo Avro para um de nossos muitos <a href='/docs/user_guide/data/distribution/braze_currents/setting_up_currents/available_partners'>parceiros de dados</a>, permitindo que você use os dados exclusivos e valiosos que a Braze cria para potencializar seus esforços de business intelligence (BI) e análise de dados em outras plataformas de primeira linha."

guide_featured_title: "Artigos da seção"
guide_featured_list:
  - name: Configurar Currents
    link: /docs/user_guide/data/distribution/braze_currents/setting_up_currents
    image: /assets/img/braze_icons/building-01.svg
  - name: Glossário de eventos do Currents
    link: /docs/user_guide/data/distribution/braze_currents/event_glossary
    image: /assets/img/braze_icons/data.svg
  - name: Casos de uso
    link: /docs/user_guide/data/distribution/braze_currents/use_cases
    image: /assets/img/braze_icons/expand-05.svg
  - name: FAQ
    link: /docs/user_guide/data/distribution/braze_currents/faq
    image: /assets/img/braze_icons/annotation-question.svg
---

## Recursos do Currents {#currents-capabilities}

O Currents permite que você:
* Transmita dados de eventos da Braze para um data warehouse ou para um dos nossos [parceiros de análise de dados]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/available_partners) para uma análise detalhada.
* Transmita dados de eventos da Braze continuamente para alimentar ferramentas de business intelligence, algoritmos de machine learning e muito mais.
* Encaminhe dados de eventos da Braze para diversos outros sistemas usando [Tealium]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/tealium/tealium), [Segment]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/segment/segment) ou [mParticle]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/mparticle/mparticle_for_currents).

Há muito mais que você pode fazer com dados de eventos acessados pelo Currents. [A Braze também usa o Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/use_cases/how_braze_uses_currents)!

## Modelo de distribuição de dados do Currents {#currents-data-distribution-model}

O Currents usa pools de direitos para controlar a criação de conectores e o rastreamento opcional de eventos.

- **Direitos de Engagement Events** são necessários para cada conector padrão do Currents que você criar.
- **Direitos de Customer Behavior Events** são necessários quando você ativa **Track Customer Behavior and User Events** em um conector.
- **Direitos de User Profiles and Attributes** são necessários quando você ativa **Track user profiles and attributes** em um conector.

Conectores de teste do Currents usam um limite de teste separado e não consomem direitos de conectores padrão.

Se você atingir qualquer limite de direitos, consulte a [solução de problemas de Configurar Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents#troubleshooting) e as [Perguntas frequentes sobre Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/faq), ou entre em contato com seu gerente de conta.

## Como acessar o Currents {#how-to-access-currents}

Um conector do Currents já está incluído em muitos dos nossos pacotes de nível profissional e empresarial. Se você tiver interesse em usar o Currents, entre em contato com o gerente da sua conta. O gerente da sua conta e nossos especialistas em dados podem ajudar na [configuração e integração do Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents).

<br><br>