---
nav_title: Google Tag Manager
article_title: Google Tag Manager com o SDK da Braze
platform:
  - Android
  - FireOS
  - Swift
page_order: 1.1
description: "Aprenda como inicializar o SDK da Braze usando métodos como inicialização em tempo de execução, inicialização atrasada ou Google Tag Manager."

---

# Google Tag Manager com o SDK da Braze {#google-tag-manager-with-the-braze-sdk}

> Aprenda como usar o [Google Tag Manager (GTM)](https://developers.google.com/tag-platform/tag-manager) com o SDK da Braze, para que você possa controlar remotamente o rastreamento de eventos da Braze e as atualizações de atributos de usuário sem precisar de alterações de código ou novas versões do app.

{% sdktabs %}
{% sdktab web %}
{% multi_lang_include developer_guide/web/google_tag_manager.md %}
{% endsdktab %}

{% sdktab android %}
{% multi_lang_include developer_guide/android/google_tag_manager.md %}
{% endsdktab %}

{% sdktab swift %}
{% multi_lang_include developer_guide/swift/google_tag_manager.md %}
{% endsdktab %}
{% endsdktabs %}

## Solução de problemas {#troubleshooting}

Se a Braze não inicializar ou os eventos não aparecerem como esperado, confirme se o contêiner do GTM está publicado, se os disparadores e a ordem de acionamento das tags estão alinhados com o [ciclo de vida e a estratégia de inicialização]({{site.baseurl}}/developer_guide/sdk_integration) do seu SDK, e se os dispositivos de teste não estão bloqueando os endpoints da Braze.

Para falhas de inicialização, verifique se a tag da Braze ou o provedor de tag personalizado está recebendo o `actionType` e os parâmetros esperados (consulte as guias Android, Swift e Web nesta página). Para obter um registro detalhado ao validar eventos disparados pelo GTM, ative o registro de depuração do SDK da sua plataforma conforme descrito nos guias de integração vinculados nessas guias.