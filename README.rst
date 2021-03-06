=====================
django_localflavor_lt
=====================

Country-specific Django helpers for Lithuania.


=======
WARNING
=======

This app has been superseded by the newly created django-localflavor_ app
which recombines all the different country locaflavors again (after having
been removed from Django). Development and maintenance of this app has
stopped and is only left online as a reminder for the users of those apps.
It will be removed after grace period of 1 Django release (~spring 2014).

.. _django-localflavor: https://github.com/django/django-localflavor/


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

* forms.LTPostalCodeField: A form input that validates
  Lithuanian postal codes in the format XXXXX or LT-XXXXX.

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
