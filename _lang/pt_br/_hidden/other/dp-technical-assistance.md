---
nav_title: Assistência técnica em proteção de dados
article_title: Assistência técnica de proteção de dados nos Serviços Braze
page_order: 1
description: "Esta página fornece instruções técnicas para que você gerencie, por meio dos Serviços Braze, solicitações de indivíduos em relação a seus direitos de dados pessoais."
alias: /help/dp-technical-assistance/
permalink: /dp-technical-assistance/
hide_toc: true
---

<!--
Warning! Don't make any changes to this document without approval from the legal department.
-->

# Assistência técnica de proteção de dados nos Serviços Braze {#data-protection-technical-assistance-in-the-braze-services}

Há uma série de leis de proteção de dados que regulam o que as organizações podem fazer com dados pessoais ("Leis de Proteção de Dados"), incluindo o Regulamento Geral de Proteção de Dados da UE e do Reino Unido ("GDPR"), a Lei de Privacidade do Consumidor da Califórnia ("CCPA") e a Lei de Portabilidade e Responsabilidade de Seguros de Saúde ("HIPAA"). Existem outras leis e regulamentações nacionais, estaduais e específicas do setor que podem se aplicar ao seu negócio.

Essas Leis de Proteção de Dados concedem aos indivíduos "direitos de privacidade" sobre seus dados pessoais. As organizações são obrigadas a receber e responder a solicitações de indivíduos que exercem seus direitos de privacidade. Os Serviços Braze podem ajudar você a cumprir essas Leis de Proteção de Dados, fornecendo recursos para facilitar determinadas ações exigidas por essas leis. Este documento fornece instruções técnicas para usar esses recursos para gerenciar solicitações de direitos de privacidade. Cabe a você determinar quais Leis de Proteção de Dados se aplicam ao seu negócio e agir em conformidade com elas.

## Isenção de responsabilidade legal {#legal-disclaimer}

Nenhuma das informações a seguir tem a intenção de ser, nem deve ser considerada, assessoria jurídica da Braze. Recomenda-se que você busque a orientação de seu próprio advogado com relação à sua situação específica e à forma como as Leis de Proteção de Dados se aplicam a você e ao seu uso dos Serviços Braze.

## Terminologia {#terminology}

Para os fins deste documento, qualquer referência a dados pessoais também pode ser entendida como uma referência a informações pessoais ou informações de identificação pessoal ("Dados Pessoais"). Para simplificar, geralmente usamos a linguagem do GDPR ao abordar os direitos dos usuários finais. A linguagem do GDPR é muitas vezes intercambiável ou estreitamente alinhada com um termo ou conceito definido de outras Leis de Proteção de Dados.

## Noções básicas {#the-basics}

A maioria das leis de privacidade define três partes interessadas principais envolvidas no processamento de Dados Pessoais: titulares de dados, controladores de dados e processadores de dados. Cada grupo tem direitos e responsabilidades diferentes com relação ao uso de Dados Pessoais:

- Um titular de dados é um indivíduo cujos Dados Pessoais estão sendo processados pelo processador ou controlador de dados
- Um controlador de dados é uma entidade que determina as finalidades e os meios do processamento de Dados Pessoais
- Um processador de dados é uma entidade que processa Dados Pessoais em nome e sob as instruções do controlador de dados

Em relação aos Serviços Braze:

- Os titulares dos dados são, por exemplo, os usuários finais do seu aplicativo de cliente (por exemplo, seus clientes) ou seus colaboradores que são usuários da empresa na sua instância dos Serviços Braze.
- Você, o cliente da Braze, é o controlador de dados que decide como e por que os Dados Pessoais dos titulares dos dados serão coletados e processados nos Serviços Braze.
- A Braze é uma processadora de dados que processa os Dados Pessoais nos Serviços Braze em seu nome e de acordo com as instruções que recebemos de você.

Os termos acima são do GDPR, mas, por exemplo, os termos comparáveis da CCPA são:
- "consumidores" para titulares de dados.
- "empresas" para controladores de dados.
- "prestadores de serviço" para processadores de dados.

Você encontrará abaixo informações relevantes sobre as solicitações de direitos de privacidade mais comuns dos titulares dos dados, incluindo como você pode respondê-las por meio dos recursos técnicos dos Serviços Braze.

## O direito de ser informado {#the-right-to-be-informed}

O direito de ser informado engloba sua obrigação de fornecer "informações de processamento justo", normalmente por meio de um aviso de privacidade. Ele enfatiza a necessidade de transparência sobre como você usa os Dados Pessoais.

### Recomendação da Braze {#braze-recommendation}

