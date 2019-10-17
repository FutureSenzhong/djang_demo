import os

import celery as celery
import pymysql
from celery.schedules import crontab

from my_blog import settings

pymysql.install_as_MySQLdb()


# ע�ỷ��������ע��Django�����ļ���
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'teamproject.settings')
# ����Celery��ʵ����ָ��broker����Ϣ���з���
app = celery.Celery('teamproject', broker='redis://:123456@120.78.155.198:6379/1')
# ��ȡDjango��Ŀ��������Ϣ�����綨ʱ������Ҫ��ȡʱ����
app.config_from_object('django.conf:settings')
# �������ļ�ע���Ӧ���з����첽����Ͷ�ʱ����
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

# ���ö�ʱ����
app.conf.update(
    timezone=settings.TIME_ZONE,
    enable_utc=True,
    # ��ʱ���񣨼ƻ������൱������Ϣ��������
    # ���ֻ��������û����������ô��Ϣ�ͻ�����Ϣ�����л�ѹ
    # ����ʵ�ʲ�����Ŀ��ʱ�������ߡ������ߡ���Ϣ���п��ܶ��ǲ�ͬ�ڵ�
    beat_schedule={
        'export_emp_excel_task': {
            'task': 'common.tasks.auto_export_excel',
            'schedule': crontab(),
        },
    },
)
