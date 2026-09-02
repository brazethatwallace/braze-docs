---
nav_title: Dados do Segment or segmento
article_title: Exportar dados do Segment or segmento
page_order: 4
page_type: reference
description: "Este artigo de referência aborda como exportar dados de Segment or segmento or segmento para CSV, as permissões necessárias para exportar dados de usuários, exportações de etapas do Canvas e os campos incluídos na exportação."
---

# Exportar dados do Segment or segmento or segmento para CSV {#export-segment-data-to-csv}

> Esta página aborda como solicitar uma exportação CSV de dados de usuários de um Segment or segmento or segmento e os dados incluídos na exportação.

{% alert note %}
As opções de exportação CSV aparecem no menu suspenso **User Data** apenas para usuários da empresa que possuem a [permissão "Export User Data"]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) para esse espaço de trabalho.
{% endalert %}

Para exportar dados de Segment or segmento or segmento para um CSV, selecione o menu suspenso **User Data** ao editar um Segment or segmento or segmento e selecione exportar os dados do usuário ou os endereços de e-mail do Segment or segmento or segmento.

![Seção de informações do Segment or segmento or segmento com o menu suspenso User Data mostrando opções de exportação.]({% image_buster /assets/img_archive/csvexport.png %})

Você também pode solicitar uma exportação CSV na página principal de **Segments**, selecionando o menu suspenso <i class="fas fa-gear" aria-label="Configurações"></i> **Settings** de um Segment or segmento or segmento:

![Menu suspenso Settings na página principal de Segments.]({% image_buster /assets/img_archive/csvexport2.png %})

{% alert tip %}
Para exportar dados de todos os seus perfis de usuários, crie um Segment or segmento or segmento sem filtros e solicite uma exportação CSV.
{% endalert %}

A saída CSV contém os dados de cada perfil de usuário capturado no Segment or segmento or segmento no momento da exportação. Você pode exportar qualquer Segment or segmento or segmento selecionando o ícone de engrenagem e a exportação CSV. A Braze gerará o relatório em segundo plano e o enviará por e-mail para o usuário que estiver conectado no momento.

## Detalhes da exportação CSV de Segments {#segment-csv-export-details}

{% alert note %}
Os usuários do dashboard precisam da permissão **Exportar dados de usuários** para usar as opções de exportação CSV. Se não tiverem essa permissão, as opções de exportação CSV não aparecerão.
{% endalert %}

**CSV Export Email Addresses** inclui apenas linhas de usuários no Segment or segmento que possuem um endereço de e-mail. Por exemplo, se o seu Segment or segmento tem 100.000 usuários, mas apenas 50.000 possuem um endereço de e-mail, **CSV Export Email Addresses** produz cerca de 50.000 linhas. **CSV Export User Data** exporta todos os dados de usuários do Segment or segmento.

