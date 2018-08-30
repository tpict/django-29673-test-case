# django-29673-test-case
Test case for Django ticket #29673.

Run the following:
```
pipenv install
pipenv run ./manage.py test
```

Result:
```
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
..E.
======================================================================
ERROR: test_internal (django29673.public.tests.Django29673TestCase)
Do stuff with the internal use site.
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/tpict/Projects/django-29673-test-case/django29673/public/tests.py", line 13, in test_internal
    response = self.client.get(reverse("internal-site"))
  File "/home/tpict/Projects/django-29673-test-case/.venv/lib/python3.6/site-packages/django/urls/base.py", line 90, in reverse
    return iri_to_uri(resolver._reverse_with_prefix(view, prefix, *args, **kwargs))
  File "/home/tpict/Projects/django-29673-test-case/.venv/lib/python3.6/site-packages/django/urls/resolvers.py", line 622, in _reverse_with_prefix
    raise NoReverseMatch(msg)
django.urls.exceptions.NoReverseMatch: Reverse for 'internal-site' not found. 'internal-site' is not a valid view function or pattern name.

----------------------------------------------------------------------
Ran 4 tests in 0.006s

FAILED (errors=1)
Destroying test database for alias 'default'...
```

Next, run the following:
```
pipenv run ./manage.py test django29673.base
pipenv run ./manage.py test django29673.public
```


All tests should pass.

An example workaround is included in `django29673/base/middleware.py`.
