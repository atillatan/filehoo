---
---

{% if site.environment=="production" %}
if (window.location.protocol != "https:") window.location.protocol = "https";
{% endif %}

$('a.a-large').bind('click', function() {
  console.log('something');
});