A maioria das Leis de Proteção de Dados enfatiza a necessidade de transparência em relação à forma como você usa os Dados Pessoais. Essa é a responsabilidade dos controladores de dados, que normalmente manterão um aviso de privacidade facilmente acessível aos usuários de seus produtos e serviços e que abranja o processamento feito pela Braze.

## O direito de acesso {#the-right-of-access}

De acordo com as Leis de Proteção de Dados, os titulares de dados podem ter o direito de obter:

- Confirmação de que seus Dados Pessoais estão sendo processados,
- Acesso a seus Dados Pessoais, e
- Outras informações complementares, conforme determinado pela Lei de Proteção de Dados aplicável.

### Recomendação da Braze

Para fornecer Dados Pessoais da Braze em um formato legível por máquina em resposta a uma solicitação de acesso do titular dos dados, você pode exportar o perfil do usuário final fazendo uma chamada de API para as [REST APIs]({{site.baseurl}}/api/endpoints/export/#user-export) da Braze com o identificador de usuário (definido por você como o `external_id` fornecido à Braze) e/ou o identificador do dispositivo.

#### BrazeAI Decisioning Studio™

Para atender a uma solicitação de direito de acesso em relação a Dados Pessoais no BrazeAI Decisioning Studio™, entre em contato com o gerente da sua conta com os customer_id(s) e/ou e-mail(s) relevantes.

## O direito de retificação {#the-right-to-rectification}

Os indivíduos têm o direito de ter seus Dados Pessoais corrigidos se estiverem imprecisos ou incompletos. Se você tiver divulgado os Dados Pessoais em questão a terceiros, poderá considerar a necessidade de informá-los sobre a retificação, quando possível.

### Recomendação da Braze

Caso um titular dos dados solicite a retificação de imprecisões nos Dados Pessoais que estão sendo processados por você ou pela Braze em seu nome, você pode usar os SDKs da Braze ou as [REST APIs]({{site.baseurl}}/api/endpoints/user_data/#user-track-endpoint) da Braze para corrigir esses Dados Pessoais.

## O direito à exclusão {#the-right-to-erasure}

O direito à exclusão também é conhecido como "direito de ser esquecido" ou "direito de ser excluído".

### Recomendação da Braze

#### Exclusão padrão {#standard-deletion}

Depois de interromper a coleta de dados, você pode usar o [endpoint da REST API de exclusão de usuário da Braze]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/) para excluir um usuário final, o que removerá todos os registros desse usuário final dos Serviços Braze:

- Para usuários finais que têm um external_id nos Serviços Braze, você pode usar esse ID para excluir os dados desse usuário final.
- Para usuários finais anônimos que não têm um external_id nos Serviços Braze, é possível recuperar o identificador de dispositivo desse usuário final usando o SDK da Braze e usar o identificador de dispositivo para encontrar o perfil de usuário final associado a esse dispositivo. Em seguida, é possível usar a API de exclusão de usuário para excluir o perfil associado a esse usuário final.

A exclusão de um usuário final dos Serviços Braze excluirá permanentemente o Perfil de Usuário centralizado da Braze para esse usuário final, conforme definido pelo `external_id` fornecido. Isso inclui informações de perfil estruturadas que a Braze coletou por padrão ou que você configurou os Serviços Braze para coletar, como informações do dispositivo, país, idioma e endereço de e-mail.

Observe que o endereço de e-mail ou o número de telefone associado ao perfil do usuário final ainda poderá ser armazenado pela Braze, pois poderá estar associado ao perfil de outro usuário final. Endereços de e-mail e números de telefone não são exclusivos nos Serviços Braze. Isso significa que sua equipe poderia ter configurado a Braze para armazenar o mesmo endereço de e-mail ou número de telefone em vários perfis de usuário. Se a sua equipe tiver configurado a Braze dessa forma, esteja ciente de que talvez seja necessário excluir todos os perfis de usuários que representam um determinado titular de dados para atender a uma solicitação de exclusão de um titular de dados, e sua equipe precisaria fazer várias chamadas de API para excluir todos os Perfis de Usuário que se referem a um determinado titular de dados.

#### BrazeAI Decisioning Studio™

Para atender a uma solicitação de direito à exclusão em relação a Dados Pessoais no BrazeAI Decisioning Studio™, entre em contato com o gerente da sua conta com os customer_id(s) e/ou e-mail(s) relevantes. O gerente da sua conta pode providenciar a exclusão de todos os dados pessoais associados encontrados no data warehouse.

#### Considerações adicionais sobre a exclusão {#additional-deletion-considerations}

<style>
#considerations td {
    word-break: break-word;
    width: 100%;
    font-size: 16px;
}
</style>

<table id="considerations">
  <caption>Considerações adicionais sobre a exclusão</caption>
