---
nav_title: EduMe
article_title: EduMe
description: "Este artículo de referencia describe la asociación entre Braze y EduMe, una herramienta de formación basada en el móvil que te permite aprovechar el Contenido conectado de Braze para dar a tus usuarios acceso a los cursos y lecciones de EduMe en tus Campaigns de Braze."
alias: /partners/edume/
page_type: partner
search_tag: Partner

---

# EduMe

> [EduMe](https://edume.com) es una herramienta de formación móvil que proporciona a tus trabajadores los conocimientos que necesitan para triunfar, cuando los necesitan y dondequiera que estén.

_Esta integración está mantenida por EduMe._

## Sobre la integración {#about-the-integration}

La integración de Braze y EduMe aprovecha el [Contenido conectado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/#about-connected-content) de Braze para dar a tus usuarios acceso a los cursos y lecciones de EduMe en tus Campaigns de Braze. El progreso individual y de grupo puede seguirse a través de la función de informes de EduMe.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
|---|---|
| Cuenta EduMe | Se necesita una cuenta EduMe para beneficiarse de esta asociación. |
| Clave de API de EduMe | Debes solicitar una clave de API a tu contacto de éxito del cliente de EduMe. Esta clave se utiliza en tu llamada de Contenido conectado de Braze. |
| Secreto de firma de enlace de EduMe | Debes solicitar a tu contacto de éxito del cliente en EduMe que configure un secreto de firma de enlace para tu organización. Este secreto se utiliza para habilitar enlaces sin interrupciones en el Contenido conectado. No tienes que hacer nada con este secreto. |
| ID de grupo y contenido de EduMe | Estos identificadores son necesarios para configurar tus llamadas de Contenido conectado. Ponte en contacto con el servicio de atención al cliente de EduMe si necesitas ayuda para obtener estos identificadores. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración {#integration}

### Crea tu llamada de Contenido conectado {#create-your-connected-content-call}

Para dar acceso a un usuario a un curso, lección o cuestionario eNPS, y hacer un seguimiento de su progreso con tu ID de usuario interno en EduMe, sigue la llamada a la API que se muestra en este ejemplo:

{% raw %}
```
Welcome to my Rickshaw App platform.
Access your onboarding course at:

{% connected_content
  https://connect.edume.com/
  EDUME-CONTENT-LINK-AND-CONTENT-ID&groupId=5681&externalUserId={{${driver_id}}}
  :headers {
       "x-api-key": "YOUR-EDUME-API-KEY"
  }
%}
```
{% endraw %}

1. Sustituye `YOUR-EDUME-API-KEY` por tu clave de API de EduMe.<br><br>
2. Sustituye `EDUME-CONTENT-LINK-AND-CONTENT-ID` por la cadena de enlace de contenido y el identificador de módulo, lección o cuestionario correspondientes. Puedes encontrar estos identificadores en tu cuenta de EduMe.
  - Curso: `getCourseLink?moduleId=12087`
  - Lección: `getLessonLink?lessonId=25805`
  - Cuestionario eNPS: `getSurveyLink?surveyId=654`<br><br>
3. Los usuarios que llegan a EduMe a través de este enlace se añaden a un equipo o grupo de EduMe de tu elección. Sustituye `groupId` por el ID del equipo o del grupo de EduMe correspondiente. Normalmente se utiliza el ID de equipo, excepto para los cursos que requieren inscripción, en cuyo caso debes utilizar el ID de grupo.<br><br>
4. Incluye un campo apropiado para mapear el campo `externalUserId`. El ejemplo de llamada de contenido conectado utiliza `driver_id`, aunque es probable que tu campo sea diferente. Este ID está disponible en los informes de EduMe, lo que te permite correlacionarlos con tus sistemas.<br><br>
5. Por último, personaliza y prueba tu mensaje según sea necesario. Te recomendamos que envíes al menos un mensaje de prueba, accedas al contenido de EduMe, completes la lección o el curso y compruebes que se están registrando los análisis de EduMe.