{% alert important %}
Devido a restrições de tamanho de arquivo, sua exportação pode falhar se o tamanho estimado do seu Segment or segmento for superior a 500.000 usuários. Essa restrição usa o tamanho estimado do seu Segment or segmento, e não o cálculo exato. Para mais detalhes, consulte [Exportando Segments grandes](#exporting-large-segments).
{% endalert %}

Se você vinculou suas [credenciais do Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3#integration) à Braze, o CSV será enviado para o seu bucket S3 com a chave `segment-export/SEGMENT_ID/YYYY-MM-dd/users-RANDOMSTRING.zip`. Você precisa estar conectado ao dashboard para acessar o link de download enviado por e-mail.

{% multi_lang_include alerts/important_alerts.md alert='S3 file bucket export' %}

## Dados incluídos na exportação {#data-included-in-export}

Os dados a seguir são incluídos na sua exportação, dependendo da sua seleção.

### Exportação CSV de dados de usuários {#csv-export-user-data}

| Nome do campo                  | Descrição                                              |
| --------------------------- | -------------------------------------------------------- |
| Appboy ID                   | ID interno (não pode ser alterado)                           |
| country                     | País                                    |
| created_at                  | Data e hora em que o perfil de usuário foi criado                   |
| created_from                | Método utilizado para criar o perfil de usuário (por exemplo, REST or transferir estado representacional API or interface de programação do aplicativo (API), SDK or kit de desenvolvimento de software ou importação CSV)         |
| devices                     | Informações do dispositivo                           |
| date_of_birth               | Data de nascimento                                            |
| email                       | Endereço de e-mail                                            |
| unsubscribed_from_emails_at | Data de cancelamento de inscrição de e-mails                            |
| user_id                     | ID externo                                              |
| first_name                  | Nome                                               |
| first_session               | Data e hora da primeira sessão                           |
| gender                      | Gênero                                                   |
| google_ad_ids               | IDs de publicidade do Google associados ao usuário                      |
| city                        | Cidade                                     |
| IDFAs                       | Valores de Identificador para Publicidade (IDFA)                 |
| IDFVs                       | Valores de Identificador para Fornecedor (IDFV)                      |
| language                    | Idioma no padrão ISO-639-1                                        |
| last_app_version_used       | Última versão do app utilizada                             |
| last_name                   | Sobrenome                                                |
| last_session                | Data e hora da última sessão                            |
| number_of_google_ad_ids     | Contagem de IDs de publicidade do Google associados               |
| number_of_IDFAs             | Contagem de IDFAs associados                                |
| number_of_IDFVs             | Contagem de IDFVs associados                                |
| number_of_push_tokens       | Contagem de tokens de notificação por push associados             |
| number_of_roku_ad_ids       | Contagem de IDs de publicidade Roku associados                 |
| number_of_windows_ad_ids    | Contagem de IDs de publicidade Windows associados              |
| phone_number                | Número de telefone                                             |
| opted_into_push_at          | Data de aceitação de notificações por push                       |
| unsubscribed_from_push_at   | Data de cancelamento de inscrição de notificações por push                |
| random_bucket               | Número de bucket aleatório                                 |
| roku_ad_ids                 | IDs de publicidade Roku                          |
| session_count               | Número total de sessões                                 |
| timezone                    | Fuso horário do usuário no mesmo formato do Banco de Dados de Fusos Horários IANA                                         |
| in_app_purchase_total       | Valor total gasto em compras no app                   |
| user_aliases                | Aliases do usuário, se houver                                          |
| windows_ad_ids              | IDs de publicidade Windows                       |
| Custom events               | Com base na seleção na exportação                             |
| Custom attributes           | Com base na seleção na exportação                             |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Exportação CSV de dados de usuários" }

{% alert note %}
Ao exportar dados de usuários de uma etapa do Canvas, o CSV inclui todos os usuários que passaram por essa etapa durante toda a vida útil da etapa do Canvas. Não é possível limitar a exportação a um intervalo de datas ou outra janela de tempo. Para saber como executar essas exportações, consulte [Exportar dados do Canvas]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_canvas_data).
{% endalert %}

### Exportação CSV de endereços de e-mail {#csv-export-email-addresses}

| Nome do campo                  | Descrição            |
| --------------------------- | ---------------------- |
| user_id                     | ID externo do usuário     |
| first_name                  | Nome             |
| last_name                   | Sobrenome              |
| email                       | E-mail                  |
| unsubscribed_from_emails_at | Data de cancelamento de inscrição de e-mail |
| opted_in_to_emails_at       | Data de aceitação de e-mail      |
| user_aliases                | Aliases do usuário, se houver   |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Exportação CSV de endereços de e-mail" }

{% alert tip %}
Para obter ajuda com exportações CSV e API or interface de programação do aplicativo (API), acesse nosso artigo de [solução de problemas]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting).
{% endalert %}

{% alert note %}
Os dados de grupo de inscrições não estão disponíveis por meio de exportações de Segments. Para identificar usuários por status de inscrição, crie um Segment or segmento separado com base na associação ao grupo de inscrições e exporte esse Segment or segmento.
{% endalert %}

## Exportando Segments grandes {#exporting-large-segments}

Existem vários métodos para exportar um Segment or segmento grande que contenha mais de 500.000 usuários.

{% tabs %}
{% tab Múltiplos Segments %}

Você pode dividir um Segment or segmento grande em Segments menores e depois exportar cada um dos Segments menores da Braze.

{% endtab %}
{% tab Números de bucket aleatórios %}

Você também pode usar [números de bucket aleatórios]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers) para dividir sua base de usuários em múltiplos Segments e depois combiná-los após a exportação. Por exemplo, se você precisar dividir seu Segment or segmento em dois Segments diferentes, pode fazer isso com os seguintes filtros:
- Segment or segmento 1: O número de bucket aleatório é menor que 5000 (inclui 0-4999)
- Segment or segmento 2: O número de bucket aleatório é maior que 4999 (inclui 5000-9999)

{% endtab %}
{% tab Endpoints %}

Você também pode alavancar os seguintes endpoints para exportar dados de usuários de um Segment or segmento específico. Note que esses endpoints estão sujeitos a limites de dados e [limites de frequência]({{site.baseurl}}/api/basics).
- [`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment)
- [`/users/export/global_control_group`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group)

Se você conectou [credenciais do Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3#integration), exportações grandes podem ser entregues ao seu bucket, além do link de download enviado por e-mail, conforme descrito em [Detalhes da exportação CSV de Segment or segmento](#segment-csv-export-details).

{% endtab %}
{% endtabs %}