<tbody>
  <tr>
    <td>
        <p>Os clientes podem criar campos personalizados para propriedades de eventos e extras de mensagens. Esses campos não se destinam a Dados Pessoais e, portanto, não estão incluídos no processo de exclusão padrão descrito acima. Se, no entanto, você usar a Braze para inserir ou coletar Dados Pessoais por meio de propriedades de eventos e extras de mensagens, poderá configurar o processo de exclusão disparado pelo endpoint da REST API de exclusão de usuários para incluir também esses campos, de modo que os dados contidos nesses campos também sejam excluídos.</p>
        <p>As configurações padrão são aplicadas no nível da empresa, mas você pode optar por excluir os seguintes campos quando o processo de exclusão for executado, no nível do grupo de app/espaço de trabalho:</p>
    <ul>
        <li>PROPERTIES para USERS_BEHAVIORS_CUSTOMEVENT</li>
        <li>PROPERTIES para USERS_BEHAVIORS_PURCHASE</li>
        <li>MESSAGE_EXTRAS para:
            <ul>
            <li>USERS_MESSAGES_CONTENTCARD</li>
            <li>USERS_MESSAGES_EMAIL_SEND</li>
            <li>USERS_MESSAGES_PUSHNOTIFICATION_SEND</li>
            <li>USERS_MESSAGES_PUSHNOTIFICATION_RETRYSEND_SHARED</li>
            <li>USERS_MESSAGES_WEBHOOK_SEND</li>
            <li>USERS_MESSAGES_SMS_SEND</li>
            <li>Eventos futuros de envio de mensagens</li>
            </ul>
        </li>
    </ul>
    <p>As configurações para isso podem ser acessadas em <b>Configurações da empresa</b> > <b>Configurações de administrador</b> > <b>Configurações de segurança</b>. As preferências de exclusão de dados são definidas por tipo ou categoria de evento. Somente um usuário com permissões de administrador pode fazer alterações nessas configurações. Como alternativa, um administrador pode delegar essas permissões a outro usuário.</p>
    <p>Se um tipo de evento ou extra de mensagem for definido para ser incluído no processo de exclusão, os dados desse campo serão excluídos dali em diante para os usuários para os quais você estiver executando o endpoint da REST API de exclusão de usuário. Além disso, quando você selecionar essa preferência de exclusão, no próximo trabalho de exclusão programado, os dados desses campos serão excluídos de quaisquer conjuntos de dados anonimizados existentes que contenham esses campos. Não será possível restaurar os campos de dados excluídos.</p>
    </td>
  </tr>
</tbody>
</table>

#### Análise de dados {#analytics}

Para manter a integridade da análise de uso de Campaigns e aplicativos, os dados agregados anônimos não serão modificados quando um usuário final for excluído. Por exemplo, a Braze não diminuirá o número total de sessões de um app quando um usuário final for excluído. A(s) sessão(ões) em que esse usuário final visitou o aplicativo ainda será(ão) incluída(s) no número total de visitas a esse aplicativo, mas esses dados não serão conectados de forma alguma ao perfil do usuário final esquecido, garantindo que esses dados anonimizados e agregados não possam ser vinculados a um usuário final individual.

As análises de dados nos Serviços Braze estão vinculadas ao identificador de usuário final da Braze. Depois que o perfil do usuário final for excluído, o identificador de usuário da Braze se tornará efetivamente um identificador completamente anônimo, pois a Braze não poderá vinculá-lo a nenhum usuário final individual.

#### Após a exclusão ter ocorrido {#once-deletion-has-happened}

Em geral, espera-se que você faça esforços razoáveis para notificar os titulares dos dados quando tiver atendido à solicitação deles para apagar seus Dados Pessoais. Um usuário final excluído poderá se registrar novamente ou se engajar novamente com seu app ou serviço em uma data posterior, e a Braze não poderá identificá-lo como o usuário excluído ou esquecido. Os Serviços Braze não são capazes de criar listas de identificadores de usuários ou endereços de e-mail excluídos em seu nome.

## O direito à restrição de processamento {#the-right-to-restriction-of-processing}

Os titulares dos dados podem ter o direito de "bloquear" ou suprimir o processamento de seus Dados Pessoais em determinadas circunstâncias. Restringir o processamento significa não realizar qualquer processamento ao qual o titular dos dados tenha se oposto.

### Recomendação da Braze

