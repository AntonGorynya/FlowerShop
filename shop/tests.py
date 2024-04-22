import pytest
from django.contrib.auth.models import User


@pytest.mark.parametrize('username,email,password', [('john', 'test@test.com', 'pass')])
@pytest.mark.django_db(transaction=True)
def test_add_user(username, email, password):
    user = User.objects.create_user(
        username=username,
        email=email,
        password=password
    )
    User.objects.get(id=user.id)


@pytest.mark.parametrize('user_id', [1, 2])
@pytest.mark.django_db(transaction=True)
def test_raise_exception(user_id):
    with pytest.raises(User.DoesNotExist):
        User.objects.get(id=user_id)
