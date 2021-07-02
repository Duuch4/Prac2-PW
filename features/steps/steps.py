@given(u'Exists a user "user" with password "password"')
def step_impl(context):
    from django.contrib.auth.models import User
    context.user = user
    context.password = password
    User.objects.create_user(username=user, email='user@example.com', password=password)


@given(u'I login as user "user" with password "password"')
def step_impl(context):
    context.browser.get(context.get_url('/accounts/login/?next=/era/'))
    form = context.browser.find_element_by_tag_name('form')
    user = form.find_element_by_id('id_username')
    user.send_keys(user)
    password = form.find_element_by_id('id_password')
    password.send_keys(password)
    login = form.find_element_by_tag_name('input')
    login.click()


@when(u'I create career')
def step_impl(context):
    context.browser.get(context.get_url('/accounts/facultad/9/create/'))
    name = form.find_element_by_id('id_name')
    name.send_keys("GEI")
    desc = form.find_element_by_id('id_description')
    desc.send_keys("Grau en enginyeria informatica")
    submit = form.find_element_by_tag_name('input')
    submit.click()


@then(u'I\'m viewing the details page for career by "user"')
def step_impl(context):
    title = form.find_element_by_tag_name("h1").text
    if "info" not in title:
        raise Exception


@then(u'There are 1 career')
def step_impl(context):
    if len(form.find_elements_by_tag_name("h1")) != 1:
        raise Exception


@when(u'I create faculty')
def step_impl(context):
    context.browser.get(context.get_url('/era/facultad/create'))
    name = form.find_element_by_id('id_name')
    name.send_keys("EPS")
    desc = form.find_element_by_id('id_description')
    desc.send_keys("Escola Politecnica Superior")
    submit = form.find_element_by_tag_name('input')
    submit.click()


@then(u'I\'m viewing the details page for faculty by "user"')
def step_impl(context):
    title = form.find_element_by_tag_name("h1").text
    if "info" not in title:
        raise Exception


@then(u'There are 1 faculty')
def step_impl(context):
    if len(form.find_elements_by_tag_name("h1")) != 1:
        raise Exception


@when(u'I edit a career')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I edit a career')


@then(u'I\'m viewing the details page for career by "user"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I\'m viewing the details page for career by "user"')


@then(u'There are 1 career edited')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then There are 1 career edited')


@when(u'I edit a faculty')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I edit a faculty')


@then(u'I\'m viewing the details page for facultys wich changed by "user"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I\'m viewing the details page for facultys wich changed by "user"')


@then(u'There are 1 faculty edited')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then There are 1 faculty edited')


@when(u'I see the list of the careers')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I see the list of the careers')


@then(u'I\'m viewing the list of all the careers by "user"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I\'m viewing the list of all the careers by "user"')


@then(u'There are X careers in the list')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then There are X careers in the list')


@when(u'I see the list of the facultys')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I see the list of the facultys')


@then(u'I\'m viewing the list of all the facultys by "user"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I\'m viewing the list of all the facultys by "user"')


@then(u'There are X facultys in the list')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then There are X facultys in the list')

