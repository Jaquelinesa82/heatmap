from django.urls import reverse
from mapproject.django_assertions import assert_contains
import pytest


@pytest.fixture
def resp(client, db):
    resp = client.get(reverse('dashboard:listData'))
    return resp


def test_status_code(resp):
    assert resp.status_code == 200


def test_title(resp):
    assert_contains(resp, '<title>Heatmap</title>')


def test_listData_link(resp):
    assert_contains(resp, f'href="{reverse("dashboard:listData")}"><h2>Dados</h2></a>')
