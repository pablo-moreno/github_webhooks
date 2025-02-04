import logging
from django.db import models
from rest_framework.request import Request

logger = logging.getLogger('webhooks')


class Application(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=240, blank=True, null=True)
    repository = models.URLField(unique=True)
    deploy_script = models.CharField(max_length=200, blank=True, null=True)
    version = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return f'{self.name}@{self.version}'


class WebHook(models.Model):
    type = models.CharField(max_length=50)
    repository = models.URLField(blank=True, null=True)
    action = models.CharField(max_length=24, blank=True, null=True)
    url = models.CharField(max_length=200, blank=True, null=True)
    author = models.CharField(max_length=16, blank=True, null=True)
    version = models.CharField(max_length=16, blank=True, null=True)
    prerelease = models.BooleanField(default=True)

    @staticmethod
    def from_github(request):
        """
            Parses a Github request and returns a WebHook instance
        :param request:
        :return:
        """
        webhook = WebHook()
        webhook_type = request.META.get('HTTP_X_GITHUB_EVENT', None)
        data = request.data
        webhook.type = webhook_type
        webhook.repository = data.get('repository', {}).get('html_url')
        webhook.action = data.get('action')

        if webhook_type == 'release':
            webhook.url = data.get('release', {}).get('url')
            webhook.author = data.get('release', {}).get('author', {}).get('login')
            webhook.version = data.get('release', {}).get('tag_name', None)
            webhook.prerelease = data.get('release', {}).get('prerelease', True)

        return webhook

    @staticmethod
    def from_gitlab(request: Request) -> 'WebHook':
        """
            Parses a Gitlab request and returns a WebHook instance
        :param request:
        :return:
        """
        return WebHook()

    def __str__(self):
        return f'({self.type}) ({self.action}): {self.repository}'


class Deploy(models.Model):
    PEN = 'PEN'
    DNG = 'DNG'
    OK = 'OK'
    KO = 'KO'

    DEPLOY_STATUSES = (
        (PEN, 'PENDING'),
        (DNG, 'DOING'),
        (OK, 'DONE'),
        (KO, 'ERROR'),
    )

    app = models.ForeignKey(Application, on_delete=models.CASCADE, null=True)
    started_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=DEPLOY_STATUSES, max_length=16)

    def __str__(self):
        return f'{self.app.name} - {self.status}'
