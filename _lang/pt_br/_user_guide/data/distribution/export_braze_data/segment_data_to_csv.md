---
nav_title: Dados do Segment
article_title: Exportar dados do Segment
page_order: 4
page_type: reference
description: "Este artigo de referência aborda como exportar dados de segmento para CSV, as permissões necessárias para exportar dados de usuários, exportações de etapas do Canvas e os campos incluídos na exportação."

---

# Exportar dados do segmento para CSV {#export-segment-data-to-csv}

> Esta página aborda como solicitar uma exportação CSV de dados de usuários de um segmento e os dados incluídos na exportação.

{% alert note %}
As opções de exportação CSV aparecem no menu suspenso **User Data** apenas para usuários da empresa que possuem a [permissão "Export User Data"]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/) para esse espaço de trabalho.
{% endalert %}

Para exportar dados de segmento para um CSV, selecione o menu suspenso **User Data** ao editar um segmento e selecione exportar os dados do usuário ou os endereços de e-mail do segmento.

![Seção de informações do segmento com o menu suspenso User Data mostrando opções de exportação.]({% image_buster /assets/img_archive/csvexport.png %})

Você também pode solicitar uma exportação CSV na página principal de **Segments**, selecionando o menu suspenso <i class="fas fa-gear"></i> **Settings** de um segmento:

![Menu suspenso Settings na página principal de Segments.]({% image_buster /assets/img_archive/csvexport2.png %})

{% alert tip %}
Para exportar dados de todos os seus perfis de usuários, crie um segmento sem filtros e solicite uma exportação CSV.
{% endalert %}

A saída CSV contém os dados de cada perfil de usuário capturado no segmento no momento da exportação. Você pode exportar qualquer segmento selecionando o ícone de engrenagem e a exportação CSV. A Braze gerará o relatório em segundo plano e o enviará por e-mail para o usuário que estiver conectado no momento.

## Detalhes da exportação CSV de segmento {#segment-csv-export-details}

{% alert note %}
Os usuários do dashboard precisam da permissão **Export user data** para usar as opções de exportação CSV. Se não tiverem essa permissão, as opções de exportação CSV não aparecerão.
{% endalert %}

**Exportar endereços de e-mail em CSV** inclui apenas linhas de usuários no segmento que possuem um endereço de e-mail. Por exemplo, se o seu segmento tem 100.000 usuários, mas apenas 50.000 possuem um endereço de e-mail, **Exportar endereços de e-mail em CSV** produzirá cerca de 50.000 linhas. **Exportar dados de usuários em CSV** exporta todos os dados de usuários do segmento.