Os Serviços Braze não suportam a restrição do processamento de categorias individuais de Dados Pessoais. Caso tenha sido solicitado por um titular de dados a restringir o processamento de determinados subconjuntos dos Dados Pessoais desse titular, você deve usar as [APIs da Braze]({{site.baseurl}}/api/home/) para exportar todo(s) o(s) perfil(is) desse usuário final e, em seguida, [excluí-lo(s)]({{site.baseurl}}/api/endpoints/user_data/#user-delete-endpoint) da Braze. As APIs da Braze podem ser usadas para reimportar esses dados caso o usuário final permita posteriormente que você processe esses subconjuntos específicos de seus Dados Pessoais. Além disso, recomenda-se que o usuário final desinstale ou saia de todos os aplicativos que usam o SDK da Braze para interromper a coleta de dados adicionais sobre o titular dos dados.

Para clientes que usam apenas o BrazeAI Decisioning Studio™, você não deve mais enviar dados para o Decisioning Studio.

## O direito à portabilidade de dados {#the-right-to-data-portability}

O direito à portabilidade de dados permite que os titulares de dados obtenham e reutilizem seus Dados Pessoais para seus próprios fins em diferentes serviços. Os Dados Pessoais devem ser fornecidos em um formato estruturado, legível por máquina e comumente usado.

### Recomendação da Braze

Semelhante ao direito de acesso, você pode usar a [REST API]({{site.baseurl}}/api/endpoints/export/#user-export) da Braze para exportar os Dados Pessoais de um usuário final e fornecê-los ao titular dos dados de acordo com sua solicitação. Além disso, entre em contato com o gerente da sua conta com os customer_id(s) e/ou e-mail(s) relevantes para solicitar uma cópia de quaisquer Dados Pessoais mantidos no BrazeAI Decisioning Studio.

## O direito de contestar {#the-right-to-object}

Os indivíduos podem ter o direito de se opor a:

- processamento baseado em interesses legítimos ou no desempenho de uma tarefa de interesse público/exercício de autoridade oficial (incluindo criação de perfis);
- marketing direto (incluindo criação de perfis); e
- processamento para fins de pesquisa científica/histórica e estatística.

### Recomendação da Braze

A Braze oferece a capacidade de marcar um Perfil de Usuário como tendo cancelado a inscrição de SMS, e-mails ou notificações por push por meio de nossas [REST APIs]({{site.baseurl}}/api/home/) e dos SDKs para [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/setting_custom_attributes/), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_custom_attributes/) e [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_custom_attributes/). Se receber objeções dos titulares dos dados quanto ao recebimento de tais mensagens, você pode usar as APIs da Braze para cancelar a inscrição desses usuários finais.

Se isso não for suficiente, para evitar o processamento de Dados Pessoais de usuários finais pela Braze, o perfil do usuário final deverá ser excluído da mesma forma especificada no "Direito à exclusão".


## Direitos relacionados à tomada de decisões automatizadas e à criação de perfis {#rights-related-to-automated-decision-making-and-profiling}

Algumas Leis de Proteção de Dados impedem, ou permitem que os titulares dos dados optem por não participar de, tomada de decisões automatizadas ou criação de perfis em determinadas circunstâncias, em particular para decisões que "produzam um efeito legal ou um efeito similarmente significativo sobre o indivíduo".

### Recomendação da Braze

A Braze não realiza nenhuma ação automatizada de criação de perfil ou tomada de decisão com ramificações legais ou equivalentes para os titulares dos dados. Se você acreditar que seu próprio uso dos Serviços Braze terá impactos legais ou equivalentes e tiver recebido uma objeção a isso, poderá optar por excluir o Perfil de Usuário da mesma forma que no "Direito à exclusão".

## Direcionamento de publicidade {#targeting-advertising}

De acordo com algumas leis de privacidade estaduais dos EUA, os titulares dos dados podem se opor ao uso de seus Dados Pessoais para fins de publicidade direcionada.

### Recomendação da Braze

Ao criar públicos para fins de direcionamento de anúncios para seus titulares de dados, você deve garantir que excluiu todos os titulares de dados que se opuseram à publicidade direcionada, por exemplo, consumidores da Califórnia que exerceram seu direito de "Não vender ou compartilhar" nos termos da CCPA.

Para saber mais sobre como criar públicos para sincronizar com plataformas de terceiros, consulte [Sincronização de públicos]({{site.baseurl}}/partners/canvas_steps/).

## O direito à não discriminação {#the-right-to-non-discrimination}

Os titulares de dados têm o direito de exercer seus direitos de privacidade sem discriminação.

### Recomendação da Braze

Em seu uso dos Serviços Braze, os clientes devem garantir que não discriminem os titulares de dados que tenham exercido seus direitos de privacidade. Por exemplo, recomendamos que os titulares de dados que tenham exercido seus direitos de privacidade não sejam segmentados em públicos ou direcionados de outra forma que possa discriminá-los.