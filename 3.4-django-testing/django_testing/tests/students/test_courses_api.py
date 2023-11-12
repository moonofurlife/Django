import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from model_bakery import baker

from students.models import Course, Student


@pytest.fixture
def client():
    return APIClient()
@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return factory

@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)
    return factory

@pytest.fixture
def user():
    return User.objects.create_user('admin')

@pytest.mark.django_db
def test_get_course(client, user, course_factory):
    # тест одного курса

    course = course_factory()

    response = client.get(f'/api/v1/courses/{course.id}/')

    data = response.json()
    assert response.status_code == 200
    assert data['name'] == course.name


@pytest.mark.django_db
def test_get_course(client, user, course_factory):
    #тест курсов

    quantity = 1000
    course = course_factory(_quantity=quantity)

    response = client.get(f'/api/v1/courses/')

    data = response.json()
    assert response.status_code == 200
    assert len(data) == quantity
    for i, m in enumerate(data):
        assert course[i].name == m['name']

@pytest.mark.django_db
def test_get_filter_cource(client, user, course_factory):
    #тест фильтра

    courses = course_factory(_quantity=10)
    i = 4

    response = client.get('/api/v1/courses/', {'id': courses[i].id, 'name': courses[i].name},)

    assert response.status_code == 200
    assert courses[i].id == response.json()[0]['id']
    assert courses[i].name == response.json()[0]['name']

@pytest.mark.django_db
def test_create_course(client):
    # тест успешного создания курса

    count = Course.objects.count()
    name = 'Python from zero'

    response1 = client.post('/api/v1/courses/', data={'name': name})
    response2 = client.get(f'/api/v1/courses/?name={name}')
    response3 = client.get(f'/api/v1/courses/{response1.json()["id"]}/')

    assert response1.status_code == 201
    assert Course.objects.count() == count + 1
    assert response2.status_code == 200
    assert name == response3.json()['name']

@pytest.mark.django_db
def test_update_delete_course(client, course_factory):
    # тест успешного обновления курса и удаления
    courses = course_factory(_quantity=2)

    response1 = client.patch(f'/api/v1/courses/{courses[0].id}/', data={'name': 'Python from zero'})
    response2 = client.delete(f'/api/v1/courses/{courses[1].id}/')
    response3 = client.get(f'/api/v1/courses/{courses[1].id}/')

    assert response1.status_code == 200
    assert response2.status_code == 204
    assert response3.status_code == 404