{% alert important %}
Devido a restrições de tamanho de arquivo, sua exportação poderá falhar se o tamanho estimado do seu segmento for superior a 500.000 usuários. Note que essa restrição usa o tamanho estimado do seu segmento, e não o cálculo exato. Para mais detalhes, consulte [Exportação de segmentos grandes](#exporting-large-segments).
{% endalert %}

Se você tiver vinculado suas [credenciais do Amazon S3]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/amazon_s3/#amazon-s3-integration) à Braze, o CSV será enviado para o seu bucket S3 com a chave `segment-export/SEGMENT_ID/YYYY-MM-dd/users-RANDOMSTRING.zip`. É necessário estar conectado ao dashboard para acessar o link de download enviado por e-mail.

{% multi_lang_include alerts/important_alerts.md alert='S3 file bucket export' %}

## Dados incluídos na exportação {#data-included-in-export}

Os itens a seguir estão incluídos na sua exportação, dependendo da sua seleção.

### Exportar dados de usuários em CSV {#csv-export-user-data}

| Nome do campo                 | Descrição                                              |
| --------------------------- | -------------------------------------------------------- |
| Appboy ID                   | ID interna (não pode ser alterada)                           |
| country                     | País                                    |
| created_at                  | Data e hora em que o perfil do usuário foi criado                   |
| created_from                | Método usado para criar o perfil do usuário (por exemplo, REST API, SDK ou importação CSV)         |
| devices                     | Informações sobre o dispositivo                           |
| date_of_birth               | Data de nascimento                                            |
| email                       | Endereço de e-mail                                            |
| unsubscribed_from_emails_at | Data de cancelamento da inscrição de e-mails                            |
| user_id                     | ID externo                                              |
| first_name                  | Nome                                               |
| first_session               | Data e hora da primeira sessão                           |
| gender                      | Gênero                                                   |
| google_ad_ids               | IDs de publicidade do Google associados ao usuário                      |
| city                        | Cidade                                     |
| IDFAs                       | Valores do identificador para publicidade (IDFA)                 |
| IDFVs                       | Valores do identificador do fornecedor (IDFV)                      |
| language                    | Idioma no padrão ISO-639-1                                        |
| last_app_version_used       | Última versão do app usada                             |
| last_name                   | Sobrenome                                                |
| last_session                | Data e hora da última sessão                            |
| number_of_google_ad_ids     | Contagem de IDs de publicidade do Google associados               |
| number_of_IDFAs             | Contagem de IDFAs associados                                |
| number_of_IDFVs             | Contagem de IDFVs associados                                |
| number_of_push_tokens       | Contagem de tokens de notificação por push associados             |
| number_of_roku_ad_ids       | Contagem de IDs de publicidade Roku associados                 |
| number_of_windows_ad_ids    | Contagem de IDs de publicidade do Windows associados              |
| phone_number                | Número de telefone                                             |
| opted_into_push_at          | Data de opt-in nas notificações por push                       |
| unsubscribed_from_push_at   | Data de cancelamento da inscrição nas notificações por push                |
| random_bucket               | Número aleatório do bucket                                 |
| roku_ad_ids                 | IDs de publicidade da Roku                          |
| session_count               | Número total de sessões                                 |
| timezone                    | Fuso horário do usuário no mesmo formato do banco de dados de fuso horário da IANA                                         |
| in_app_purchase_total       | Valor total gasto em compras no app                   |
| user_aliases                | Aliases de usuário, se houver                                          |
| windows_ad_ids              | IDs de publicidade do Windows                       |
| Eventos personalizados               | Com base na seleção na exportação                             |
| Atributos personalizados           | Com base na seleção na exportação                             |
{: .reset-td-br-1 .reset-td-br-2 aria-label="CSV export user data" }

{% alert note %}
Quando você exporta dados de usuários de uma etapa do Canvas, o CSV inclui todos os usuários que passaram por essa etapa ao longo de toda a vida útil da etapa do Canvas. Não é possível limitar a exportação a um intervalo de datas ou outro período. Para saber como executar essas exportações, consulte [Exportar dados do Canvas]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_canvas_data/).
{% endalert %}

### Exportar endereços de e-mail em CSV {#csv-export-email-addresses}

| Nome do campo                 | Descrição            |
| --------------------------- | ---------------------- |
| user_id                     | ID externo do usuário     |
| first_name                  | Nome             |
| last_name                   | Sobrenome              |
| email                       | E-mail                  |
| unsubscribed_from_emails_at | Data de cancelamento da inscrição do e-mail |
| opted_in_to_emails_at       | Data de opt-in do e-mail      |
| user_aliases                | Aliases de usuário, se houver   |
{: .reset-td-br-1 .reset-td-br-2 aria-label="CSV Export Email Addresses" }

{% alert tip %}
Para obter ajuda com exportações CSV e API, visite nosso artigo de [solução de problemas]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting/).
{% endalert %}

{% alert note %}
Os dados de grupos de inscrições não estão disponíveis por meio de exportações de segmento. Para identificar usuários por status de inscrição, crie um segmento separado com base na associação ao grupo de inscrições e exporte esse segmento.
{% endalert %}

## Exportação de segmentos grandes {#exporting-large-segments}

Há vários métodos para exportar um segmento grande de usuários que contém mais de 500.000 usuários.

{% tabs %}
{% tab Múltiplos segmentos %}

Você pode dividir um segmento grande em segmentos menores e, em seguida, exportar cada um dos segmentos menores da Braze.

{% endtab %}
{% tab Números aleatórios de bucket %}

Você também pode usar [números aleatórios de bucket]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers/) para dividir sua base de usuários em vários segmentos e combiná-los após a exportação. Por exemplo, se você precisar dividir seu segmento em dois segmentos diferentes, poderá fazer isso com os seguintes filtros:
- Segment 1: O número do bucket aleatório é menor que 5000 (inclui 0-4999)
- Segment 2: O número do bucket aleatório é maior que 4999 (inclui 5000-9999)

{% endtab %}
{% tab Endpoints %}

Também é possível usar os seguintes endpoints para exportar dados de usuários de um segmento específico. Note que esses endpoints estão sujeitos a limites de dados e [limites de taxa]({{site.baseurl}}/api/basics/).
- [`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/)
- [`/users/export/global_control_group`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group/)

Se você tiver conectado suas [credenciais do Amazon S3]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/amazon_s3/#amazon-s3-integration), exportações grandes podem ser entregues no seu bucket, além do link de download enviado por e-mail, conforme descrito em [Detalhes da exportação CSV de segmento](#segment-csv-export-details).

{% endtab %}
{% endtabs %}