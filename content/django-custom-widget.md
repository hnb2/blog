Title: Custom widgets and templates with Django 1.11
Date: 2017-11-02 20:00
Category: Misc
Tags: python, django, widget, template

Since the release of Django 1.11, there have been changes on how you can create custom widgets and notably how to use your own templates. Here's a quick sumup of how I reached my goal browsing through official doc, Django's source code on Github and numerous stackoverflow posts.

## Define your own widget

Let's say you want to make a custom radio radiogroup to support those [cool material design bootstrap ones](https://mdbootstrap.com/components/bootstrap-radio-button/):

```py
# Inside forms.py
from django import forms

# Let's define our new radio buttons
class MaterialBootstrapRadioButtons(forms.RadioSelect):
    template_name = 'forms/widget/material_bootstrap_radio_buttons.html'
    option_template_name = 'forms/widget/material_bootstrap_radio_button.html'
```

As you can see we defined a simple Widget off the original `RadioSelect`, we do not want to change the widget itself, just the way it looks like. We also created 2 files in our `templates/form/widget` directory.

 * `template_name` holds the template for the actual radio button group
 * `option_template_name` holds the template for the option (a single radio button here)

Here is *material_bootstrap_radio_buttons.html*, which is simplified version of [the original one](https://github.com/django/django/blob/master/django/forms/templates/django/forms/widgets/multiple_input.html):

```html
{% for group, options, index in widget.optgroups %}
    {% for option in options %}
        {% include option.template_name with widget=option %}
    {% endfor %}
{% endfor %}
```

And here is *material_bootstrap_radio_button.html*:

```html
<div class="form-group">
    <input type="radio" id="{{widget.attrs.id}}" name="{{widget.name}}" value="{{widget.value}}" />
    <label for="{{widget.attrs.id}}">{{widget.value}}</label>
</div>
```

Now that we defined our widget, let's use it:

```py
# Still inside forms.py

class RatingForm(forms.Form):
    CHOICES = [(1, 1,), (2, 2,), (3, 3,), (4, 4,), (5, 5,)]
    rating = forms.ChoiceField(
        choices=CHOICES,
        widget=MaterialBootstrapRadioButtons()
    )
    comment = forms.CharField(widget=forms.Textarea())
```

## Modify the settings to support your new templates

Now the issue is that our templates are not "connected" to anything and cannot be found.

Since Django 1.11 we need to add the following to our `settings.py`:

```py
INSTALLED_APPS = [
    # ...
    'django.forms',
]

FORM_RENDERER = 'django.forms.renderers.TemplatesSetting'

TEMPLATES = [
    # ...
    'DIRS': ['templates'],
    'APP_DIRS': True,
    # ...
]
```

A couple of things to note here:

 * `django.forms` is a "new" app to add to our `INSTALLED_APPS`. That way Django can also find it's default form templates.
 * `FORM_RENDERER` is a new settings to mention that our form rendering will not rely on the [built-in form renderer](https://docs.djangoproject.com/en/1.11/ref/forms/renderers/#built-in-template-form-renderers) but on our own, so we can use our own templates.
 * `TEMPLATES` should have our own template's home directory set in `DIRS` and have `APP_DIRS` set to True (which is usually always the case, but i'd rather mention just in case)

## Learn More

You have now a good starting point to create your own useful widget, here are a couple of pointers on how to understand all this better:

 * Django's source code [for the forms module](https://github.com/django/django/tree/master/django/forms)
 * The new [form rendering API](https://docs.djangoproject.com/en/1.11/ref/forms/renderers/), introduced in Django 1.11
 * The [backward incompatibility notes about widget rendering](https://docs.djangoproject.com/en/1.11/releases/1.11/#changes-due-to-the-introduction-of-template-based-widget-rendering), introduced as well in Django 1.11
 * The rather complete [widget doc](https://docs.djangoproject.com/en/1.11/ref/forms/widgets/)
