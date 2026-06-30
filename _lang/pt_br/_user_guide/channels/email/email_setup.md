---
nav_title: "Configuração"
article_title: Configuração de e-mail
layout: dev_guide
page_order: 0
guide_top_header: "Configuração de e-mail"
guide_top_text: "A Braze pode ajudar você a começar a enviar campanhas de e-mail. Siga nossos guias ou confira nosso <a href='https://learning.braze.com/email-onboarding-for-pro-and-enterprise-achieving-high-deliverability' target='_blank'>curso de integração de e-mail</a> do Braze Learning."
page_type: landing
description: "Essa landing page inclui recursos sobre como começar a usar campanhas de e-mail, incluindo a configuração de seus IPs e domínios, aquecimento de IP, validação de e-mail e muito mais."
channel: email

guide_featured_title: "Artigos da seção"
guide_featured_list:
- name: "Configuração de IPs e domínios"
  link: /docs/user_guide/channels/email/email_setup/setting_up_ips_and_domains
  image: /assets/img/braze_icons/target-05.svg
- name: "Aquecimento de IP"
  link: /docs/user_guide/channels/email/email_setup/ip_warming
  image: /assets/img/braze_icons/annotation-alert.svg
- name: "Validação de e-mail"
  link: /docs/user_guide/channels/email/email_setup/email_validation
  image: /assets/img/braze_icons/check-square-broken.svg
- name: "Autenticação de e-mail"
  link: /docs/user_guide/channels/email/email_setup/authentication
  image: /assets/img/braze_icons/user-square.svg
- name: "Importe sua lista de e-mails"
  link: /docs/user_guide/channels/email/email_setup/import_your_email_list
  image: /assets/img/braze_icons/list.svg
- name: "Visão geral do SSL"
  link: /docs/user_guide/channels/email/email_setup/ssl
  image: /assets/img/braze_icons/navigation-pointer-01.svg
- name: "Consentimento e coleta de endereços"
  link: /docs/user_guide/channels/email/email_setup/consent_and_address_collection
  image: /assets/img/braze_icons/book-closed.svg
- name: "Armadilhas da entregabilidade e armadilhas de spam"
  link: /docs/user_guide/channels/email/email_setup/deliverability_pitfalls_and_spam_traps
  image: /assets/img/braze_icons/alert-triangle.svg
- name: "Pixel de abertura e rastreamento de cliques"
  link: /docs/user_guide/channels/email/email_setup/open_pixel_and_click_tracking
  image: /assets/img/braze_icons/cursor-click-02.svg
---

## Requisitos {#requirements}

Antes de começar a enviar e-mails, você precisa de alguns itens. Consulte a tabela a seguir para saber mais sobre esses requisitos.

| Requisito | Descrição | Origem |
|---|---|---|
| Um IP (Protocolo de Internet) dedicado | Um IP dedicado é um endereço de Internet exclusivo fornecido exclusivamente para uma única conta de hospedagem. | A Braze fornece IPs dedicados para garantir o controle da reputação do remetente do seu e-mail. A integração da Braze configurará isso para você. |
| Domínios com marca branca | Eles consistem em um domínio e um subdomínio. Ao usar a marca branca, você pode passar nas verificações de autenticação de e-mail para DKIM e SPF. | A equipe de integração da Braze gerará esses domínios para você, mas você deve escolher os nomes. |
| Subdomínios | Trata-se de uma subdivisão de um domínio (como "@news.company.com") em seu endereço de e-mail. Ter um subdomínio evitará erros que possam prejudicar a reputação do e-mail oficial de sua empresa. | A equipe de integração gerará isso para você, mas você deve decidir o nome do subdomínio. Não é possível usar subdomínios que estejam sendo usados atualmente fora da Braze. |
| Pools de IP | Trata-se de uma configuração opcional usada para separar a reputação de diferentes tipos de e-mail (como "promocional" e "transacional") para evitar que a reputação de um afete o outro e para oferecer maior entregabilidade. | A equipe de integração configurará os pools para você. Depois, ao compor seu e-mail, você pode visualizar o pool de IP do seu e-mail na etapa **Público-alvo**. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Requisitos" }

## Aquecimento de IP {#ip-warming}

{% alert important %}
O aquecimento de IP é a **etapa mais importante** no processo de configuração de e-mail. Embora não seja sua primeira etapa (na verdade, é a última), estamos destacando aqui para informar que você deve aquecer seu endereço IP. Caso contrário, qualquer e-mail que você enviar será direcionado para spam ou estará sujeito a outras barreiras de envio.
{% endalert %}

O [aquecimento de IP]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming) é quando você envia um número relativamente pequeno de e-mails no seu primeiro lote e, ao longo do tempo, aumenta gradualmente o volume nos lotes seguintes até atingir seu volume diário típico. Isso é feito no final do processo de configuração de e-mail.

Ao começar com volumes menores de e-mail, você estabelece um nível de confiança com seu provedor de e-mail, mostrando que está enviando e-mails apenas para usuários relevantes. Enviar seu primeiro lote de e-mails para seus usuários mais engajados pode ajudar a ganhar confiança mais rapidamente com seu provedor.

Depois de concluir o aquecimento do seu IP, você pode [começar a criar e enviar e-mails]({{site.baseurl}}/user_guide/channels/email/html_editor)!

## E-mails de transação legalmente obrigatórios {#legally-required-transactional-emails}

{% multi_lang_include alerts/important_alerts.md alert='Email via SMS' %}

<br><br>