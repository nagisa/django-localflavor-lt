=====================
django_localflavor_lt
=====================

Country-specific Django helpers for Lithuania.

What's in the Lithuania localflavor?
====================================

* forms.LTIDCodeField: A form field that validated input as a Lithuanian
  identity code. Following checks are made:

  * The number consists of 11 digits.
  * The birthdate is a valid date.
  * The calculated checksum is correct.

* forms.LTCountySelect:  A form ``Select`` widget that uses a list of
  Lithuanian counties as choices.

* forms.LTMunicipalitySelect: A form ``Select`` widget that uses a list of
  Lithuanian municipalities as choices.

See the source code for full details.

About localflavors
==================

Django's "localflavor" packages offer additional functionality for particular
countries or cultures.

For example, these might include form fields for your country's postal codes,
phone number formats or government ID numbers.

This code used to live in Django proper -- in django.contrib.localflavor -- but
was separated into standalone packages in Django 1.5 to keep the framework's
core clean.

For a list of other available localflavors, see https://github.com/django/
